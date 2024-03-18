# pylint: disable=redefined-outer-name

import json
import sys
from enum import Enum
from pathlib import Path
from typing import Optional

import pytest

from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models.typed_data import TypedData
from starknet_py.tests.e2e.fixtures.constants import (
    CONTRACTS_COMPILED_V0_DIR,
    CONTRACTS_COMPILED_V1_DIR,
    CONTRACTS_COMPILED_V2_DIR,
    CONTRACTS_V1_ARTIFACTS,
    CONTRACTS_V1_COMPILED,
    CONTRACTS_V2_ARTIFACTS,
    CONTRACTS_V2_COMPILED,
    TYPED_DATA_DIR,
)


def pytest_addoption(parser):
    parser.addoption(
        "--net",
        action="store",
        default="devnet",
        help="Network to run tests on: possible 'testnet', 'devnet', 'all'",
    )
    parser.addoption(
        "--contract_dir",
        action="store",
        default="",
        help="Contract directory: possible 'v1', 'v2'",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--net") == "all":
        return

    run_testnet = config.getoption("--net") == "testnet"
    run_devnet = config.getoption("--net") == "devnet"
    for item in items:
        runs_on_testnet = "run_on_testnet" in item.keywords
        runs_on_devnet = "run_on_devnet" in item.keywords
        should_not_run = (runs_on_devnet and not run_devnet) or (
            runs_on_testnet and not run_testnet
        )
        if should_not_run:
            item.add_marker(pytest.mark.skip())


@pytest.fixture(scope="package")
def network(pytestconfig, run_devnet: str) -> str:
    """
    Returns network address depending on the --net parameter.
    """
    net = pytestconfig.getoption("--net")
    net_address = {
        "devnet": run_devnet,
        "testnet": "testnet",
        "integration": "https://external.integration.starknet.io",
    }

    return net_address[net]


@pytest.fixture(
    params=[
        "typed_data_example.json",
        "typed_data_felt_array_example.json",
        "typed_data_long_string_example.json",
        "typed_data_struct_array_example.json",
    ],
)
def typed_data(request) -> TypedData:
    """
    Returns TypedData dictionary example.
    """
    file_name = getattr(request, "param")
    file_path = TYPED_DATA_DIR / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        typed_data = json.load(file)

    return typed_data


@pytest.fixture(name="get_tx_receipt_path", scope="package")
def get_tx_receipt_full_node_client():
    return f"{FullNodeClient.__module__}.FullNodeClient.get_transaction_receipt"


@pytest.fixture(name="get_tx_status_path", scope="package")
def get_tx_status_full_node_client():
    return f"{FullNodeClient.__module__}.FullNodeClient.get_transaction_status"


class ContractVersion(Enum):
    V1 = "V1"
    V2 = "V2"


class UnkonwnArtifacts(BaseException):
    pass


def load_contract(contract_name: str, version: Optional[ContractVersion] = None):
    if version is None:
        if "--contract_dir=v1" in sys.argv:
            version = ContractVersion.V1
        if "--contract_dir=v2" in sys.argv:
            version = ContractVersion.V2

    artifacts_path = CONTRACTS_V2_ARTIFACTS
    directory = CONTRACTS_V2_COMPILED

    if version == ContractVersion.V1:
        artifacts_path = CONTRACTS_V1_ARTIFACTS
        directory = CONTRACTS_V1_COMPILED

    loaded_artifcats = json.loads((artifacts_path).read_text("utf-8"))

    for item in loaded_artifcats["contracts"]:
        if item["contract_name"] == contract_name:
            artifacts = item["artifacts"]
            break

    if not isinstance(artifacts, dict):
        raise UnkonwnArtifacts(
            f"Artifacts for contract {contract_name} haven't be founded"
        )

    sierra = (directory / artifacts["sierra"]).read_text("utf-8")
    casm = (directory / artifacts["casm"]).read_text("utf-8")

    return {"casm": casm, "sierra": sierra}


def read_contract(file_name: str, *, directory: Optional[Path] = None) -> str:
    """
    Return contents of file_name from directory.
    """
    if directory is None:
        directory = CONTRACTS_COMPILED_V0_DIR
        if "--contract_dir=v1" in sys.argv:
            directory = CONTRACTS_COMPILED_V1_DIR
        if "--contract_dir=v2" in sys.argv:
            directory = CONTRACTS_COMPILED_V2_DIR

    return (directory / file_name).read_text("utf-8")
