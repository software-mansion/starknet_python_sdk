from enum import IntEnum
from typing import Optional

from starknet_py.common import int_from_bytes
from starknet_py.constants import FEE_CONTRACT_ADDRESS
from starknet_py.net.networks import (
    GOERLI,
    MAINNET,
    SEPOLIA_INTEGRATION,
    SEPOLIA_TESTNET,
    Network,
)


class StarknetChainId(IntEnum):
    """
    An enumeration representing Starknet chain IDs.
    """

    MAINNET = int_from_bytes(b"SN_MAIN")
    GOERLI = int_from_bytes(b"SN_GOERLI")
    SEPOLIA_TESTNET = int_from_bytes(b"SN_SEPOLIA")
    SEPOLIA_INTEGRATION = int_from_bytes(b"SN_INTEGRATION_SEPOLIA")


def chain_from_network(
    net: Network, chain: Optional[StarknetChainId] = None
) -> StarknetChainId:
    mapping = {
        MAINNET: StarknetChainId.MAINNET,
        GOERLI: StarknetChainId.GOERLI,
        SEPOLIA_TESTNET: StarknetChainId.SEPOLIA_TESTNET,
        SEPOLIA_INTEGRATION: StarknetChainId.SEPOLIA_INTEGRATION,
    }

    if isinstance(net, str) and net in mapping:
        return mapping[net]

    if not chain:
        raise ValueError("Chain is required when not using predefined networks.")

    return chain


def default_token_address_for_chain(chain_id: StarknetChainId) -> str:
    if chain_id not in [
        StarknetChainId.SEPOLIA_TESTNET,
        StarknetChainId.SEPOLIA_INTEGRATION,
        StarknetChainId.GOERLI,
        StarknetChainId.MAINNET,
    ]:
        raise ValueError(
            "Argument token_address must be specified when using a custom network."
        )

    return FEE_CONTRACT_ADDRESS
