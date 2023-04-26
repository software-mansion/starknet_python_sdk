import dataclasses
from typing import Tuple
from unittest.mock import AsyncMock, patch

import pytest

from starknet_py.hash.selector import get_selector_from_name
from starknet_py.hash.storage import get_storage_var_address
from starknet_py.net.client_errors import ContractNotFoundError
from starknet_py.net.client_models import (
    Call,
    CasmClass,
    CasmClassEntryPointsByType,
    DeclaredContractHash,
    DeclareTransaction,
    DeployTransaction,
    L1HandlerTransaction,
    ReplacedClass,
    SierraContractClass,
    SierraEntryPointsByType,
    TransactionStatus,
    TransactionStatusResponse,
)
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.models.transaction import DeclareV2
from starknet_py.net.networks import MAINNET, TESTNET, TESTNET2, CustomGatewayUrls
from starknet_py.tests.e2e.fixtures.constants import MAX_FEE
from starknet_py.tests.e2e.fixtures.misc import read_contract


@pytest.mark.asyncio
async def test_get_class_by_hash_sierra_program(
    gateway_client, hello_starknet_class_hash_tx_hash: Tuple[int, int]
):
    # TODO: Replace with `client` when RPC 0.3.0 is supported
    client = gateway_client
    (class_hash, _) = hello_starknet_class_hash_tx_hash

    contract_class = await client.get_class_by_hash(class_hash=class_hash)

    assert isinstance(contract_class, SierraContractClass)
    assert contract_class.contract_class_version == "0.1.0"
    assert isinstance(contract_class.sierra_program, list)
    assert isinstance(contract_class.entry_points_by_type, SierraEntryPointsByType)
    assert isinstance(contract_class.abi, str)


@pytest.mark.asyncio
async def test_get_declare_v2_transaction(
    gateway_client,
    hello_starknet_class_hash_tx_hash: Tuple[int, int],
    declare_v2_hello_starknet: DeclareV2,
):
    # TODO: Replace with `client` when RPC 0.3.0 is supported
    client = gateway_client
    (class_hash, tx_hash) = hello_starknet_class_hash_tx_hash

    transaction = await client.get_transaction(tx_hash=tx_hash)

    assert isinstance(transaction, DeclareTransaction)
    assert transaction == DeclareTransaction(
        class_hash=class_hash,
        compiled_class_hash=declare_v2_hello_starknet.compiled_class_hash,
        sender_address=declare_v2_hello_starknet.sender_address,
        hash=tx_hash,
        max_fee=declare_v2_hello_starknet.max_fee,
        signature=declare_v2_hello_starknet.signature,
        nonce=declare_v2_hello_starknet.nonce,
        version=declare_v2_hello_starknet.version,
    )


@pytest.mark.asyncio
async def test_get_block_with_declare_v2(
    gateway_client,
    hello_starknet_class_hash_tx_hash: Tuple[int, int],
    declare_v2_hello_starknet: DeclareV2,
    block_with_declare_v2_number: int,
):
    # TODO: Replace with `client` when RPC 0.3.0 is supported
    client = gateway_client
    (class_hash, tx_hash) = hello_starknet_class_hash_tx_hash

    block = await client.get_block(block_number=block_with_declare_v2_number)

    assert (
        DeclareTransaction(
            class_hash=class_hash,
            compiled_class_hash=declare_v2_hello_starknet.compiled_class_hash,
            sender_address=declare_v2_hello_starknet.sender_address,
            hash=tx_hash,
            max_fee=declare_v2_hello_starknet.max_fee,
            signature=declare_v2_hello_starknet.signature,
            nonce=declare_v2_hello_starknet.nonce,
            version=declare_v2_hello_starknet.version,
        )
        in block.transactions
    )


@pytest.mark.asyncio
async def test_get_new_state_update(
    gateway_client,
    hello_starknet_class_hash_tx_hash: Tuple[int, int],
    declare_v2_hello_starknet: DeclareV2,
    block_with_declare_v2_number: int,
    replaced_class: Tuple[int, int, int],
):
    # TODO: Replace with `client` when RPC 0.3.0 is supported
    client = gateway_client
    (class_hash, _) = hello_starknet_class_hash_tx_hash

    state_update = await client.get_state_update(
        block_number=block_with_declare_v2_number
    )

    assert state_update.state_diff.replaced_classes == []
    assert (
        DeclaredContractHash(
            class_hash=class_hash,
            compiled_class_hash=declare_v2_hello_starknet.compiled_class_hash,
        )
        in state_update.state_diff.declared_contract_hashes
    )

    (block_number, contract_address, class_hash) = replaced_class
    state_update = await client.get_state_update(block_number=block_number)

    assert (
        ReplacedClass(contract_address=contract_address, class_hash=class_hash)
        in state_update.state_diff.replaced_classes
    )


