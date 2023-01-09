# pylint: disable=line-too-long
# fmt: off

from starknet_py.common import int_from_bytes

# Address came from starkware-libs/starknet-addresses repository: https://github.com/starkware-libs/starknet-addresses
FEE_CONTRACT_ADDRESS = "0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7"
DEFAULT_DEPLOYER_ADDRESS = "0x041a78e741e5aF2fEc34B695679bC6891742439f7AFB8484Ecd7766661aD02BF"

RPC_INVALID_MESSAGE_SELECTOR_ERROR = 21
RPC_CLASS_HASH_NOT_FOUND_ERROR = 28

DEFAULT_ENTRY_POINT_NAME = "__default__"
DEFAULT_L1_ENTRY_POINT_NAME = "__l1_default__"
DEFAULT_ENTRY_POINT_SELECTOR = 0
MASK_250 = 2**250 - 1

# MAX_STORAGE_ITEM_SIZE and ADDR_BOUND must be consistent with the corresponding constant in
# starkware/starknet/common/storage.cairo.
MAX_STORAGE_ITEM_SIZE = 256
ADDR_BOUND = 2**251 - MAX_STORAGE_ITEM_SIZE

FIELD_PRIME = 0x800000000000011000000000000000000000000000000000000000000000001
EC_ORDER = 0x800000000000010FFFFFFFFFFFFFFFFB781126DCAE7B2321E66A241ADC64D2F

# From cairo-lang
CONTRACT_ADDRESS_PREFIX = int_from_bytes(b"STARKNET_CONTRACT_ADDRESS")
L2_ADDRESS_UPPER_BOUND = 2**251 - 256
