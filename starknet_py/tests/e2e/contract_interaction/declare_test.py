import pytest

from starknet_py.contract import Contract
from starknet_py.net.client_models import ResourceBounds, ResourceBoundsMapping
from starknet_py.tests.e2e.fixtures.constants import MAX_FEE, MAX_RESOURCE_BOUNDS_L1
from starknet_py.tests.e2e.fixtures.misc import load_contract


@pytest.mark.asyncio
async def test_throws_when_cairo1_without_compiled_contract_casm_and_class_hash(
    account,
):
    error_message = (
        "For Cairo 1.0 contracts, either the 'compiled_class_hash' or the 'compiled_contract_casm' "
        "argument must be provided."
    )
    compiled_contract = load_contract("Map")["sierra"]

    with pytest.raises(ValueError, match=error_message):
        await Contract.declare_v2(
            account, compiled_contract=compiled_contract, max_fee=MAX_FEE
        )

    with pytest.raises(ValueError, match=error_message):
        resource_bounds = ResourceBoundsMapping(
            l1_gas=MAX_RESOURCE_BOUNDS_L1,
            l2_gas=ResourceBounds.init_with_zeros(),
        )
        await Contract.declare_v3(
            account,
            compiled_contract=compiled_contract,
            resource_bounds=resource_bounds,
        )
