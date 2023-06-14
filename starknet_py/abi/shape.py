from typing import List, Literal, Union

from typing_extensions import TypedDict, NotRequired

STRUCT_ENTRY = "struct"
FUNCTION_ENTRY = "function"
CONSTRUCTOR_ENTRY = "constructor"
L1_HANDLER_ENTRY = "l1_handler"
EVENT_ENTRY = "event"


class TypedMemberDict(TypedDict):
    name: str
    type: str


class StructMemberDict(TypedMemberDict):
    offset: NotRequired[int]  # should be optional? :2601 in rpc spec


class StructDict(TypedDict):
    type: Literal["struct"]
    name: str
    size: int
    members: List[StructMemberDict]


class FunctionBaseDict(TypedDict):
    name: str
    inputs: List[TypedMemberDict]
    outputs: List[TypedMemberDict]
    stateMutability: NotRequired[Literal["view"]]  # :2693 in rpc spec


class FunctionDict(FunctionBaseDict):
    type: Literal["function"]


class ConstructorDict(FunctionBaseDict):
    type: Literal["constructor"]


class L1HandlerDict(FunctionBaseDict):
    type: Literal["l1_handler"]


class EventDict(TypedDict):
    name: str
    type: Literal["event"]
    data: List[TypedMemberDict]
    keys: List[TypedMemberDict]


AbiDictEntry = Union[
    StructDict, FunctionDict, ConstructorDict, L1HandlerDict, EventDict
]
AbiDictList = List[AbiDictEntry]
