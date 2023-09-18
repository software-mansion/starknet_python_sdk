import sys
from typing import cast
from unittest.mock import AsyncMock, patch

import pytest

from starknet_py.contract import Contract
from starknet_py.hash.address import compute_address
from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.account.account import Account
from starknet_py.net.account.base_account import BaseAccount
from starknet_py.net.client_errors import ClientError
from starknet_py.net.client_models import (
    Call,
    DeployAccountTransaction,
    DeployAccountTransactionResponse,
    EstimatedFee,
    SierraContractClass,
    TransactionStatus,
)
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.models import StarknetChainId
from starknet_py.net.models.transaction import Declare, DeclareV2
from starknet_py.net.signer.stark_curve_signer import KeyPair
from starknet_py.net.udc_deployer.deployer import Deployer
from starknet_py.tests.e2e.fixtures.constants import MAX_FEE


@pytest.mark.run_on_devnet
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client",
    [GatewayClient(net="custom.net"), FullNodeClient(node_url="custom.net/rpc")],
)
async def test_get_balance_throws_when_token_not_specified(account, client):
    modified_account = Account(
        address=account.address,
        client=client,
        key_pair=KeyPair(1, 2),
        chain=cast(StarknetChainId, 1),
    )
    with pytest.raises(
        ValueError,
        match="Argument token_address must be specified when using a custom network.",
    ):
        await modified_account.get_balance()


@pytest.mark.asyncio
async def test_balance_when_token_specified(account, erc20_contract):
    balance = await account.get_balance(erc20_contract.address)

    assert balance == 200


@pytest.mark.asyncio
async def test_estimated_fee_greater_than_zero(erc20_contract, account):
    erc20_contract = Contract(
        address=erc20_contract.address, abi=erc20_contract.data.abi, provider=account
    )

    estimated_fee = (
        await erc20_contract.functions["balanceOf"]
        .prepare("1234", max_fee=0)
        .estimate_fee(block_hash="latest")
    )

    assert estimated_fee.overall_fee > 0
    assert (
        estimated_fee.gas_price * estimated_fee.gas_usage == estimated_fee.overall_fee
    )


@pytest.mark.asyncio
async def test_estimate_fee_for_declare_transaction(account, map_compiled_contract):
    declare_tx = await account.sign_declare_transaction(
        compiled_contract=map_compiled_contract, max_fee=MAX_FEE
    )

    estimated_fee = await account.client.estimate_fee(tx=declare_tx)

    assert isinstance(estimated_fee.overall_fee, int)
    assert estimated_fee.overall_fee > 0
    assert (
        estimated_fee.gas_usage * estimated_fee.gas_price == estimated_fee.overall_fee
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("key, val", [(20, 20), (30, 30)])
async def test_sending_multicall(account, map_contract, key, val):
    calls = [
        map_contract.functions["put"].prepare(key=10, value=10),
        map_contract.functions["put"].prepare(key=key, value=val),
    ]

    res = await account.execute(calls=calls, max_fee=int(1e20))
    await account.client.wait_for_tx(res.transaction_hash)

    (value,) = await map_contract.functions["get"].call(key=key)

    assert value == val


@pytest.mark.run_on_devnet
@pytest.mark.asyncio
async def test_get_block_traces(gateway_account):
    traces = await gateway_account.client.trace_block_transactions(block_number=2)

    assert traces.traces != []


@pytest.mark.asyncio
async def test_rejection_reason_in_transaction_receipt(map_contract):
    with pytest.raises(ClientError, match=r".*INSUFFICIENT_MAX_FEE.*"):
        _ = await map_contract.functions["put"].invoke(key=10, value=20, max_fee=1)


def test_sign_and_verify_offchain_message_fail(account, typed_data):
    signature = account.sign_message(typed_data)
    signature = [signature[0] + 1, signature[1]]
    result = account.verify_message(typed_data, signature)

    assert result is False


def test_sign_and_verify_offchain_message(account, typed_data):
    signature = account.sign_message(typed_data)
    result = account.verify_message(typed_data, signature)

    assert result is True


@pytest.mark.asyncio
async def test_get_class_hash_at(map_contract, account):
    class_hash = await account.client.get_class_hash_at(
        map_contract.address, block_hash="latest"
    )

    assert class_hash != 0


# TODO (#1154): remove line below
@pytest.mark.xfail(
    "--client=gateway" in sys.argv,
    reason="0.12.2 returns Felts in state_root, devnet returns NonPrefixedHex",
)
@pytest.mark.asyncio()
async def test_get_nonce(account, map_contract):
    nonce = await account.get_nonce()
    address = map_contract.address
    block = await account.client.get_block(block_number="latest")

    tx = await account.execute(
        Call(
            to_addr=address, selector=get_selector_from_name("put"), calldata=[10, 20]
        ),
        max_fee=MAX_FEE,
    )
    await account.client.wait_for_tx(tx.transaction_hash)

    new_nonce = await account.get_nonce()
    new_nonce_latest_block = await account.get_nonce(block_number="latest")

    old_nonce = await account.get_nonce(block_number=block.block_number)

    assert isinstance(nonce, int) and isinstance(new_nonce, int)
    assert new_nonce == nonce + 1

    assert old_nonce == nonce
    assert new_nonce_latest_block == new_nonce


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "calls", [[Call(10, 20, [30])], [Call(10, 20, [30]), Call(40, 50, [60])]]
)
async def test_sign_invoke_transaction(account, calls):
    signed_tx = await account.sign_invoke_transaction(calls, max_fee=MAX_FEE)

    assert isinstance(signed_tx.signature, list)
    assert len(signed_tx.signature) > 0
    assert signed_tx.max_fee == MAX_FEE


