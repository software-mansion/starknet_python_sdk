from typing import Optional

from starknet_py.common import int_from_hex
from starknet_py.net.networks import Network, MAINNET, TESTNET


def deployer_address_from_network(
    net: Network, deployer_address: Optional[int] = None
) -> int:
    # FIXME: change to real addresses once deployed
    mapping = {
        MAINNET: 123,
        TESTNET: 456,
    }

    if isinstance(net, str) and net in mapping:
        return mapping[net]

    if not deployer_address:
        raise ValueError(
            "deployer_address is required when not using predefined networks."
        )

    return int_from_hex(deployer_address)
