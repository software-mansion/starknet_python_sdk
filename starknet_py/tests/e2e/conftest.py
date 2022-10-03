# pylint: disable=redefined-outer-name

import asyncio
import json
import os
import socket
import subprocess
import sys
import time
from contextlib import closing
from pathlib import Path
from typing import Tuple, List

import pytest
import pytest_asyncio
from starkware.crypto.signature.signature import get_random_private_key
from starkware.starknet.definitions.general_config import StarknetGeneralConfig

from starknet_py.common import create_compiled_contract
from starknet_py.net import KeyPair, AccountClient
from starknet_py.net.client import Client
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.http_client import GatewayHttpClient
from starknet_py.net.models import StarknetChainId, AddressRepresentation
from starknet_py.contract import Contract
from starknet_py.net.models.typed_data import TypedData
from starknet_py.net.udc_deployer.deployer import Deployer
from starknet_py.transactions.deploy import make_deploy_tx
from starknet_py.utils.data_transformer.data_transformer import CairoSerializer

TESTNET_ACCOUNT_PRIVATE_KEY = (
    "0x5d6871223e9d2f6136f3913e8ccb6daae0b6b2a8452b39f92a1ddc5a76eed9a"
)
TESTNET_ACCOUNT_ADDRESS = (
    "0x7536539dbba2a49ab688a1c86332625f05f660a94908f362d29212e6071432d"
)

INTEGRATION_ACCOUNT_PRIVATE_KEY = (
    "0x5C09392256E68EA48445A9386668055418EAB5538ADBE4B12FD0FDC782C1A07"
)
INTEGRATION_ACCOUNT_ADDRESS = (
    "0x60D7C88541F969520E46D39EC7C9053451CFEDBC2EEB847B684981A22CD452E"
)

TESTNET_NEW_ACCOUNT_PRIVATE_KEY = (
    "0x39232a85ce81bf97f04f2bb96064719c7ddb551e02ef1e9991ebba9cda5c02c"
)
TESTNET_NEW_ACCOUNT_ADDRESS = (
    "0x75ce3f13b7a1aaa3d0d2c39bf3ca8d5430ee7570ffeab130daf0bedf2c2a41e"
)

INTEGRATION_NEW_ACCOUNT_PRIVATE_KEY = "0x1"

INTEGRATION_NEW_ACCOUNT_ADDRESS = (
    "0X126FAB6AE8ACA83E2DD00B92F94F3402397D527798E18DC28D76B7740638D23"
)

mock_dir = Path(os.path.dirname(__file__)) / "mock"
typed_data_dir = mock_dir / "typed_data"
contracts_dir = mock_dir / "contracts"


# This fixture was added to enable using async fixtures
@pytest.fixture(scope="module")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


def pytest_addoption(parser):
    parser.addoption(
        "--net",
        action="store",
        default="devnet",
        help="Network to run tests on: possible 'testnet', 'devnet', 'all'",
    )


def get_available_port() -> int:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(("", 0))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return sock.getsockname()[1]


def start_devnet():
    devnet_port = get_available_port()

    command = [
        "poetry",
        "run",
        "starknet-devnet",
        "--host",
        "localhost",
        "--port",
        str(devnet_port),
        "--accounts",  # deploys specified number of accounts
        str(1),
        "--seed",  # generates same accounts each time
        str(1),
    ]
    # pylint: disable=consider-using-with
    proc = subprocess.Popen(command)
    time.sleep(5)
    return devnet_port, proc


@pytest.fixture(scope="module")
def run_devnet() -> str:
    """
    Runs devnet instance once per module and returns it's address
    """
    devnet_port, proc = start_devnet()
    yield f"http://localhost:{devnet_port}"
    proc.kill()


@pytest.fixture(scope="module")
def network(pytestconfig, run_devnet: str) -> str:
    """
    Returns network address depending on the --net parameter
    """
    net = pytestconfig.getoption("--net")
    net_address = {
        "devnet": run_devnet,
        "testnet": "testnet",
        "integration": "https://external.integration.starknet.io",
    }

    return net_address[net]


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


