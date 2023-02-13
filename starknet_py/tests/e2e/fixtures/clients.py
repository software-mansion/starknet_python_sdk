import sys
from typing import List

import pytest

from starknet_py.net.client import Client
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.models import StarknetChainId
from starknet_py.net.networks import Network


@pytest.fixture(name="gateway_client", scope="package")
def create_gateway_client(network: str) -> GatewayClient:
    """
    Creates and returns GatewayClient.
    """
    return GatewayClient(net=Network(address=network, chain_id=StarknetChainId.TESTNET))


@pytest.fixture(name="full_node_client", scope="package")
def create_full_node_client(network: str) -> FullNodeClient:
    """
    Creates and returns FullNodeClient.
    """
    return FullNodeClient(
        net=Network(address=network + "/rpc", chain_id=StarknetChainId.TESTNET)
    )


def net_to_clients() -> List[str]:
    """
    Return client fixture names based on network in sys.argv.
    """
    clients = ["gateway_client"]
    nets = ["--net=integration", "--net=testnet", "testnet", "integration"]

    if set(nets).isdisjoint(sys.argv):
        clients.append("full_node_client")
    return clients


@pytest.fixture(
    scope="package",
    params=net_to_clients(),
)
def client(request) -> Client:
    """
    Returns Client instances.
    """
    return request.getfixturevalue(request.param)
