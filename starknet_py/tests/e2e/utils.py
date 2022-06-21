from __future__ import annotations
import os


from starknet_py.net import Client, KeyPair
from starknet_py.net.account.account_client import AccountClient
from starknet_py.net.models.chains import StarknetChainId


DEVNET_PORT = os.environ.get("DEVNET_PORT")
if not DEVNET_PORT:
    raise RuntimeError("DEVNET_PORT environment variable not provided!")

DEVNET_ADDRESS = f"http://localhost:{DEVNET_PORT}"

ACCOUNT_CLIENT_ADDRESS = (
    "0x7d2f37b75a5e779f7da01c22acee1b66c39e8ba470ee5448f05e1462afcedb4"
)
ACCOUNT_CLIENT_PRIVATE_KEY = "0xcd613e30d8f16adf91b7584a2265b1f5"


class DevnetClientFactory:
    def __init__(
        self,
        net: str = DEVNET_ADDRESS,
        chain: StarknetChainId = StarknetChainId.TESTNET,
    ):
        self.net = net
        self.chain = chain

    async def make_devnet_client(self) -> Client:
        client = await AccountClient.create_account(net=self.net, chain=self.chain)
        return client

    def make_devnet_client_from_predefined_account(self) -> AccountClient:
        key_pair = KeyPair.from_private_key(int(ACCOUNT_CLIENT_PRIVATE_KEY, 0))
        client = AccountClient(
            address=ACCOUNT_CLIENT_ADDRESS,
            key_pair=key_pair,
            net=self.net,
            chain=self.chain,
        )

        return client

    async def make_devnet_client_without_account(self) -> Client:
        return Client(net=self.net, chain=self.chain)