@pytest.mark.asyncio
async def test_sign_invoke_transaction_auto_estimate(account, map_contract):
    signed_tx = await account.sign_invoke_transaction(
        Call(map_contract.address, get_selector_from_name("put"), [3, 4]),
        auto_estimate=True,
    )

    assert isinstance(signed_tx.signature, list)
    assert len(signed_tx.signature) > 0
    assert signed_tx.max_fee > 0


@pytest.mark.asyncio
async def test_sign_declare_transaction(account, map_compiled_contract):
    signed_tx = await account.sign_declare_transaction(
        map_compiled_contract, max_fee=MAX_FEE
    )

    assert isinstance(signed_tx, Declare)
    assert signed_tx.version == 1
    assert isinstance(signed_tx.signature, list)
    assert len(signed_tx.signature) > 0
    assert signed_tx.max_fee == MAX_FEE


@pytest.mark.asyncio
async def test_sign_declare_transaction_auto_estimate(account, map_compiled_contract):
    signed_tx = await account.sign_declare_transaction(
        map_compiled_contract, auto_estimate=True
    )

    assert isinstance(signed_tx, Declare)
    assert signed_tx.version == 1
    assert isinstance(signed_tx.signature, list)
    assert len(signed_tx.signature) > 0
    assert signed_tx.max_fee > 0


@pytest.mark.asyncio
async def test_sign_declare_v2_transaction(
    account, sierra_minimal_compiled_contract_and_class_hash
):
    (
        compiled_contract,
        compiled_class_hash,
    ) = sierra_minimal_compiled_contract_and_class_hash

    signed_tx = await account.sign_declare_v2_transaction(
        compiled_contract,
        compiled_class_hash=compiled_class_hash,
        max_fee=MAX_FEE,
    )

    assert isinstance(signed_tx, DeclareV2)
    assert signed_tx.version == 2
    assert isinstance(signed_tx.signature, list)
    assert len(signed_tx.signature) > 0
    assert signed_tx.max_fee == MAX_FEE


@pytest.mark.asyncio
async def test_sign_declare_v2_transaction_auto_estimate(
    account, sierra_minimal_compiled_contract_and_class_hash
):
    (
        compiled_contract,
        compiled_class_hash,
    ) = sierra_minimal_compiled_contract_and_class_hash

    signed_tx = await account.sign_declare_v2_transaction(
        compiled_contract,
        compiled_class_hash=compiled_class_hash,
        auto_estimate=True,
    )

    assert isinstance(signed_tx, DeclareV2)
    assert signed_tx.version == 2
    assert isinstance(signed_tx.signature, list)
    assert len(signed_tx.signature) > 0
    assert signed_tx.max_fee > 0


@pytest.mark.asyncio
async def test_declare_contract_raises_on_sierra_contract_without_compiled_class_hash(
    sierra_minimal_compiled_contract_and_class_hash, account
):
    compiled_contract, _ = sierra_minimal_compiled_contract_and_class_hash
    with pytest.raises(
        ValueError,
        match="Signing sierra contracts requires using `sign_declare_v2_transaction` method.",
    ):
        await account.sign_declare_transaction(compiled_contract=compiled_contract)


