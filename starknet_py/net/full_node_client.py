import re
import warnings
from typing import Dict, List, Optional, Union, cast

import aiohttp
from marshmallow import EXCLUDE

from starknet_py.net.client import Client
from starknet_py.net.client_errors import ClientError
from starknet_py.net.client_models import (
    BlockStateUpdate,
    BlockTransactionTraces,
    Call,
    ContractClass,
    DeclareTransactionResponse,
    DeployAccountTransactionResponse,
    EstimatedFee,
    Events,
    Hash,
    SentTransactionResponse,
    StarknetBlock,
    Tag,
    Transaction,
    TransactionReceipt,
    TransactionType,
)
from starknet_py.net.http_client import RpcHttpClient
from starknet_py.net.models.transaction import (
    AccountTransaction,
    Declare,
    DeclareSchema,
    DeployAccount,
    Invoke,
)
from starknet_py.net.networks import Network
from starknet_py.net.schemas.rpc import (
    BlockStateUpdateSchema,
    ContractClassSchema,
    DeclareTransactionResponseSchema,
    DeployAccountTransactionResponseSchema,
    EstimatedFeeSchema,
    EventsSchema,
    PendingTransactionsSchema,
    SentTransactionSchema,
    StarknetBlockSchema,
    TransactionReceiptSchema,
    TypesOfTransactionsSchema,
)
from starknet_py.transaction_exceptions import TransactionNotReceivedError
from starknet_py.utils.sync import add_sync_methods


