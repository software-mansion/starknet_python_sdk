import json

import pytest
from starkware.starknet.core.os.contract_class.class_hash import (
    compute_class_hash as sw_compute_class_hash,
)
from starkware.starknet.services.api.contract_class.contract_class import (
    ContractClass as SwContractClass,
)

from starknet_py.common import create_sierra_compiled_contract
from starknet_py.hash.sierra_class_hash import compute_sierra_class_hash
from starknet_py.tests.e2e.fixtures.constants import CONTRACTS_COMPILED_V1_DIR
from starknet_py.tests.e2e.fixtures.misc import read_contract


@pytest.mark.parametrize(
    "sierra_contract_class_source",
    [
        "account_compiled.json",
        "erc20_compiled.json",
        "hello_starknet_compiled.json",
        "minimal_contract_compiled.json",
        "test_contract_compiled.json",
        "token_bridge_compiled.json",
    ],
)
def test_compute_sierra_class_hash(sierra_contract_class_source):
    sierra_contract_class_str = read_contract(
        sierra_contract_class_source, directory=CONTRACTS_COMPILED_V1_DIR
    )
    sierra_contract_class_dict = json.loads(sierra_contract_class_str)
    sierra_contract_class_dict["abi"] = json.dumps(sierra_contract_class_dict["abi"])
    del sierra_contract_class_dict["sierra_program_debug_info"]

    sierra_contract_class = create_sierra_compiled_contract(sierra_contract_class_str)
    class_hash = compute_sierra_class_hash(sierra_contract_class)

    sw_contract_class = SwContractClass.load(sierra_contract_class_dict)
    sw_class_hash = sw_compute_class_hash(sw_contract_class)

    assert class_hash == sw_class_hash