@pytest.fixture(name="gateway_client", scope="module")
def create_gateway_client(network: str) -> GatewayClient:
    """
    Creates and returns GatewayClient
    """
    return GatewayClient(net=network)


@pytest.fixture(name="rpc_client", scope="module")
def create_rpc_client(run_devnet: str) -> FullNodeClient:
    """
    Creates and returns FullNodeClient
    """
    return FullNodeClient(node_url=run_devnet + "/rpc", net=run_devnet)


def create_account_client(
    address: AddressRepresentation,
    private_key: str,
    client: Client,
    supported_tx_version: int,
) -> AccountClient:
    key_pair = KeyPair.from_private_key(int(private_key, 0))
    return AccountClient(
        address=address,
        client=client,
        key_pair=key_pair,
        chain=StarknetChainId.TESTNET,
        supported_tx_version=supported_tx_version,
    )


async def devnet_account_details(
    network: str, gateway_client: GatewayClient
) -> Tuple[str, str]:
    """
    Creates an AccountClient (and when using devnet adds fee tokens to its balance)
    """
    devnet_account = await AccountClient.create_account(
        client=gateway_client, chain=StarknetChainId.TESTNET
    )

    http_client = GatewayHttpClient(network)
    await http_client.post(
        method_name="mint",
        payload={
            "address": hex(devnet_account.address),
            "amount": int(1e30),
        },
    )

    return hex(devnet_account.address), hex(devnet_account.signer.private_key)


@pytest_asyncio.fixture(scope="module")
async def address_and_private_key(
    pytestconfig, network: str, gateway_client: GatewayClient
) -> Tuple[str, str]:
    """
    Returns address and private key of an account, depending on the network
    """
    net = pytestconfig.getoption("--net")

    account_details = {
        "testnet": (TESTNET_ACCOUNT_ADDRESS, TESTNET_ACCOUNT_PRIVATE_KEY),
        "integration": (INTEGRATION_ACCOUNT_ADDRESS, INTEGRATION_ACCOUNT_PRIVATE_KEY),
    }

    if net == "devnet":
        return await devnet_account_details(network, gateway_client)
    return account_details[net]


@pytest.fixture(scope="module")
def gateway_account_client(
    address_and_private_key: Tuple[str, str], gateway_client: GatewayClient
) -> AccountClient:
    """
    Returns an AccountClient created with GatewayClient
    """
    address, private_key = address_and_private_key

    return create_account_client(
        address, private_key, gateway_client, supported_tx_version=0
    )


@pytest.fixture(scope="module")
def rpc_account_client(
    address_and_private_key: Tuple[str, str], rpc_client: FullNodeClient
) -> AccountClient:
    """
    Returns an AccountClient created with FullNodeClient
    """
    address, private_key = address_and_private_key

    return create_account_client(
        address, private_key, rpc_client, supported_tx_version=0
    )


async def new_devnet_account_details(
    network: str, gateway_client: GatewayClient
) -> Tuple[str, str]:
    """
    Deploys a new AccountClient and adds fee tokens to its balance (only on devnet)
    """
    private_key = get_random_private_key()

    key_pair = KeyPair.from_private_key(private_key)
    deploy_tx = make_deploy_tx(
        constructor_calldata=[key_pair.public_key],
        compiled_contract=(contracts_dir / "new_account_compiled.json").read_text(
            "utf-8"
        ),
    )

    result = await gateway_client.deploy(deploy_tx)
    await gateway_client.wait_for_tx(
        tx_hash=result.transaction_hash,
    )
    address = result.contract_address

    http_client = GatewayHttpClient(network)
    await http_client.post(
        method_name="mint",
        payload={
            "address": hex(address),
            "amount": int(1e30),
        },
    )

    return hex(address), hex(key_pair.private_key)


@pytest_asyncio.fixture(scope="module")
async def new_address_and_private_key(
    pytestconfig, network: str, gateway_client: GatewayClient
) -> Tuple[str, str]:
    """
    Returns address and private key of a new account, depending on the network
    """
    net = pytestconfig.getoption("--net")

    account_details = {
        "testnet": (TESTNET_NEW_ACCOUNT_ADDRESS, TESTNET_NEW_ACCOUNT_PRIVATE_KEY),
        "integration": (
            INTEGRATION_NEW_ACCOUNT_ADDRESS,
            INTEGRATION_NEW_ACCOUNT_PRIVATE_KEY,
        ),
    }

    if net == "devnet":
        return await new_devnet_account_details(network, gateway_client)
    return account_details[net]