@add_sync_methods
class FullNodeClient(Client):
    def __init__(
        self,
        node_url: str,
        net: Optional[Network] = None,
        session: Optional[aiohttp.ClientSession] = None,
    ):
        """
        Client for interacting with Starknet json-rpc interface.

        :param node_url: Url of the node providing rpc interface
        :param net: Starknet network identifier
        :param session: Aiohttp session to be used for request. If not provided, client will create a session for
                        every request. When using a custom session, user is responsible for closing it manually.
        """
        self.url = node_url
        self._client = RpcHttpClient(url=node_url, session=session)

        if net is not None:
            warnings.warn("Parameter net is deprecated.", category=DeprecationWarning)
        self._net = net

    @property
    def net(self) -> Optional[Network]:
        warnings.warn(
            "Property net is deprecated in the FullNodeClient.",
            category=DeprecationWarning,
        )
        return self._net

    async def get_block(
        self,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> StarknetBlock:
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )

        res = await self._client.call(
            method_name="getBlockWithTxs",
            params={"block_id": block_identifier},
        )
        return cast(StarknetBlock, StarknetBlockSchema().load(res, unknown=EXCLUDE))

    async def get_block_traces(
        self,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> BlockTransactionTraces:
        raise NotImplementedError()

    async def get_events(
        self,
        from_block_number: Optional[Union[int, Tag]] = None,
        from_block_hash: Optional[Union[Hash, Tag]] = None,
        to_block_number: Optional[Union[int, Tag]] = None,
        to_block_hash: Optional[Union[Hash, Tag]] = None,
        contract_address: Optional[Hash] = None,
        keys: Optional[List[Hash]] = None,
    ) -> Events:
        # pylint: disable=too-many-arguments
        params = {
            "chunk_size": 1024,
            "from_block": get_block_identifier(from_block_hash, from_block_number),
            "to_block": get_block_identifier(to_block_hash, to_block_number),
        }

        if contract_address is not None:
            params["address"] = _to_rpc_felt(contract_address)
        if keys:
            params["keys"] = list(map(_to_rpc_felt, keys))

        res = await self._client.call(
            method_name="getEvents",
            params={"filter": params},
        )
        ret = cast(Events, EventsSchema().load(res, unknown=EXCLUDE))
        con_token = res.get("continuation_token")
        while con_token:
            params["continuation_token"] = con_token
            res = await self._client.call(
                method_name="getEvents",
                params={"filter": params},
            )
            new_events = cast(Events, EventsSchema().load(res, unknown=EXCLUDE))
            ret.events.extend(new_events.events)
            con_token = res.get("continuation_token")
        return ret

    async def get_state_update(
        self,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> BlockStateUpdate:
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )

        res = await self._client.call(
            method_name="getStateUpdate",
            params={"block_id": block_identifier},
        )
        return cast(
            BlockStateUpdate, BlockStateUpdateSchema().load(res, unknown=EXCLUDE)
        )

    async def get_storage_at(
        self,
        contract_address: Hash,
        key: int,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> int:
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )

        res = await self._client.call(
            method_name="getStorageAt",
            params={
                "contract_address": _to_rpc_felt(contract_address),
                "key": _to_storage_key(key),
                "block_id": block_identifier,
            },
        )
        res = cast(str, res)
        return int(res, 16)

    async def get_transaction(
        self,
        tx_hash: Hash,
    ) -> Transaction:
        try:
            res = await self._client.call(
                method_name="getTransactionByHash",
                params={"transaction_hash": _to_rpc_felt(tx_hash)},
            )
        except ClientError as ex:
            raise TransactionNotReceivedError() from ex
        return cast(Transaction, TypesOfTransactionsSchema().load(res, unknown=EXCLUDE))

    async def get_transaction_receipt(self, tx_hash: Hash) -> TransactionReceipt:
        res = await self._client.call(
            method_name="getTransactionReceipt",
            params={"transaction_hash": _to_rpc_felt(tx_hash)},
        )
        return cast(
            TransactionReceipt, TransactionReceiptSchema().load(res, unknown=EXCLUDE)
        )

    async def estimate_fee(
        self,
        tx: AccountTransaction,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> EstimatedFee:
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )

        res = await self._client.call(
            method_name="estimateFee",
            params={
                "request": _create_broadcasted_txn(transaction=tx),
                "block_id": block_identifier,
            },
        )

        return cast(EstimatedFee, EstimatedFeeSchema().load(res, unknown=EXCLUDE))

    async def call_contract(
        self,
        call: Call,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> List[int]:
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )
        res = await self._client.call(
            method_name="call",
            params={
                "request": {
                    "contract_address": _to_rpc_felt(call.to_addr),
                    "entry_point_selector": _to_rpc_felt(call.selector),
                    "calldata": [_to_rpc_felt(i1) for i1 in call.calldata],
                },
                "block_id": block_identifier,
            },
        )
        return [int(i, 16) for i in res]

    async def send_transaction(self, transaction: Invoke) -> SentTransactionResponse:
        params = _create_broadcasted_txn(transaction=transaction)

        res = await self._client.call(
            method_name="addInvokeTransaction",
            params={"invoke_transaction": params},
        )

        return cast(
            SentTransactionResponse, SentTransactionSchema().load(res, unknown=EXCLUDE)
        )

    async def deploy_account(
        self, transaction: DeployAccount
    ) -> DeployAccountTransactionResponse:
        params = _create_broadcasted_txn(transaction=transaction)

        res = await self._client.call(
            method_name="addDeployAccountTransaction",
            params={"deploy_account_transaction": params},
        )

        return cast(
            DeployAccountTransactionResponse,
            DeployAccountTransactionResponseSchema().load(res, unknown=EXCLUDE),
        )

    async def declare(self, transaction: Declare) -> DeclareTransactionResponse:
        params = _create_broadcasted_txn(transaction=transaction)

        res = await self._client.call(
            method_name="addDeclareTransaction",
            params={"declare_transaction": {**params}},
        )

        return cast(
            DeclareTransactionResponse,
            DeclareTransactionResponseSchema().load(res, unknown=EXCLUDE),
        )

    async def get_class_hash_at(
        self,
        contract_address: Hash,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> int:
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )
        res = await self._client.call(
            method_name="getClassHashAt",
            params={
                "contract_address": _to_rpc_felt(contract_address),
                "block_id": block_identifier,
            },
        )
        res = cast(str, res)
        return int(res, 16)

    async def get_class_by_hash(
        self,
        class_hash: Hash,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> ContractClass:
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )

        res = await self._client.call(
            method_name="getClass",
            params={
                "class_hash": _to_rpc_felt(class_hash),
                "block_id": block_identifier,
            },
        )
        return cast(ContractClass, ContractClassSchema().load(res, unknown=EXCLUDE))

    # Only RPC methods

    async def get_transaction_by_block_id(
        self,
        index: int,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> Transaction:
        """
        Get the details of transaction in block identified by block_hash and transaction index.

        :param index: Index of the transaction
        :param block_hash: Hash of the block
        :param block_number: Block's number or literals `"pending"` or `"latest"`
        :return: Transaction object
        """
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )

        res = await self._client.call(
            method_name="getTransactionByBlockIdAndIndex",
            params={
                "block_id": block_identifier,
                "index": index,
            },
        )
        return cast(Transaction, TypesOfTransactionsSchema().load(res, unknown=EXCLUDE))

    async def get_block_transaction_count(
        self,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> int:
        """
        Get the number of transactions in a block given a block id

        :param block_hash: Block's hash or literals `"pending"` or `"latest"`
        :param block_number: Block's number or literals `"pending"` or `"latest"`
        :return: Number of transactions in the designated block
        """
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )

        res = await self._client.call(
            method_name="getBlockTransactionCount",
            params={"block_id": block_identifier},
        )
        res = cast(int, res)
        return res

    async def get_class_at(
        self,
        contract_address: Hash,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> ContractClass:
        """
        Get the contract class definition in the given block at the given address

        :param contract_address: The address of the contract whose class definition will be returned
        :param block_hash: Block's hash or literals `"pending"` or `"latest"`
        :param block_number: Block's number or literals `"pending"` or `"latest"`
        :return: Contract declared to Starknet
        """
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )

        res = await self._client.call(
            method_name="getClassAt",
            params={
                "block_id": block_identifier,
                "contract_address": _to_rpc_felt(contract_address),
            },
        )

        return cast(ContractClass, ContractClassSchema().load(res, unknown=EXCLUDE))

    async def get_pending_transactions(self) -> List[Transaction]:
        """
        Returns the transactions in the transaction pool, recognized by sequencer

        :returns: List of transactions
        """
        res = await self._client.call(method_name="pendingTransactions", params={})
        res = {"pending_transactions": res}

        return cast(
            List[Transaction], PendingTransactionsSchema().load(res, unknown=EXCLUDE)
        )

    async def get_contract_nonce(
        self,
        contract_address: Hash,
        block_hash: Optional[Union[Hash, Tag]] = None,
        block_number: Optional[Union[int, Tag]] = None,
    ) -> int:
        block_identifier = get_block_identifier(
            block_hash=block_hash, block_number=block_number
        )
        res = await self._client.call(
            method_name="getNonce",
            params={
                "contract_address": _to_rpc_felt(contract_address),
                "block_id": block_identifier,
            },
        )
        res = cast(str, res)
        return int(res, 16)


def get_block_identifier(
    block_hash: Optional[Union[Hash, Tag]] = None,
    block_number: Optional[Union[int, Tag]] = None,
) -> Union[Dict, Tag, int, Hash, None]:
    if block_hash is not None and block_number is not None:
        raise ValueError(
            "Arguments block_hash and block_number are mutually exclusive."
        )

    if block_hash in ("latest", "pending") or block_number in ("latest", "pending"):
        return block_hash or block_number

    if block_hash is not None:
        ret = {"block_hash": _to_rpc_felt(block_hash)}
        return ret

    if block_number is not None:
        ret = {"block_number": block_number}
        return ret

    return "pending"


def _create_broadcasted_txn(transaction: AccountTransaction) -> dict:
    txn_map = {
        TransactionType.DECLARE: _create_broadcasted_declare_properties,
        TransactionType.INVOKE: _create_broadcasted_invoke_properties,
        TransactionType.DEPLOY_ACCOUNT: _create_broadcasted_deploy_account_properties,
    }

    common_properties = _create_broadcasted_txn_common_properties(transaction)
    transaction_specific_properties = txn_map[transaction.type](transaction)

    return {
        **common_properties,
        **transaction_specific_properties,
    }


def _create_broadcasted_declare_properties(transaction: Declare) -> dict:
    contract_class = cast(Dict, DeclareSchema().dump(obj=transaction))["contract_class"]
    declare_properties = {
        "contract_class": {
            "program": contract_class["program"],
            "entry_points_by_type": contract_class["entry_points_by_type"],
            "abi": contract_class["abi"],
        },
        "sender_address": _to_rpc_felt(transaction.sender_address),
    }
    return declare_properties


def _create_broadcasted_invoke_properties(transaction: Invoke) -> dict:
    invoke_properties = {
        "sender_address": _to_rpc_felt(transaction.sender_address),
        "calldata": [_to_rpc_felt(data) for data in transaction.calldata],
    }
    return invoke_properties


def _create_broadcasted_deploy_account_properties(transaction: DeployAccount) -> dict:
    deploy_account_txn_properties = {
        "contract_address_salt": _to_rpc_felt(transaction.contract_address_salt),
        "constructor_calldata": [
            _to_rpc_felt(data) for data in transaction.constructor_calldata
        ],
        "class_hash": _to_rpc_felt(transaction.class_hash),
    }
    return deploy_account_txn_properties


def _create_broadcasted_txn_common_properties(transaction: AccountTransaction) -> dict:
    broadcasted_txn_common_properties = {
        "type": transaction.type.name,
        "max_fee": _to_rpc_felt(transaction.max_fee),
        "version": _to_rpc_felt(transaction.version),
        "signature": [_to_rpc_felt(sig) for sig in transaction.signature],
        "nonce": _to_rpc_felt(transaction.nonce),
    }
    return broadcasted_txn_common_properties


def _to_storage_key(key: int) -> str:
    """
    Convert a value to RPC storage key matching a ``^0x0[0-7]{1}[a-fA-F0-9]{0,62}$`` pattern.

    :param key: The key to convert.
    :return: RPC storage key representation of the key.
    """

    hashed_key = hex(key)[2:]

    if hashed_key[0] not in ("0", "1", "2", "3", "4", "5", "6", "7"):
        hashed_key = "0" + hashed_key

    hashed_key = "0x0" + hashed_key

    if not re.match(r"^0x0[0-7]{1}[a-fA-F0-9]{0,62}$", hashed_key):
        raise ValueError(f"Value {key} cannot be represented as RPC storage key.")

    return hashed_key


def _to_rpc_felt(value: Hash) -> str:
    """
    Convert the value to RPC felt matching a ``^0x0[a-fA-F0-9]{1,63}$`` pattern.\

    :param value: The value to convert.
    :return: RPC felt representation of the value.
    """
    if isinstance(value, str):
        value = int(value, 16)

    if value == 0:
        return "0x00"
    return "0x0" + hex(value).lstrip("0x")
