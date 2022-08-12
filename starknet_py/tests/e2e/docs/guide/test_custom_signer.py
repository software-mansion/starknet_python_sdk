from typing import List

import pytest


@pytest.mark.asyncio
async def test_custom_signer():
    # pylint: disable=import-outside-toplevel, duplicate-code, unused-variable

    # add to docs: start
    from starknet_py.net import AccountClient
    from starknet_py.net.signer import BaseSigner
    from starknet_py.net.gateway_client import GatewayClient
    from starknet_py.net.models import Transaction
    from starknet_py.net.models import StarknetChainId

    # Create a custom signer class implementing BaseSigner interface
    class CustomSigner(BaseSigner):
        @property
        def public_key(self) -> int:
            return 0x123

        def sign_transaction(self, transaction: Transaction) -> List[int]:
            return [0x0, 0x1]

    # Create an AccountClient instance with the signer you've implemented
    custom_signer = CustomSigner()
    client = GatewayClient("testnet")
    account_client = AccountClient(
        client=client,
        address=0x1111,
        signer=custom_signer,
        chain=StarknetChainId.TESTNET
    )
    # Now you can use AccountClient as you'd always do
    # add to docs: end