@pytest.fixture(scope="module")
def new_gateway_account_client(
    new_address_and_private_key: Tuple[str, str], gateway_client: GatewayClient
) -> AccountClient:
    """
    Returns a new AccountClient created with GatewayClient
    """
    address, private_key = new_address_and_private_key

    return create_account_client(
        address, private_key, gateway_client, supported_tx_version=1
    )


def net_to_accounts() -> List[str]:
    accounts = [
        "gateway_account_client",
        "new_gateway_account_client",
        "rpc_account_client",
    ]
    if any(
        net in sys.argv
        for net in ["--net=integration", "--net=testnet", "testnet", "integration"]
    ):
        accounts.remove("rpc_account_client")

    return accounts


@pytest.fixture(
    scope="module",
    params=net_to_accounts(),
)
def account_client(request) -> AccountClient:
    """
    This parametrized fixture returns all AccountClients, one by one.
    Test using this fixture will be run three times, once per account.
    """
    return request.getfixturevalue(request.param)


@pytest.fixture(
    scope="module", params=["deploy_map_contract", "new_deploy_map_contract"]
)
def map_contract(request) -> Contract:
    """
    Returns account contracts using old and new account versions
    """
    return request.getfixturevalue(request.param)


@pytest.fixture(scope="module")
def map_source_code() -> str:
    """
    Returns source code of the map contract
    """
    return (contracts_dir / "map.cairo").read_text("utf-8")


@pytest.fixture(scope="module")
def erc20_source_code() -> str:
    """
    Returns source code of the erc20 contract
    """
    return (contracts_dir / "erc20.cairo").read_text("utf-8")


@pytest_asyncio.fixture(name="deploy_map_contract", scope="module")
async def deploy_map_contract(
    gateway_account_client: AccountClient, map_source_code: str
) -> Contract:
    """
    Deploys map contract and returns its instance
    """
    deployment_result = await Contract.deploy(
        client=gateway_account_client, compilation_source=map_source_code
    )
    deployment_result = await deployment_result.wait_for_acceptance()
    return deployment_result.deployed_contract


@pytest_asyncio.fixture(name="new_deploy_map_contract", scope="module")
async def new_deploy_map_contract(
    new_gateway_account_client: AccountClient, map_source_code: str
) -> Contract:
    """
    Deploys new map contract and returns its instance
    """
    deployment_result = await Contract.deploy(
        client=new_gateway_account_client, compilation_source=map_source_code
    )
    deployment_result = await deployment_result.wait_for_acceptance()
    return deployment_result.deployed_contract


@pytest_asyncio.fixture(name="erc20_contract", scope="module")
async def deploy_erc20_contract(
    gateway_account_client: AccountClient, erc20_source_code: str
) -> Contract:
    """
    Deploys erc20 contract and returns its instance
    """
    deployment_result = await Contract.deploy(
        client=gateway_account_client, compilation_source=erc20_source_code
    )
    deployment_result = await deployment_result.wait_for_acceptance()
    return deployment_result.deployed_contract


@pytest.fixture(
    name="compiled_proxy",
    params=["argent_proxy_compiled.json", "oz_proxy_compiled.json"],
)
def compiled_proxy(request) -> str:
    """
    Returns source code of compiled proxy contract
    """
    return (contracts_dir / request.param).read_text("utf-8")


@pytest.fixture(
    name="typed_data",
    params=[
        "typed_data_example.json",
        "typed_data_felt_array_example.json",
        "typed_data_long_string_example.json",
        "typed_data_struct_array_example.json",
    ],
)
def typed_data(request) -> TypedData:
    """
    Returns TypedData dictionary example
    """
    file_name = getattr(request, "param")
    file_path = typed_data_dir / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        typed_data = json.load(file)

    return typed_data