@pytest.mark.asyncio
async def test_sign_deploy_account_transaction(account):
    class_hash = 0x1234
    salt = 0x123
    calldata = [1, 2, 3]
    signed_tx = await account.sign_deploy_account_transaction(
        class_hash, salt, calldata, max_fee=MAX_FEE
    )

    assert isinstance(signed_tx.signature, list)
    assert len(signed_tx.signature) > 0
    assert signed_tx.max_fee == MAX_FEE
    assert signed_tx.class_hash == class_hash
    assert signed_tx.contract_address_salt == salt
    assert signed_tx.constructor_calldata == calldata


@pytest.mark.asyncio
async def test_sign_deploy_account_transaction_auto_estimate(
    account, account_with_validate_deploy_class_hash
):
    class_hash = account_with_validate_deploy_class_hash
    salt = 0x1234
    calldata = [account.signer.public_key]
    signed_tx = await account.sign_deploy_account_transaction(
        class_hash, salt, calldata, auto_estimate=True
    )

    assert isinstance(signed_tx.signature, list)
    assert len(signed_tx.signature) > 0
    assert signed_tx.max_fee > 0
    assert signed_tx.class_hash == class_hash
    assert signed_tx.contract_address_salt == salt
    assert signed_tx.constructor_calldata == calldata


@pytest.mark.skip("No 0.12.1 devnet")
@pytest.mark.asyncio
async def test_deploy_account(client, deploy_account_details_factory, map_contract):
    address, key_pair, salt, class_hash = await deploy_account_details_factory.get()

    deploy_result = await Account.deploy_account(
        address=address,
        class_hash=class_hash,
        salt=salt,
        key_pair=key_pair,
        client=client,
        chain=StarknetChainId.TESTNET,
        max_fee=int(1e16),
    )
    await deploy_result.wait_for_acceptance()

    account = deploy_result.account

    assert isinstance(account, BaseAccount)
    assert account.address == address

    # Test making a tx
    res = await account.execute(
        calls=Call(
            to_addr=map_contract.address,
            selector=get_selector_from_name("put"),
            calldata=[30, 40],
        ),
        max_fee=MAX_FEE,
    )
    tx_receipt = await account.client.wait_for_tx(res.transaction_hash)

    assert tx_receipt.finality_status in (
        TransactionStatus.ACCEPTED_ON_L1,
        TransactionStatus.ACCEPTED_ON_L2,
    )


@pytest.mark.asyncio
async def test_deploy_account_raises_on_incorrect_address(
    client, deploy_account_details_factory
):
    address, key_pair, salt, class_hash = await deploy_account_details_factory.get()

    with pytest.raises(
        ValueError,
        match=f"Provided address {hex(0x111)} is different than computed address {hex(address)}",
    ):
        await Account.deploy_account(
            address=0x111,
            class_hash=class_hash,
            salt=salt,
            key_pair=key_pair,
            client=client,
            chain=StarknetChainId.TESTNET,
            max_fee=MAX_FEE,
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "call_contract, client",
    [
        (
            "starknet_py.net.gateway_client.GatewayClient.call_contract",
            "gateway_client",
        ),
        (
            "starknet_py.net.full_node_client.FullNodeClient.call_contract",
            "full_node_client",
        ),
    ],
)
async def test_deploy_account_raises_on_no_enough_funds(
    deploy_account_details_factory, call_contract, client, request
):
    client = request.getfixturevalue(client)
    address, key_pair, salt, class_hash = await deploy_account_details_factory.get()

    with patch(call_contract, AsyncMock()) as mocked_balance:
        mocked_balance.return_value = (0, 0)

        with pytest.raises(
            ValueError,
            match="Not enough tokens at the specified address to cover deployment costs",
        ):
            await Account.deploy_account(
                address=address,
                class_hash=class_hash,
                salt=salt,
                key_pair=key_pair,
                client=client,
                chain=StarknetChainId.TESTNET,
                max_fee=MAX_FEE,
            )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client_method_path, client",
    [
        (
            "starknet_py.net.gateway_client.GatewayClient",
            "gateway_client",
        ),
        (
            "starknet_py.net.full_node_client.FullNodeClient",
            "full_node_client",
        ),
    ],
)
async def test_deploy_account_passes_on_enough_funds(
    deploy_account_details_factory, client_method_path, client, request
):
    address, key_pair, salt, class_hash = await deploy_account_details_factory.get()
    client = request.getfixturevalue(client)

    with patch(
        client_method_path + ".call_contract", AsyncMock()
    ) as mocked_balance, patch(
        client_method_path + ".deploy_account", AsyncMock()
    ) as mocked_deploy:
        mocked_balance.return_value = (0, 100)
        mocked_deploy.return_value = DeployAccountTransactionResponse(
            transaction_hash=0x1
        )

        await Account.deploy_account(
            address=address,
            class_hash=class_hash,
            salt=salt,
            key_pair=key_pair,
            client=client,
            chain=StarknetChainId.TESTNET,
            max_fee=MAX_FEE,
        )


