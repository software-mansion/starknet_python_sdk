import datetime

import pytest

from starknet_py.constants import ANY_CALLER, OutsideExecutionInterfaceID
from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.account.account import BaseAccount
from starknet_py.net.client_models import (
    Call,
    OutsideExecutionTimeBounds,
    ResourceBounds,
)
from starknet_py.tests.e2e.fixtures.constants import MAX_FEE
from starknet_py.transaction_errors import TransactionRevertedError


@pytest.mark.asyncio
async def test_argent_account_outside_execution_compatibility(
    argent_account: BaseAccount,
    argent_account_v040: BaseAccount,
):
    result = await argent_account.supports_interface(OutsideExecutionInterfaceID.V1)
    assert result is True
    result = await argent_account.supports_interface(OutsideExecutionInterfaceID.V2)
    assert result is False

    result = await argent_account_v040.supports_interface(
        OutsideExecutionInterfaceID.V1
    )
    assert result is True
    result = await argent_account_v040.supports_interface(
        OutsideExecutionInterfaceID.V2
    )
    assert result is True


@pytest.mark.asyncio
async def test_account_outside_execution_any_caller(
    argent_account_v040: BaseAccount,
    account: BaseAccount,
    map_contract,
):
    assert any(
        [
            await argent_account_v040.supports_interface(
                OutsideExecutionInterfaceID.V1
            ),
            await argent_account_v040.supports_interface(
                OutsideExecutionInterfaceID.V2
            ),
        ]
    )

    put_call = Call(
        to_addr=map_contract.address,
        selector=get_selector_from_name("put"),
        calldata=[20, 20],
    )

    call = await argent_account_v040.sign_outside_execution_call(
        calls=[
            put_call,
        ],
        execution_time_bounds=OutsideExecutionTimeBounds(
            execute_after=datetime.datetime.now() - datetime.timedelta(hours=1),
            execute_before=datetime.datetime.now() + datetime.timedelta(hours=1),
        ),
        caller=ANY_CALLER,
    )

    tx = await account.execute_v3(
        calls=[call],
        l1_resource_bounds=ResourceBounds(
            max_amount=int(1e5), max_price_per_unit=int(1e13)
        ),
    )
    await account.client.wait_for_tx(tx.transaction_hash)


@pytest.mark.asyncio
async def test_account_outside_execution_for_invalid_caller(
    argent_account_v040: BaseAccount,
    account: BaseAccount,
    map_contract,
):
    assert any(
        [
            await argent_account_v040.supports_interface(
                OutsideExecutionInterfaceID.V1
            ),
            await argent_account_v040.supports_interface(
                OutsideExecutionInterfaceID.V2
            ),
        ]
    )

    random_address = 0x1234567890123456789012345678901234567890

    put_call = Call(
        to_addr=map_contract.address,
        selector=get_selector_from_name("put"),
        calldata=[20, 20],
    )

    call = await argent_account_v040.sign_outside_execution_call(
        calls=[
            put_call,
        ],
        execution_time_bounds=OutsideExecutionTimeBounds(
            execute_after=datetime.datetime.now() - datetime.timedelta(hours=1),
            execute_before=datetime.datetime.now() + datetime.timedelta(hours=1),
        ),
        caller=random_address,
    )

    tx = await account.execute_v3(
        calls=[call],
        l1_resource_bounds=ResourceBounds(
            max_amount=int(1e5), max_price_per_unit=int(1e13)
        ),
    )

    with pytest.raises(TransactionRevertedError) as err:
        await argent_account_v040.client.wait_for_tx(tx.transaction_hash)

    assert "argent/invalid-caller" in err.value.message


@pytest.mark.asyncio
async def test_account_outside_execution_for_impossible_time_bounds(
    argent_account_v040: BaseAccount,
    account: BaseAccount,
    map_contract,
):

    assert any(
        [
            await argent_account_v040.supports_interface(
                OutsideExecutionInterfaceID.V1
            ),
            await argent_account_v040.supports_interface(
                OutsideExecutionInterfaceID.V2
            ),
        ]
    )

    put_call = Call(
        to_addr=map_contract.address,
        selector=get_selector_from_name("put"),
        calldata=[20, 20],
    )

    call = await argent_account_v040.sign_outside_execution_call(
        calls=[put_call],
        execution_time_bounds=OutsideExecutionTimeBounds(
            execute_after=datetime.datetime.now() - datetime.timedelta(days=10),
            execute_before=datetime.datetime.now() - datetime.timedelta(days=9),
        ),
        caller=ANY_CALLER,
    )

    tx = await account.execute_v1(calls=[call], max_fee=MAX_FEE)

    with pytest.raises(TransactionRevertedError) as err:
        await argent_account_v040.client.wait_for_tx(tx.transaction_hash)

    assert "argent/invalid-timestamp" in err.value.message


@pytest.mark.asyncio
async def test_account_outside_execution_by_itself_is_impossible(
    argent_account_v040: BaseAccount,
    map_contract,
):

    assert any(
        [
            await argent_account_v040.supports_interface(
                OutsideExecutionInterfaceID.V1
            ),
            await argent_account_v040.supports_interface(
                OutsideExecutionInterfaceID.V2
            ),
        ]
    )

    put_call = Call(
        to_addr=map_contract.address,
        selector=get_selector_from_name("put"),
        calldata=[20, 20],
    )

    call = await argent_account_v040.sign_outside_execution_call(
        calls=[put_call],
        execution_time_bounds=OutsideExecutionTimeBounds(
            execute_after=datetime.datetime.now() - datetime.timedelta(days=10),
            execute_before=datetime.datetime.now() - datetime.timedelta(days=9),
        ),
        caller=ANY_CALLER,
    )

    tx = await argent_account_v040.execute_v1(calls=[call], max_fee=MAX_FEE)

    with pytest.raises(TransactionRevertedError) as err:
        await argent_account_v040.client.wait_for_tx(tx.transaction_hash)

    assert "ReentrancyGuard: reentrant call" in err.value.message