@pytest_asyncio.fixture(name="cairo_serializer", scope="module")
async def cairo_serializer(gateway_account_client: AccountClient) -> CairoSerializer:
    """
    Returns CairoSerializer for "simple_storage_with_event.cairo"
    """
    client = gateway_account_client
    contract_content = (contracts_dir / "simple_storage_with_event.cairo").read_text(
        "utf-8"
    )

    deployment_result = await Contract.deploy(
        client, compilation_source=contract_content
    )
    await deployment_result.wait_for_acceptance()
    contract = deployment_result.deployed_contract

    return CairoSerializer(identifier_manager=contract.data.identifier_manager)


@pytest_asyncio.fixture(scope="module")
async def deployer_address(gateway_client: AccountClient) -> int:
    """
    Returns an address of the UDC
    """
    deploy_tx = make_deploy_tx(
        compilation_source=(mock_dir / "contracts/universal_deployer.cairo").read_text(
            "utf-8"
        )
    )
    res = await gateway_client.deploy(deploy_tx)
    return res.contract_address


@pytest_asyncio.fixture(scope="module")
async def map_class_hash(
    new_gateway_account_client: AccountClient, map_source_code: str
) -> int:
    """
    Returns class_hash of the map.cairo
    """
    declare = await new_gateway_account_client.sign_declare_transaction(
        compilation_source=map_source_code,
        max_fee=int(1e16),
    )
    res = await new_gateway_account_client.declare(declare)
    await new_gateway_account_client.wait_for_tx(res.transaction_hash)
    return res.class_hash


constructor_with_arguments_source = (
    contracts_dir / "constructor_with_arguments.cairo"
).read_text("utf-8")


@pytest.fixture(scope="module")
def constructor_with_arguments_abi() -> List:
    """
    Returns an abi of the constructor_with_arguments.cairo
    """
    return (
        create_compiled_contract(compilation_source=constructor_with_arguments_source)
    ).abi


@pytest_asyncio.fixture(scope="module")
async def constructor_with_arguments_class_hash(
    new_gateway_account_client: AccountClient,
) -> int:
    """
    Returns a class_hash of the constructor_with_arguments.cairo
    """
    return (
        await new_gateway_account_client.declare(
            await new_gateway_account_client.sign_declare_transaction(
                compilation_source=constructor_with_arguments_source, max_fee=int(1e16)
            )
        )
    ).class_hash


@pytest_asyncio.fixture(scope="module")
async def put_with_event_transaction_hash(
    new_gateway_account_client: AccountClient, deployer_address: int
) -> int:
    """
    Returns hash of the transaction with an event
    """
    declare_tx = await new_gateway_account_client.sign_declare_transaction(
        compilation_source=(
            contracts_dir / "simple_storage_with_event.cairo"
        ).read_text("utf-8"),
        max_fee=int(1e16),
    )
    resp = await new_gateway_account_client.declare(declare_tx)
    await new_gateway_account_client.wait_for_tx(resp.transaction_hash)

    deployer = Deployer(account=new_gateway_account_client, address=deployer_address)
    deploy_tx = await deployer.make_deployment(
        class_hash=resp.class_hash
    ).prepare_transaction(max_fee=int(1e16))

    resp = await new_gateway_account_client.send_transaction(deploy_tx)
    await new_gateway_account_client.wait_for_tx(
        resp.transaction_hash, wait_for_accept=True
    )

    address = await deployer.get_deployed_contract_address(
        transaction_hash=resp.transaction_hash
    )
    abi = create_compiled_contract(
        compilation_source=(
            contracts_dir / "simple_storage_with_event.cairo"
        ).read_text("utf-8")
    ).abi

    contract = Contract(address=address, abi=abi, client=new_gateway_account_client)

    resp = await contract.functions["put"].invoke(key=10, value=20, max_fee=int(1e16))
    await resp.wait_for_acceptance()

    return resp.hash


@pytest_asyncio.fixture(name="default_gateway_gas_price", scope="module")
def default_gateway_gas_price() -> int:
    """
    Returns the default min gas price from the StarknetGeneralConfig.
    Useful for asserting that the gas price appears in the block response from
    the GatewayClient.
    """
    return StarknetGeneralConfig().min_gas_price
