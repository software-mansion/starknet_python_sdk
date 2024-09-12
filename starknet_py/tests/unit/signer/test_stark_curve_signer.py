from unittest.mock import MagicMock, Mock

import pytest

from starknet_py.common import create_sierra_compiled_contract
from starknet_py.net.models import StarknetChainId
from starknet_py.net.models.transaction import DeclareV3, DeployAccountV3, InvokeV3
from starknet_py.net.signer.stark_curve_signer import KeyPair, StarkCurveSigner
from starknet_py.tests.e2e.fixtures.misc import load_contract

compiled_contract = load_contract("HelloStarknet")["sierra"]
sierra_contract_class = create_sierra_compiled_contract(compiled_contract)


@pytest.mark.parametrize(
    "transaction",
    [
        Mock(spec=InvokeV3, calculate_hash=MagicMock(return_value=12345678)),
        Mock(spec=DeployAccountV3, calculate_hash=MagicMock(return_value=12345678)),
        Mock(spec=DeclareV3, calculate_hash=MagicMock(return_value=12345678)),
    ],
)
def test_sign_transaction(transaction):
    signer = StarkCurveSigner(
        account_address=0x1,
        key_pair=KeyPair.from_private_key(0x1),
        chain_id=StarknetChainId.MAINNET,
    )

    signature = signer.sign_transaction(transaction)

    assert isinstance(signature, list)
    assert len(signature) == 2
    assert all(isinstance(i, int) for i in signature)
    assert all(i != 0 for i in signature)


def test_key_pair():
    key_pair = KeyPair(public_key="0x123", private_key="0x456")

    assert isinstance(key_pair.public_key, int)
    assert isinstance(key_pair.private_key, int)

    key_pair = KeyPair.from_private_key("0x789")

    assert isinstance(key_pair.public_key, int)
    assert isinstance(key_pair.private_key, int)