# TODO (#1056): change this test to braavos account
@pytest.mark.skip(
    reason="'__validate_execute__' doesn't allow any other calldata than in the constructor"
)
@pytest.mark.asyncio
async def test_deploy_account_uses_custom_calldata(
    client, deploy_account_details_factory, fee_contract
):
    _, key_pair, salt, class_hash = await deploy_account_details_factory.get()
    calldata = [1, 2, 3, 4]
    address = compute_address(
        salt=salt,
        class_hash=class_hash,
        constructor_calldata=calldata,
        deployer_address=0,
    )

    res = await fee_contract.functions["transfer"].invoke(
        recipient=address, amount=int(1e16), max_fee=MAX_FEE
    )
    await res.wait_for_acceptance()

    deploy_result = await Account.deploy_account(
        address=address,
        class_hash=class_hash,
        salt=salt,
        key_pair=key_pair,
        client=client,
        chain=StarknetChainId.TESTNET,
        constructor_calldata=calldata,
        max_fee=int(1e16),
    )

    tx = await client.get_transaction(deploy_result.hash)
    assert isinstance(tx, DeployAccountTransaction)
    assert tx.constructor_calldata == calldata


@pytest.mark.asyncio
async def test_sign_invoke_tx_for_fee_estimation(account, map_contract):
    call = map_contract.functions["put"].prepare(key=40, value=50)
    transaction = await account.sign_invoke_transaction(calls=call, max_fee=MAX_FEE)

    estimate_fee_transaction = await account.sign_for_fee_estimate(transaction)

    estimation = await account.client.estimate_fee(estimate_fee_transaction)
    assert estimation.overall_fee > 0

    # Verify that the transaction signed for fee estimation cannot be sent
    with pytest.raises(ClientError):
        await account.client.send_transaction(estimate_fee_transaction)

    # Verify that original transaction can be sent
    result = await account.client.send_transaction(transaction)
    await account.client.wait_for_tx(result.transaction_hash)


@pytest.mark.asyncio
async def test_sign_declare_tx_for_fee_estimation(account, map_compiled_contract):
    transaction = await account.sign_declare_transaction(
        compiled_contract=map_compiled_contract, max_fee=MAX_FEE
    )

    estimate_fee_transaction = await account.sign_for_fee_estimate(transaction)

    estimation = await account.client.estimate_fee(estimate_fee_transaction)
    assert estimation.overall_fee > 0

    # Verify that the transaction signed for fee estimation cannot be sent
    with pytest.raises(ClientError):
        await account.client.declare(estimate_fee_transaction)

    # Verify that original transaction can be sent
    result = await account.client.declare(transaction)
    await account.client.wait_for_tx(result.transaction_hash)


@pytest.mark.asyncio
async def test_sign_deploy_account_tx_for_fee_estimation(
    client, deploy_account_details_factory
):
    address, key_pair, salt, class_hash = await deploy_account_details_factory.get()

    account = Account(
        address=address,
        client=client,
        key_pair=key_pair,
        chain=StarknetChainId.TESTNET,
    )

    transaction = await account.sign_deploy_account_transaction(
        class_hash=class_hash,
        contract_address_salt=salt,
        constructor_calldata=[key_pair.public_key],
        max_fee=MAX_FEE,
    )

    estimate_fee_transaction = await account.sign_for_fee_estimate(transaction)

    estimation = await account.client.estimate_fee(transaction)
    assert isinstance(estimation, EstimatedFee)
    assert estimation.overall_fee > 0

    # Verify that the transaction signed for fee estimation cannot be sent
    with pytest.raises(ClientError):
        await account.client.deploy_account(estimate_fee_transaction)

    # Verify that original transaction can be sent
    result = await account.client.deploy_account(transaction)
    await account.client.wait_for_tx(result.transaction_hash)


