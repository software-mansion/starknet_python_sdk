import pytest

from starknet_py.net.models import Invoke


@pytest.mark.asyncio
async def test_create_invoke_from_contract(map_contract, account):
    contract = map_contract
    max_fee = int(1e20)

    # docs: start
    from starknet_py.net.client_models import Call

    # Prepare a call through Contract
    call = contract.functions["put"].prepare(key=20, value=30)
    assert issubclass(type(call), Call)

    # Crate an Invoke transaction from call
    invoke_transaction = await account.sign_invoke_transaction(call, max_fee=max_fee)
    # docs: end

    assert isinstance(invoke_transaction, Invoke)