@pytest.mark.asyncio
async def test_get_compiled_class_by_class_hash(
    gateway_client, hello_starknet_class_hash_tx_hash: Tuple[int, int]
):
    # TODO: Replace with `client` when RPC 0.3.0 is supported
    client = gateway_client
    (class_hash, _) = hello_starknet_class_hash_tx_hash

    compiled_class = await client.get_compiled_class_by_class_hash(
        class_hash=class_hash
    )

    assert isinstance(compiled_class, CasmClass)
    assert isinstance(compiled_class.prime, int)
    assert isinstance(compiled_class.bytecode, list)
    assert isinstance(compiled_class.hints, list)
    assert isinstance(compiled_class.pythonic_hints, list)
    assert isinstance(compiled_class.compiler_version, str)
    assert isinstance(compiled_class.entry_points_by_type, CasmClassEntryPointsByType)


@pytest.mark.asyncio
async def test_gateway_raises_on_both_block_hash_and_number(
    block_with_declare_number, gateway_client
):
    with pytest.raises(
        ValueError,
        match="Arguments block_hash and block_number are mutually exclusive.",
    ):
        await gateway_client.get_block(
            block_hash="0x0", block_number=block_with_declare_number
        )


@pytest.mark.asyncio
async def test_get_class_hash_at(contract_address, gateway_client, class_hash):
    class_hash_resp = await gateway_client.get_class_hash_at(
        contract_address=contract_address
    )

    assert class_hash_resp == class_hash


@pytest.mark.asyncio
async def test_estimate_fee_bulk(
    contract_address, gateway_client, deploy_account_transaction, account
):
    invoke_tx = await account.sign_invoke_transaction(
        calls=Call(
            to_addr=contract_address,
            selector=get_selector_from_name("increase_balance"),
            calldata=[123],
        ),
        max_fee=MAX_FEE,
    )
    invoke_tx = await account.sign_for_fee_estimate(invoke_tx)

    declare_tx = await account.sign_declare_transaction(
        compiled_contract=read_contract("map_compiled.json"), max_fee=MAX_FEE
    )
    declare_tx = dataclasses.replace(declare_tx, nonce=invoke_tx.nonce + 1)
    declare_tx = await account.sign_for_fee_estimate(declare_tx)

    transactions = [invoke_tx, declare_tx, deploy_account_transaction]

    estimated_fees = await gateway_client.estimate_fee_bulk(
        transactions=transactions, block_number="latest"
    )

    assert isinstance(estimated_fees, list)

    for estimated_fee in estimated_fees:
        assert isinstance(estimated_fee.overall_fee, int)
        assert estimated_fee.overall_fee > 0


@pytest.mark.asyncio
async def test_get_code(contract_address, gateway_client):
    code = await gateway_client.get_code(contract_address=contract_address)

    assert code.abi is not None
    assert len(code.abi) != 0
    assert code.bytecode is not None
    assert len(code.bytecode) != 0


@pytest.mark.asyncio
async def test_get_code_invalid_address(gateway_client):
    with pytest.raises(
        ContractNotFoundError,
        match="^Client failed: No contract with address 123 found.$",
    ):
        await gateway_client.get_code(contract_address=123)

    with pytest.raises(
        ContractNotFoundError,
        match="^Client failed: No contract with address 123 found for block with block_number: latest.$",
    ):
        await gateway_client.get_code(contract_address=123, block_number="latest")


@pytest.mark.asyncio
async def test_get_contract_nonce(gateway_client):
    nonce = await gateway_client.get_contract_nonce(
        contract_address=0x1111,
        block_hash="latest",
    )
    assert nonce == 0


@pytest.mark.asyncio
async def test_get_transaction_status(invoke_transaction_hash, gateway_client):
    tx_status_resp = await gateway_client.get_transaction_status(
        invoke_transaction_hash
    )
    assert isinstance(tx_status_resp, TransactionStatusResponse)
    assert tx_status_resp.transaction_status == TransactionStatus.ACCEPTED_ON_L2
    assert isinstance(tx_status_resp.block_hash, int)


