from typing import Union

from starknet_py.constants import QUERY_VERSION_BASE


def _extract_tx_version(version: Union[int, str]):
    print("_extract_tx_version")
    print(version)
    print(version)
    if isinstance(version, str):
        version = int(version, 16)
    return version % QUERY_VERSION_BASE
