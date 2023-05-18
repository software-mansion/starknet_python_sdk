import pytest

from starknet_py.cairo.felt import decode_shortstring, encode_shortstring
from starknet_py.contract import Contract
from starknet_py.tests.e2e.fixtures.constants import MAX_FEE
from starknet_py.tests.e2e.fixtures.contracts import deploy_v1_contract


@pytest.mark.asyncio
async def test_general_v1_interaction(account, v1_erc20_class_hash: int):
    calldata = {
        "name_": encode_shortstring("erc20_basic"),
        "symbol_": encode_shortstring("ERC20B"),
        "decimals_": 10,
        "initial_supply": 12345,
        "recipient": account.address,
    }
    erc20 = await deploy_v1_contract(
        account=account,
        contract_file_name="erc20",
        class_hash=v1_erc20_class_hash,
        calldata=calldata,
    )

    (name,) = await erc20.functions["get_name"].call()
    decoded_name = decode_shortstring(name).lstrip("\x00")
    (decimals,) = await erc20.functions["get_decimals"].call()
    (supply,) = await erc20.functions["get_total_supply"].call()
    (account_balance,) = await erc20.functions["balance_of"].call(
        account=account.address
    )

    transfer_amount = 10
    await (
        await erc20.functions["transfer"].invoke(
            recipient=0x11, amount=transfer_amount, max_fee=MAX_FEE
        )
    ).wait_for_acceptance()

    (after_transfer_balance,) = await erc20.functions["balance_of"].call(
        account=account.address
    )

    assert decoded_name == "erc20_basic"
    assert decimals == calldata["decimals_"]
    assert supply == calldata["initial_supply"]
    assert account_balance == calldata["initial_supply"]
    assert after_transfer_balance == calldata["initial_supply"] - transfer_amount


@pytest.mark.asyncio
async def test_serializing_struct(account, v1_token_bridge_class_hash: int):
    bridge = await deploy_v1_contract(
        account=account,
        contract_file_name="token_bridge",
        class_hash=v1_token_bridge_class_hash,
        calldata={"governor_address": account.address},
    )

    await (
        await bridge.functions["set_l1_bridge"].invoke(
            l1_bridge_address={"address": 0x11}, max_fee=MAX_FEE
        )
    ).wait_for_acceptance()


@pytest.mark.asyncio
async def test_serializing_option(account, v1_test_option_class_hash: int):
    test_option = await deploy_v1_contract(
        account=account,
        contract_file_name="test_option",
        class_hash=v1_test_option_class_hash,
    )

    (received_option,) = await test_option.functions["get_option_struct"].call()

    assert dict(received_option) == {
        "first_field": 1,
        "second_field": 2,
        "third_field": None,
        "fourth_field": 4,
    }

    option_struct = {
        "first_field": 1,
        "second_field": 2**128 + 1,
        "third_field": None,
        "fourth_field": 4,
    }

    (received_option,) = await test_option.functions[
        "receive_and_send_option_struct"
    ].call(option_struct=option_struct)

    assert dict(received_option) == option_struct

    (received_option,) = await test_option.functions["get_empty_option"].call()

    assert received_option is None


@pytest.mark.asyncio
async def test_serializing_enum(account, v1_test_enum_class_hash: int):
    test_enum = await deploy_v1_contract(
        account=account,
        contract_file_name="test_enum",
        class_hash=v1_test_enum_class_hash,
    )

    (received_enum,) = await test_enum.functions["get_enum"].call()

    assert received_enum.variant == "a"
    assert received_enum.value == 100

    (received_enum,) = await test_enum.functions["get_enum_without_value"].call()

    assert received_enum.variant == "c"
    assert received_enum.value is None

    variant_name = "b"
    value = 200
    (received_enum,) = await test_enum.functions["receive_and_send_enum"].call(
        my_enum={variant_name: value}
    )

    assert received_enum.variant == variant_name
    assert received_enum.value == value

    variant_name = "c"
    value = None
    (received_enum,) = await test_enum.functions["receive_and_send_enum"].call(
        my_enum={variant_name: value}
    )

    assert received_enum.variant == variant_name
    assert received_enum.value == value


@pytest.mark.asyncio
async def test_from_address_on_v1_contract(gateway_account, v1_erc20_class_hash: int):
    # TODO (#1023): replace with account after RPC 0.3.0
    calldata = {
        "name_": encode_shortstring("erc20_basic"),
        "symbol_": encode_shortstring("ERC20B"),
        "decimals_": 10,
        "initial_supply": 12345,
        "recipient": gateway_account.address,
    }
    erc20 = await deploy_v1_contract(
        account=gateway_account,
        contract_file_name="erc20",
        class_hash=v1_erc20_class_hash,
        calldata=calldata,
    )

    erc20_from_address = await Contract.from_address(
        erc20.address, provider=gateway_account
    )

    assert erc20_from_address.address == erc20.address
    assert erc20_from_address.account == erc20.account
    assert erc20_from_address.functions.keys() == erc20.functions.keys()
    assert erc20_from_address.data == erc20.data