# pylint: disable=protected-access
@pytest.mark.parametrize(
    "net, net_address",
    (
        (TESTNET, "https://alpha4.starknet.io"),
        (TESTNET2, "https://alpha4-2.starknet.io"),
        (MAINNET, "https://alpha-mainnet.starknet.io"),
    ),
)
def test_creating_client_from_predefined_network(net, net_address):
    gateway_client = GatewayClient(net=net)

    assert gateway_client._feeder_gateway_client.url == f"{net_address}/feeder_gateway"
    assert gateway_client._gateway_client.url == f"{net_address}/gateway"


def test_creating_client_with_custom_net():
    custom_net = "custom.net"
    gateway_client = GatewayClient(net=custom_net)

    assert gateway_client._feeder_gateway_client.url == f"{custom_net}/feeder_gateway"
    assert gateway_client._gateway_client.url == f"{custom_net}/gateway"


def test_creating_client_with_custom_net_dict():
    custom_net = "custom.net"
    net = CustomGatewayUrls(
        feeder_gateway_url=f"{custom_net}/feeder_gateway",
        gateway_url=f"{custom_net}/gateway",
    )

    gateway_client = GatewayClient(net=net)

    assert gateway_client._feeder_gateway_client.url == net["feeder_gateway_url"]
    assert gateway_client._gateway_client.url == net["gateway_url"]


@pytest.mark.asyncio
async def test_get_storage_at_incorrect_address_gateway_client(gateway_client):
    storage = await gateway_client.get_storage_at(
        contract_address=0x1111,
        key=get_storage_var_address("balance"),
        block_hash="latest",
    )
    assert storage == 0


@pytest.mark.asyncio
async def test_get_l1_handler_transaction_without_nonce(gateway_client):
    with patch(
        "starknet_py.net.http_client.GatewayHttpClient.call", AsyncMock()
    ) as mocked_transaction_call:
        mocked_transaction_call.return_value = {
            "status": "ACCEPTED_ON_L1",
            "block_hash": "0x38ce7678420eaff5cd62597643ca515d0887579a8be69563067fe79a624592b",
            "block_number": 370459,
            "transaction_index": 9,
            "transaction": {
                "version": "0x0",
                "contract_address": "0x278f24c3e74cbf7a375ec099df306289beb0605a346277d200b791a7f811a19",
                "entry_point_selector": "0x2d757788a8d8d6f21d1cd40bce38a8222d70654214e96ff95d8086e684fbee5",
                "calldata": [
                    "0xd8beaa22894cd33f24075459cfba287a10a104e4",
                    "0x3f9c67ef1d31e24b386184b4ede63a869c4659de093ef437ee235cae4daf2be",
                    "0x3635c9adc5dea00000",
                    "0x0",
                    "0x7cb4539b69a2371f75d21160026b76a7a7c1cacb",
                ],
                "transaction_hash": "0x7e1ed66dbccf915857c6367fc641c24292c063e54a5dd55947c2d958d94e1a9",
                "type": "L1_HANDLER",
            },
        }

        transaction = await gateway_client.get_transaction(tx_hash=0x1)

        assert isinstance(transaction, L1HandlerTransaction)
        assert transaction.nonce is None


# Check if the `Deploy` transaction is fetched correctly
@pytest.mark.asyncio
async def test_get_deploy_tx():
    client = GatewayClient(net=TESTNET)
    deploy_tx = await client.get_transaction(
        tx_hash="0x068d6145cb99622cc930f9b26034c6f5127c348e8c21a5e232e36540a48622bb"
    )

    assert deploy_tx == DeployTransaction(
        hash=2963673878706802757881372249643497924351429288158219425664578299882910393019,
        signature=[],
        max_fee=0,
        version=0,
        contract_address=3201539328574232511583948975549924874632298555514040085947217389204344560301,
        constructor_calldata=[
            2977964825119970114006147768568360818918965859196023865674869683232138769290,
            1295919550572838631247819983596733806859788957403169325509326258146877103642,
            1,
            1755481054165712359795659576392952180676068046985196641715115837975005192835,
        ],
        class_hash=1390726910323976264396851446996494490757233897803493337751952271375342730526,
    )