@pytest.mark.asyncio
async def test_sign_transaction_custom_nonce(account, cairo1_hello_starknet_class_hash):
    deployment = Deployer().create_contract_deployment(cairo1_hello_starknet_class_hash)
    deploy_tx = await account.sign_invoke_transaction(deployment.call, max_fee=MAX_FEE)

    new_balance = 30
    invoke_tx = await account.sign_invoke_transaction(
        Call(
            deployment.address,
            get_selector_from_name("increase_balance"),
            [new_balance],
        ),
        nonce=deploy_tx.nonce + 1,
        max_fee=MAX_FEE,
    )

    deploy_res = await account.client.send_transaction(deploy_tx)
    invoke_res = await account.client.send_transaction(invoke_tx)

    await account.client.wait_for_tx(deploy_res.transaction_hash)
    await account.client.wait_for_tx(invoke_res.transaction_hash)

    result = await account.client.call_contract(
        Call(deployment.address, get_selector_from_name("get_balance"), [])
    )

    assert invoke_tx.nonce == deploy_tx.nonce + 1
    assert result == [new_balance]


@pytest.mark.asyncio
async def test_argent_cairo1_account_deploy(
    full_node_client,
    argent_cairo1_account_class_hash,
    deploy_account_details_factory,
):
    address, key_pair, salt, class_hash = await deploy_account_details_factory.get(
        class_hash=argent_cairo1_account_class_hash, argent_calldata=True
    )

    deploy_result = await Account.deploy_account(
        address=address,
        class_hash=class_hash,
        salt=salt,
        key_pair=key_pair,
        client=full_node_client,
        cairo_version=1,
        constructor_calldata=[key_pair.public_key, 0],
        chain=StarknetChainId.TESTNET,
        max_fee=int(1e16),
    )
    await deploy_result.wait_for_acceptance()
    account = deploy_result.account

    assert isinstance(account, BaseAccount)
    assert account.cairo_version == 1

    account_contract_class = await full_node_client.get_class_at(
        contract_address=account.address, block_number="latest"
    )

    assert isinstance(account_contract_class, SierraContractClass)


@pytest.mark.asyncio
async def test_argent_cairo1_account_execute(
    deployed_balance_contract,
    argent_cairo1_account: BaseAccount,
):
    # verify that initial balance is 0
    get_balance_call = Call(
        to_addr=deployed_balance_contract.address,
        selector=get_selector_from_name("get_balance"),
        calldata=[],
    )
    get_balance = await argent_cairo1_account.client.call_contract(
        call=get_balance_call, block_number="latest"
    )

    assert get_balance[0] == 0

    value = 20
    increase_balance_by_20_call = Call(
        to_addr=deployed_balance_contract.address,
        selector=get_selector_from_name("increase_balance"),
        calldata=[value],
    )
    execute = await argent_cairo1_account.execute(
        calls=increase_balance_by_20_call, max_fee=int(1e16)
    )
    await argent_cairo1_account.client.wait_for_tx(tx_hash=execute.transaction_hash)
    receipt = await argent_cairo1_account.client.get_transaction_receipt(
        tx_hash=execute.transaction_hash
    )

    # TODO (#1179): devnet 0.3.0 still return STATUS instead of FINALITY_STATUS
    assert receipt.status == TransactionStatus.ACCEPTED_ON_L2

    # verify that the previous call was executed
    get_balance_call = Call(
        to_addr=deployed_balance_contract.address,
        selector=get_selector_from_name("get_balance"),
        calldata=[],
    )
    get_balance = await argent_cairo1_account.client.call_contract(
        call=get_balance_call, block_number="latest"
    )

    assert get_balance[0] == value


# TODO (#1184): remove that
@pytest.mark.asyncio
async def test_cairo1_account_deprecations(
    deployed_balance_contract,
    argent_cairo1_account: BaseAccount,
):
    call = Call(
        to_addr=deployed_balance_contract.address,
        selector=get_selector_from_name("increase_balance"),
        calldata=[20],
    )
    with pytest.warns(
        UserWarning,
        match="Parameter 'cairo_version' has been deprecated. Please use argument 'cairo_version' in Account constructor.",
    ):
        _ = await argent_cairo1_account.execute(
            calls=call, max_fee=int(1e16), cairo_version=1
        )
        _ = await argent_cairo1_account.sign_invoke_transaction(
            calls=call, max_fee=int(1e16), cairo_version=1
        )
