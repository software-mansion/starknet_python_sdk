from abc import ABC, abstractmethod
from typing import Optional

from starkware.starknet.public.abi import (
    get_selector_from_name,
    get_storage_var_address,
)

from starknet_py.net.client import Client
from starknet_py.net.client_models import Call
from starknet_py.net.models import Address


# fmt: off
# docs-proxy-check: start
class ProxyCheck(ABC):
    @abstractmethod
    async def implementation_address(
        self, address: Address, client: Client
    ) -> Optional[int]:
        """
        :return: Implementation address of contract being proxied by proxy contract at `address`
            given as an argument or None if implementation does not exist.
        """

    @abstractmethod
    async def implementation_hash(
        self, address: Address, client: Client
    ) -> Optional[int]:
        """
        :return: Implementation class hash of contract being proxied by proxy contract at `address`
            given as an argument or None if implementation does not exist.
        """
# docs-proxy-check: end
# fmt: on


class ArgentProxyCheck(ProxyCheck):
    async def implementation_address(
        self, address: Address, client: Client
    ) -> Optional[int]:
        return await self.get_implementation(address, client)

    async def implementation_hash(
        self, address: Address, client: Client
    ) -> Optional[int]:
        return await self.get_implementation(address, client)

    @staticmethod
    async def get_implementation(address: Address, client: Client) -> Optional[int]:
        call = Call(
            to_addr=address,
            selector=get_selector_from_name("get_implementation"),
            calldata=[],
        )
        (implementation,) = await client.call_contract(call=call)
        return implementation


class OpenZeppelinProxyCheck(ProxyCheck):
    async def implementation_address(
        self, address: Address, client: Client
    ) -> Optional[int]:
        return await self._get_storage_at_or_none(
            address=address, client=client, key="Proxy_implementation_address"
        )

    async def implementation_hash(
        self, address: Address, client: Client
    ) -> Optional[int]:
        return await self._get_storage_at_or_none(
            address=address, client=client, key="Proxy_implementation_hash"
        )

    @staticmethod
    async def _get_storage_at_or_none(
        address: Address, client: Client, key: str
    ) -> Optional[int]:
        result = await client.get_storage_at(
            contract_address=address,
            key=get_storage_var_address(key),
            block_hash="latest",
        )
        return result or None
