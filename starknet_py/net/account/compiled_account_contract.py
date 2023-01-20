# pylint: disable=too-many-lines
COMPILED_ACCOUNT_CONTRACT = r"""{
    "abi": [
        {
            "members": [
                {
                    "name": "to",
                    "offset": 0,
                    "type": "felt"
                },
                {
                    "name": "selector",
                    "offset": 1,
                    "type": "felt"
                },
                {
                    "name": "data_offset",
                    "offset": 2,
                    "type": "felt"
                },
                {
                    "name": "data_len",
                    "offset": 3,
                    "type": "felt"
                }
            ],
            "name": "CallArray",
            "size": 4,
            "type": "struct"
        },
        {
            "inputs": [],
            "name": "assert_only_self",
            "outputs": [],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "get_public_key",
            "outputs": [
                {
                    "name": "res",
                    "type": "felt"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "name": "new_public_key",
                    "type": "felt"
                }
            ],
            "name": "set_public_key",
            "outputs": [],
            "type": "function"
        },
        {
            "inputs": [
                {
                    "name": "_public_key",
                    "type": "felt"
                }
            ],
            "name": "constructor",
            "outputs": [],
            "type": "constructor"
        },
        {
            "inputs": [
                {
                    "name": "hash",
                    "type": "felt"
                },
                {
                    "name": "signature_len",
                    "type": "felt"
                },
                {
                    "name": "signature",
                    "type": "felt*"
                }
            ],
            "name": "is_valid_signature",
            "outputs": [],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "name": "class_hash",
                    "type": "felt"
                }
            ],
            "name": "__validate_declare__",
            "outputs": [],
            "type": "function"
        },
        {
            "inputs": [
                {
                    "name": "call_array_len",
                    "type": "felt"
                },
                {
                    "name": "call_array",
                    "type": "CallArray*"
                },
                {
                    "name": "calldata_len",
                    "type": "felt"
                },
                {
                    "name": "calldata",
                    "type": "felt*"
                }
            ],
            "name": "__validate__",
            "outputs": [],
            "type": "function"
        },
        {
            "inputs": [
                {
                    "name": "call_array_len",
                    "type": "felt"
                },
                {
                    "name": "call_array",
                    "type": "CallArray*"
                },
                {
                    "name": "calldata_len",
                    "type": "felt"
                },
                {
                    "name": "calldata",
                    "type": "felt*"
                }
            ],
            "name": "__execute__",
            "outputs": [
                {
                    "name": "retdata_size",
                    "type": "felt"
                },
                {
                    "name": "retdata",
                    "type": "felt*"
                }
            ],
            "type": "function"
        },
        {
            "inputs": [
                {
                    "name": "class_hash",
                    "type": "felt"
                },
                {
                    "name": "contract_address_salt",
                    "type": "felt"
                },
                {
                    "name": "constructor_calldata_len",
                    "type": "felt"
                },
                {
                    "name": "constructor_calldata",
                    "type": "felt*"
                },
                {
                    "name": "deploy_from_zero",
                    "type": "felt"
                }
            ],
            "name": "deploy_contract",
            "outputs": [
                {
                    "name": "contract_address",
                    "type": "felt"
                }
            ],
            "type": "function"
        }
    ],
    "entry_points_by_type": {
        "CONSTRUCTOR": [
            {
                "offset": "0x121",
                "selector": "0x28ffe4ff0f226a9107253e17a904099aa4f63a02a5621de0576e5aa71bc5194"
            }
        ],
        "EXTERNAL": [
            {
                "offset": "0x1ed",
                "selector": "0x15d40a3d6ca2ac30f4031e42be28da9b056fef9bb7357ac5e85627ee876e5ad"
            },
            {
                "offset": "0x193",
                "selector": "0x162da33a4585851fe8d3af3c2a9c60b557814e221e0d4f30ff0b2189d9c7775"
            },
            {
                "offset": "0xee",
                "selector": "0x1a35984e05126dbecb7c3bb9929e7dd9106d460c59b1633739a5c733a5fb13b"
            },
            {
                "offset": "0x221",
                "selector": "0x2730079d734ee55315f4f141eaed376bddd8c2133523d223a344c5604e0f7f8"
            },
            {
                "offset": "0x147",
                "selector": "0x28420862938116cb3bbdbedee07451ccc54d4e9412dbef71142ad1980a30941"
            },
            {
                "offset": "0x172",
                "selector": "0x289da278a8dc833409cabfdad1581e8e7d40e42dcaed693fa4008dcdb4963b3"
            },
            {
                "offset": "0xd1",
                "selector": "0x2de154d8a89be65c1724e962dc4c65637c05532a6c2825d0a7b7d774169dbba"
            },
            {
                "offset": "0x107",
                "selector": "0x2e3e21ff5952b2531241e37999d9c4c8b3034cccc89a202a6bf019bdf5294f9"
            }
        ],
        "L1_HANDLER": []
    },
    "program": {
        "attributes": [
            {
                "accessible_scopes": [
                    "__main__",
                    "__main__",
                    "__main__.is_valid_signature"
                ],
                "end_pc": 315,
                "flow_tracking_data": {
                    "ap_tracking": {
                        "group": 31,
                        "offset": 23
                    },
                    "reference_ids": {
                        "__main__.is_valid_signature._public_key": 220,
                        "__main__.is_valid_signature.ecdsa_ptr": 216,
                        "__main__.is_valid_signature.hash": 210,
                        "__main__.is_valid_signature.pedersen_ptr": 218,
                        "__main__.is_valid_signature.range_check_ptr": 219,
                        "__main__.is_valid_signature.signature": 212,
                        "__main__.is_valid_signature.signature_len": 211,
                        "__main__.is_valid_signature.syscall_ptr": 217
                    }
                },
                "name": "error_message",
                "start_pc": 313,
                "value": "INVALID_SIGNATURE_LENGTH"
            },
            {
                "accessible_scopes": [
                    "__main__",
                    "__main__",
                    "__main__.__execute__"
                ],
                "end_pc": 457,
                "flow_tracking_data": {
                    "ap_tracking": {
                        "group": 37,
                        "offset": 22
                    },
                    "reference_ids": {
                        "__main__.__execute__.__fp__": 331,
                        "__main__.__execute__.call_array": 324,
                        "__main__.__execute__.call_array_len": 323,
                        "__main__.__execute__.calldata": 326,
                        "__main__.__execute__.calldata_len": 325,
                        "__main__.__execute__.caller": 336,
                        "__main__.__execute__.ecdsa_ptr": 330,
                        "__main__.__execute__.pedersen_ptr": 328,
                        "__main__.__execute__.range_check_ptr": 329,
                        "__main__.__execute__.syscall_ptr": 335,
                        "__main__.__execute__.tx_info": 334
                    }
                },
                "name": "error_message",
                "start_pc": 455,
                "value": "Invalid caller. This function cannot be called from another contract."
            },
            {
                "accessible_scopes": [
                    "__main__",
                    "__main__",
                    "__main__.__execute__"
                ],
                "end_pc": 462,
                "flow_tracking_data": {
                    "ap_tracking": {
                        "group": 37,
                        "offset": 22
                    },
                    "reference_ids": {
                        "__main__.__execute__.__fp__": 331,
                        "__main__.__execute__.call_array": 324,
                        "__main__.__execute__.call_array_len": 323,
                        "__main__.__execute__.calldata": 326,
                        "__main__.__execute__.calldata_len": 325,
                        "__main__.__execute__.caller": 336,
                        "__main__.__execute__.ecdsa_ptr": 330,
                        "__main__.__execute__.pedersen_ptr": 328,
                        "__main__.__execute__.range_check_ptr": 329,
                        "__main__.__execute__.syscall_ptr": 335,
                        "__main__.__execute__.tx_info": 334
                    }
                },
                "name": "error_message",
                "start_pc": 457,
                "value": "Invalid transaction version. This account contract does not support transaction version 0."
            }
        ],
        "builtins": [
            "pedersen",
            "range_check",
            "ecdsa"
        ],
        "compiler_version": "0.10.0",
        "data": [
            "0x40780017fff7fff",
            "0x1",
            "0x208b7fff7fff7ffe",
            "0x400380007ffb7ffc",
            "0x400380017ffb7ffd",
            "0x482680017ffb8000",
            "0x3",
            "0x480280027ffb8000",
            "0x208b7fff7fff7ffe",
            "0x20780017fff7ffd",
            "0x3",
            "0x208b7fff7fff7ffe",
            "0x480a7ffb7fff8000",
            "0x480a7ffc7fff8000",
            "0x480080007fff8000",
            "0x400080007ffd7fff",
            "0x482480017ffd8001",
            "0x1",
            "0x482480017ffd8001",
            "0x1",
            "0xa0680017fff7ffe",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffffb",
            "0x402a7ffc7ffd7fff",
            "0x208b7fff7fff7ffe",
            "0x208b7fff7fff7ffe",
            "0x48297ffd80007ffc",
            "0x20680017fff7fff",
            "0x4",
            "0x402780017ffc7ffc",
            "0x1",
            "0x208b7fff7fff7ffe",
            "0x480680017fff8000",
            "0x43616c6c436f6e7472616374",
            "0x400280007ff97fff",
            "0x400380017ff97ffa",
            "0x400380027ff97ffb",
            "0x400380037ff97ffc",
            "0x400380047ff97ffd",
            "0x482680017ff98000",
            "0x7",
            "0x480280057ff98000",
            "0x480280067ff98000",
            "0x208b7fff7fff7ffe",
            "0x480680017fff8000",
            "0x4465706c6f79",
            "0x400280007ff87fff",
            "0x400380017ff87ff9",
            "0x400380027ff87ffa",
            "0x400380037ff87ffb",
            "0x400380047ff87ffc",
            "0x400380057ff87ffd",
            "0x482680017ff88000",
            "0x9",
            "0x480280067ff88000",
            "0x208b7fff7fff7ffe",
            "0x480680017fff8000",
            "0x47657443616c6c657241646472657373",
            "0x400280007ffd7fff",
            "0x482680017ffd8000",
            "0x2",
            "0x480280017ffd8000",
            "0x208b7fff7fff7ffe",
            "0x480680017fff8000",
            "0x476574436f6e747261637441646472657373",
            "0x400280007ffd7fff",
            "0x482680017ffd8000",
            "0x2",
            "0x480280017ffd8000",
            "0x208b7fff7fff7ffe",
            "0x480680017fff8000",
            "0x53746f7261676552656164",
            "0x400280007ffc7fff",
            "0x400380017ffc7ffd",
            "0x482680017ffc8000",
            "0x3",
            "0x480280027ffc8000",
            "0x208b7fff7fff7ffe",
            "0x480680017fff8000",
            "0x53746f726167655772697465",
            "0x400280007ffb7fff",
            "0x400380017ffb7ffc",
            "0x400380027ffb7ffd",
            "0x482680017ffb8000",
            "0x3",
            "0x208b7fff7fff7ffe",
            "0x480680017fff8000",
            "0x4765745478496e666f",
            "0x400280007ffd7fff",
            "0x482680017ffd8000",
            "0x2",
            "0x480280017ffd8000",
            "0x208b7fff7fff7ffe",
            "0x40780017fff7fff",
            "0x2",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffbb",
            "0x400780017fff8000",
            "0x0",
            "0x400780017fff8001",
            "0x0",
            "0x48127ffe7fff8000",
            "0x208b7fff7fff7ffe",
            "0x40780017fff7fff",
            "0x2",
            "0x480a7ffa7fff8000",
            "0x480a7ffc7fff8000",
            "0x480a7ffd7fff8000",
            "0x480280007ffb8000",
            "0x1104800180018000",
            "0x20",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffab",
            "0x40137ffd7fff8000",
            "0x480280017ffb8000",
            "0x40297ffd7fff8001",
            "0x48127ffb7fff8000",
            "0x48127ffc7fff8000",
            "0x208b7fff7fff7ffe",
            "0x40780017fff7fff",
            "0x2",
            "0x480a7ffb7fff8000",
            "0x480280007ffc8000",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffff89",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffff9c",
            "0x40137ffd7fff8000",
            "0x480280017ffc8000",
            "0x402580017fff8001",
            "0x1",
            "0x48127ffb7fff8000",
            "0x48127ffc7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ffc7fff8000",
            "0x480280007ffd8000",
            "0x480280017ffd8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffff7b",
            "0x208b7fff7fff7ffe",
            "0x20780017fff7ffc",
            "0x5",
            "0x480a7ffa7fff8000",
            "0x480a7ffd7fff8000",
            "0x208b7fff7fff7ffe",
            "0x40780017fff7fff",
            "0x1",
            "0x482680017ffc8000",
            "0x800000000000011000000000000000000000000000000000000000000000000",
            "0x40337fff7ffb8000",
            "0x480a7ffb7fff8000",
            "0x480a7ffa7fff8000",
            "0x480a7ffd7fff8000",
            "0x48317ffd80008000",
            "0x400080007ffd7ffe",
            "0x480080007ffc8000",
            "0x400080017ffc7fff",
            "0x482480017ffb8000",
            "0x1",
            "0x482480017ffb8000",
            "0x3",
            "0x480080027ffa8000",
            "0x20680017fff7ffb",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffff8",
            "0x208b7fff7fff7ffe",
            "0x400380017ff97ffa",
            "0x400380007ff97ffb",
            "0x482680017ff98000",
            "0x2",
            "0x208b7fff7fff7ffe",
            "0x480a7ffc7fff8000",
            "0x480a7ffd7fff8000",
            "0x480680017fff8000",
            "0x3b28019ccfdbd30ffc65951d94bb85c9e2b8434111a000b5afd533ce65f57a4",
            "0x208b7fff7fff7ffe",
            "0x480a7ffc7fff8000",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffffa",
            "0x480a7ffb7fff8000",
            "0x48127ffe7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffff91",
            "0x48127ffe7fff8000",
            "0x48127ff57fff8000",
            "0x48127ff57fff8000",
            "0x48127ffc7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ffb7fff8000",
            "0x480a7ffc7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffed",
            "0x480a7ffa7fff8000",
            "0x48127ffe7fff8000",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffff8b",
            "0x48127ff67fff8000",
            "0x48127ff67fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffff76",
            "0x48127ffe7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffff6c",
            "0x40127fff7fff7ff9",
            "0x48127ffe7fff8000",
            "0x208b7fff7fff7ffe",
            "0x402b7ffd7ffc7ffd",
            "0x480280007ffb8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffff6",
            "0x40780017fff7fff",
            "0x1",
            "0x48127ffe7fff8000",
            "0x480280017ffb8000",
            "0x480280027ffb8000",
            "0x480280037ffb8000",
            "0x480680017fff8000",
            "0x0",
            "0x48127ffa7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ffb7fff8000",
            "0x480a7ffc7fff8000",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffce",
            "0x208b7fff7fff7ffe",
            "0x40780017fff7fff",
            "0x1",
            "0x4003800080007ffc",
            "0x4826800180008000",
            "0x1",
            "0x480a7ffd7fff8000",
            "0x4828800080007ffe",
            "0x480a80007fff8000",
            "0x208b7fff7fff7ffe",
            "0x402b7ffd7ffc7ffd",
            "0x480280007ffb8000",
            "0x480280017ffb8000",
            "0x480280027ffb8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffee",
            "0x48127ffe7fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffff1",
            "0x48127ff47fff8000",
            "0x48127ff47fff8000",
            "0x48127ffb7fff8000",
            "0x480280037ffb8000",
            "0x48127ffa7fff8000",
            "0x48127ffa7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ffa7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffca",
            "0x480a7ffb7fff8000",
            "0x480a7ffc7fff8000",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffb9",
            "0x208b7fff7fff7ffe",
            "0x482680017ffd8000",
            "0x1",
            "0x402a7ffd7ffc7fff",
            "0x480280007ffb8000",
            "0x480280017ffb8000",
            "0x480280027ffb8000",
            "0x480280007ffd8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffff1",
            "0x40780017fff7fff",
            "0x1",
            "0x48127ffc7fff8000",
            "0x48127ffc7fff8000",
            "0x48127ffc7fff8000",
            "0x480280037ffb8000",
            "0x480680017fff8000",
            "0x0",
            "0x48127ffa7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ffa7fff8000",
            "0x480a7ffb7fff8000",
            "0x480a7ffc7fff8000",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffff9f",
            "0x208b7fff7fff7ffe",
            "0x482680017ffd8000",
            "0x1",
            "0x402a7ffd7ffc7fff",
            "0x480280007ffb8000",
            "0x480280017ffb8000",
            "0x480280027ffb8000",
            "0x480280007ffd8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffff3",
            "0x40780017fff7fff",
            "0x1",
            "0x48127ffc7fff8000",
            "0x48127ffc7fff8000",
            "0x48127ffc7fff8000",
            "0x480280037ffb8000",
            "0x480680017fff8000",
            "0x0",
            "0x48127ffa7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ff77fff8000",
            "0x480a7ff87fff8000",
            "0x480a7ff97fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffff79",
            "0x400780017fff7ffc",
            "0x2",
            "0x480a7ffa7fff8000",
            "0x480a7ffb7fff8000",
            "0x48127ffd7fff8000",
            "0x480280007ffd8000",
            "0x480280017ffd8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffff66",
            "0x48127ff47fff8000",
            "0x48127ff47fff8000",
            "0x48127ff47fff8000",
            "0x48127ffc7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480280027ffb8000",
            "0x480280017ffd8000",
            "0x400080007ffe7fff",
            "0x482680017ffd8000",
            "0x2",
            "0x480280017ffd8000",
            "0x48307fff7ffe8000",
            "0x402a7ffd7ffc7fff",
            "0x480280027ffb8000",
            "0x480280007ffb8000",
            "0x480280017ffb8000",
            "0x482480017ffd8000",
            "0x1",
            "0x480280037ffb8000",
            "0x480280007ffd8000",
            "0x480280017ffd8000",
            "0x482680017ffd8000",
            "0x2",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffdc",
            "0x40780017fff7fff",
            "0x1",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x480680017fff8000",
            "0x0",
            "0x48127ffa7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ff97fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffef0",
            "0x48127ffe7fff8000",
            "0x480a7ffa7fff8000",
            "0x480a7ffb7fff8000",
            "0x480a7ffc7fff8000",
            "0x480080057ffb8000",
            "0x480080037ffa8000",
            "0x480080047ff98000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffc6",
            "0x208b7fff7fff7ffe",
            "0x482680017ffd8000",
            "0x1",
            "0x402a7ffd7ffc7fff",
            "0x480280007ffb8000",
            "0x480280017ffb8000",
            "0x480280027ffb8000",
            "0x480280037ffb8000",
            "0x480280007ffd8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffec",
            "0x40780017fff7fff",
            "0x1",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x480680017fff8000",
            "0x0",
            "0x48127ffa7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ff67fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffecf",
            "0x48127ffe7fff8000",
            "0x480a7ff77fff8000",
            "0x480a7ff87fff8000",
            "0x480a7ff97fff8000",
            "0x480080057ffb8000",
            "0x480080037ffa8000",
            "0x480080047ff98000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffa5",
            "0x208b7fff7fff7ffe",
            "0x480280027ffb8000",
            "0x480280007ffd8000",
            "0x400080007ffe7fff",
            "0x482680017ffd8000",
            "0x1",
            "0x480280007ffd8000",
            "0x484480017fff8000",
            "0x4",
            "0x48307fff7ffd8000",
            "0x480280027ffb8000",
            "0x480080007ffe8000",
            "0x400080017ffe7fff",
            "0x482480017ffd8000",
            "0x1",
            "0x480080007ffc8000",
            "0x48307fff7ffe8000",
            "0x402a7ffd7ffc7fff",
            "0x480280027ffb8000",
            "0x480280007ffb8000",
            "0x480280017ffb8000",
            "0x482480017ffd8000",
            "0x2",
            "0x480280037ffb8000",
            "0x480280007ffd8000",
            "0x482680017ffd8000",
            "0x1",
            "0x480080007ff38000",
            "0x482480017ff28000",
            "0x1",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffd7",
            "0x40780017fff7fff",
            "0x1",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x480680017fff8000",
            "0x0",
            "0x48127ffa7fff8000",
            "0x208b7fff7fff7ffe",
            "0x40780017fff7fff",
            "0x8",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffe5b",
            "0x480a7ff67fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffe95",
            "0x40137fff7fff8000",
            "0x48127ffe7fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffe73",
            "0x400680017fff7fff",
            "0x0",
            "0x4802800080008000",
            "0x480680017fff8000",
            "0x0",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffe4e",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffe33",
            "0x40137fff7fff8001",
            "0x48127ff67fff8000",
            "0x480a7ffa7fff8000",
            "0x480a7ffb7fff8000",
            "0x480a7ffd7fff8000",
            "0x480a80017fff8000",
            "0x1104800180018000",
            "0x8d",
            "0x4003800180008002",
            "0x400b7ffa7fff8003",
            "0x400b80017fff8004",
            "0x4003800280008005",
            "0x4003800080008006",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffe24",
            "0x40137fff7fff8007",
            "0x48127ffc7fff8000",
            "0x480a80037fff8000",
            "0x480a80047fff8000",
            "0x480a80077fff8000",
            "0x1104800180018000",
            "0x5d",
            "0x48127ffe7fff8000",
            "0x480a7ff77fff8000",
            "0x480a7ff87fff8000",
            "0x480a7ff97fff8000",
            "0x48127ffb7fff8000",
            "0x480a80077fff8000",
            "0x208b7fff7fff7ffe",
            "0x480280027ffb8000",
            "0x480280007ffd8000",
            "0x400080007ffe7fff",
            "0x482680017ffd8000",
            "0x1",
            "0x480280007ffd8000",
            "0x484480017fff8000",
            "0x4",
            "0x48307fff7ffd8000",
            "0x480280027ffb8000",
            "0x480080007ffe8000",
            "0x400080017ffe7fff",
            "0x482480017ffd8000",
            "0x1",
            "0x480080007ffc8000",
            "0x48307fff7ffe8000",
            "0x402a7ffd7ffc7fff",
            "0x480280027ffb8000",
            "0x480280007ffb8000",
            "0x480280017ffb8000",
            "0x482480017ffd8000",
            "0x2",
            "0x480280037ffb8000",
            "0x480280007ffd8000",
            "0x482680017ffd8000",
            "0x1",
            "0x480080007ff38000",
            "0x482480017ff28000",
            "0x1",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffb3",
            "0x208b7fff7fff7ffe",
            "0x480a7ff87fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffebb",
            "0x480a7ff97fff8000",
            "0x480a7ffa7fff8000",
            "0x480a7ffb7fff8000",
            "0x480a7ffc7fff8000",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffe17",
            "0x208b7fff7fff7ffe",
            "0x40780017fff7fff",
            "0x1",
            "0x4003800080007ffc",
            "0x4826800180008000",
            "0x1",
            "0x480a7ffd7fff8000",
            "0x4828800080007ffe",
            "0x480a80007fff8000",
            "0x208b7fff7fff7ffe",
            "0x480280027ffb8000",
            "0x480280027ffd8000",
            "0x400080007ffe7fff",
            "0x482680017ffd8000",
            "0x3",
            "0x480280027ffd8000",
            "0x48307fff7ffe8000",
            "0x482480017fff8000",
            "0x1",
            "0x402a7ffd7ffc7fff",
            "0x480280007ffb8000",
            "0x480280007ffd8000",
            "0x480280017ffd8000",
            "0x480280027ffd8000",
            "0x482680017ffd8000",
            "0x3",
            "0x480080007ff98000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffdc",
            "0x480280027ffb8000",
            "0x48127ffe7fff8000",
            "0x482480017ffe8000",
            "0x1",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffe1",
            "0x48127ff47fff8000",
            "0x480280017ffb8000",
            "0x48127ffb7fff8000",
            "0x480280037ffb8000",
            "0x48127ffa7fff8000",
            "0x48127ffa7fff8000",
            "0x208b7fff7fff7ffe",
            "0x40780017fff7fff",
            "0x3",
            "0x20780017fff7ffb",
            "0x6",
            "0x480a7ffa7fff8000",
            "0x480680017fff8000",
            "0x0",
            "0x208b7fff7fff7ffe",
            "0x480a7ffa7fff8000",
            "0x480280007ffc8000",
            "0x480280017ffc8000",
            "0x480280027ffc8000",
            "0x480280037ffc8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffdd2",
            "0x40137ffe7fff8000",
            "0x40137fff7fff8001",
            "0x40137ffd7fff8002",
            "0x480a7ffd7fff8000",
            "0x480a80017fff8000",
            "0x480a80007fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffdb4",
            "0x480a80027fff8000",
            "0x482680017ffb8000",
            "0x800000000000011000000000000000000000000000000000000000000000000",
            "0x482680017ffc8000",
            "0x4",
            "0x482a80007ffd8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffe4",
            "0x48127ffe7fff8000",
            "0x482880007ffe8000",
            "0x208b7fff7fff7ffe",
            "0x20780017fff7ffa",
            "0x4",
            "0x480a7ff97fff8000",
            "0x208b7fff7fff7ffe",
            "0x480280007ffb8000",
            "0x400280007ffd7fff",
            "0x480280017ffb8000",
            "0x400280017ffd7fff",
            "0x480280037ffb8000",
            "0x400280027ffd7fff",
            "0x480280027ffb8000",
            "0x48327fff7ffc8000",
            "0x400280037ffd7fff",
            "0x480a7ff97fff8000",
            "0x482680017ffa8000",
            "0x800000000000011000000000000000000000000000000000000000000000000",
            "0x482680017ffb8000",
            "0x4",
            "0x480a7ffc7fff8000",
            "0x482680017ffd8000",
            "0x4",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffec",
            "0x208b7fff7fff7ffe"
        ],
        "debug_info": null,
        "hints": {
            "0": [
                {
                    "accessible_scopes": [
                        "starkware.cairo.common.alloc",
                        "starkware.cairo.common.alloc.alloc"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 0,
                            "offset": 0
                        },
                        "reference_ids": {}
                    }
                }
            ],
            "12": [
                {
                    "accessible_scopes": [
                        "starkware.cairo.common.memcpy",
                        "starkware.cairo.common.memcpy.memcpy"
                    ],
                    "code": "vm_enter_scope({'n': ids.len})",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 2,
                            "offset": 0
                        },
                        "reference_ids": {
                            "starkware.cairo.common.memcpy.memcpy.dst": 5,
                            "starkware.cairo.common.memcpy.memcpy.len": 7,
                            "starkware.cairo.common.memcpy.memcpy.src": 6
                        }
                    }
                }
            ],
            "20": [
                {
                    "accessible_scopes": [
                        "starkware.cairo.common.memcpy",
                        "starkware.cairo.common.memcpy.memcpy"
                    ],
                    "code": "n -= 1\nids.continue_copying = 1 if n > 0 else 0",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 2,
                            "offset": 5
                        },
                        "reference_ids": {
                            "starkware.cairo.common.memcpy.memcpy.__temp0": 10,
                            "starkware.cairo.common.memcpy.memcpy.continue_copying": 11,
                            "starkware.cairo.common.memcpy.memcpy.dst": 5,
                            "starkware.cairo.common.memcpy.memcpy.frame": 9,
                            "starkware.cairo.common.memcpy.memcpy.len": 7,
                            "starkware.cairo.common.memcpy.memcpy.next_frame": 12,
                            "starkware.cairo.common.memcpy.memcpy.src": 6
                        }
                    }
                }
            ],
            "23": [
                {
                    "accessible_scopes": [
                        "starkware.cairo.common.memcpy",
                        "starkware.cairo.common.memcpy.memcpy"
                    ],
                    "code": "vm_exit_scope()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 2,
                            "offset": 6
                        },
                        "reference_ids": {
                            "starkware.cairo.common.memcpy.memcpy.__temp0": 10,
                            "starkware.cairo.common.memcpy.memcpy.continue_copying": 11,
                            "starkware.cairo.common.memcpy.memcpy.dst": 5,
                            "starkware.cairo.common.memcpy.memcpy.frame": 9,
                            "starkware.cairo.common.memcpy.memcpy.len": 7,
                            "starkware.cairo.common.memcpy.memcpy.next_frame": 12,
                            "starkware.cairo.common.memcpy.memcpy.src": 6
                        }
                    }
                }
            ],
            "25": [
                {
                    "accessible_scopes": [
                        "starkware.cairo.common.math",
                        "starkware.cairo.common.math.assert_not_equal"
                    ],
                    "code": "from starkware.cairo.lang.vm.relocatable import RelocatableValue\nboth_ints = isinstance(ids.a, int) and isinstance(ids.b, int)\nboth_relocatable = (\n    isinstance(ids.a, RelocatableValue) and isinstance(ids.b, RelocatableValue) and\n    ids.a.segment_index == ids.b.segment_index)\nassert both_ints or both_relocatable, \\\n    f'assert_not_equal failed: non-comparable values: {ids.a}, {ids.b}.'\nassert (ids.a - ids.b) % PRIME != 0, f'assert_not_equal failed: {ids.a} = {ids.b}.'",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 0
                        },
                        "reference_ids": {
                            "starkware.cairo.common.math.assert_not_equal.a": 13,
                            "starkware.cairo.common.math.assert_not_equal.b": 14
                        }
                    }
                }
            ],
            "38": [
                {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.call_contract"
                    ],
                    "code": "syscall_handler.call_contract(segments=segments, syscall_ptr=ids.syscall_ptr)",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.call_contract.__temp2": 22,
                            "starkware.starknet.common.syscalls.call_contract.calldata": 19,
                            "starkware.starknet.common.syscalls.call_contract.calldata_size": 18,
                            "starkware.starknet.common.syscalls.call_contract.contract_address": 16,
                            "starkware.starknet.common.syscalls.call_contract.function_selector": 17,
                            "starkware.starknet.common.syscalls.call_contract.syscall": 21,
                            "starkware.starknet.common.syscalls.call_contract.syscall_ptr": 20
                        }
                    }
                }
            ],
            "51": [
                {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.deploy"
                    ],
                    "code": "syscall_handler.deploy(segments=segments, syscall_ptr=ids.syscall_ptr)",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.deploy.__temp3": 32,
                            "starkware.starknet.common.syscalls.deploy.class_hash": 25,
                            "starkware.starknet.common.syscalls.deploy.constructor_calldata": 28,
                            "starkware.starknet.common.syscalls.deploy.constructor_calldata_size": 27,
                            "starkware.starknet.common.syscalls.deploy.contract_address_salt": 26,
                            "starkware.starknet.common.syscalls.deploy.deploy_from_zero": 29,
                            "starkware.starknet.common.syscalls.deploy.syscall": 31,
                            "starkware.starknet.common.syscalls.deploy.syscall_ptr": 30
                        }
                    }
                }
            ],
            "58": [
                {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.get_caller_address"
                    ],
                    "code": "syscall_handler.get_caller_address(segments=segments, syscall_ptr=ids.syscall_ptr)",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 7,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.get_caller_address.__temp4": 37,
                            "starkware.starknet.common.syscalls.get_caller_address.syscall": 36,
                            "starkware.starknet.common.syscalls.get_caller_address.syscall_ptr": 35
                        }
                    }
                }
            ],
            "65": [
                {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.get_contract_address"
                    ],
                    "code": "syscall_handler.get_contract_address(segments=segments, syscall_ptr=ids.syscall_ptr)",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 8,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.get_contract_address.__temp5": 41,
                            "starkware.starknet.common.syscalls.get_contract_address.syscall": 40,
                            "starkware.starknet.common.syscalls.get_contract_address.syscall_ptr": 39
                        }
                    }
                }
            ],
            "73": [
                {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_read"
                    ],
                    "code": "syscall_handler.storage_read(segments=segments, syscall_ptr=ids.syscall_ptr)",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_read.__temp6": 46,
                            "starkware.starknet.common.syscalls.storage_read.address": 43,
                            "starkware.starknet.common.syscalls.storage_read.syscall": 45,
                            "starkware.starknet.common.syscalls.storage_read.syscall_ptr": 44
                        }
                    }
                }
            ],
            "82": [
                {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_write"
                    ],
                    "code": "syscall_handler.storage_write(segments=segments, syscall_ptr=ids.syscall_ptr)",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 10,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_write.__temp7": 52,
                            "starkware.starknet.common.syscalls.storage_write.address": 49,
                            "starkware.starknet.common.syscalls.storage_write.syscall_ptr": 51,
                            "starkware.starknet.common.syscalls.storage_write.value": 50
                        }
                    }
                }
            ],
            "88": [
                {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.get_tx_info"
                    ],
                    "code": "syscall_handler.get_tx_info(segments=segments, syscall_ptr=ids.syscall_ptr)",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 11,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.get_tx_info.__temp8": 56,
                            "starkware.starknet.common.syscalls.get_tx_info.syscall": 55,
                            "starkware.starknet.common.syscalls.get_tx_info.syscall_ptr": 54
                        }
                    }
                }
            ],
            "165": [
                {
                    "accessible_scopes": [
                        "starkware.cairo.common.signature",
                        "starkware.cairo.common.signature.verify_ecdsa_signature"
                    ],
                    "code": "ecdsa_builtin.add_signature(ids.ecdsa_ptr.address_, (ids.signature_r, ids.signature_s))",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 18,
                            "offset": 0
                        },
                        "reference_ids": {
                            "starkware.cairo.common.signature.verify_ecdsa_signature.ecdsa_ptr": 99,
                            "starkware.cairo.common.signature.verify_ecdsa_signature.message": 95,
                            "starkware.cairo.common.signature.verify_ecdsa_signature.public_key": 96,
                            "starkware.cairo.common.signature.verify_ecdsa_signature.signature_r": 97,
                            "starkware.cairo.common.signature.verify_ecdsa_signature.signature_s": 98
                        }
                    }
                }
            ],
            "213": [
                {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.assert_only_self"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 23,
                            "offset": 16
                        },
                        "reference_ids": {
                            "__wrappers__.assert_only_self.__calldata_actual_size": 134,
                            "__wrappers__.assert_only_self.__calldata_ptr": 133,
                            "__wrappers__.assert_only_self.ecdsa_ptr": 132,
                            "__wrappers__.assert_only_self.pedersen_ptr": 130,
                            "__wrappers__.assert_only_self.range_check_ptr": 131,
                            "__wrappers__.assert_only_self.ret_value": 136,
                            "__wrappers__.assert_only_self.syscall_ptr": 135
                        }
                    }
                }
            ],
            "229": [
                {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_public_key_encode_return"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 25,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__wrappers__.get_public_key_encode_return.range_check_ptr": 147,
                            "__wrappers__.get_public_key_encode_return.ret_value": 146
                        }
                    }
                }
            ],
            "272": [
                {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.set_public_key"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 28,
                            "offset": 44
                        },
                        "reference_ids": {
                            "__wrappers__.set_public_key.__calldata_actual_size": 180,
                            "__wrappers__.set_public_key.__calldata_arg_new_public_key": 178,
                            "__wrappers__.set_public_key.__calldata_ptr": 179,
                            "__wrappers__.set_public_key.__temp14": 181,
                            "__wrappers__.set_public_key.ecdsa_ptr": 176,
                            "__wrappers__.set_public_key.pedersen_ptr": 183,
                            "__wrappers__.set_public_key.range_check_ptr": 184,
                            "__wrappers__.set_public_key.ret_value": 185,
                            "__wrappers__.set_public_key.syscall_ptr": 182
                        }
                    }
                }
            ],
            "298": [
                {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.constructor"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 30,
                            "offset": 29
                        },
                        "reference_ids": {
                            "__wrappers__.constructor.__calldata_actual_size": 202,
                            "__wrappers__.constructor.__calldata_arg__public_key": 200,
                            "__wrappers__.constructor.__calldata_ptr": 201,
                            "__wrappers__.constructor.__temp15": 203,
                            "__wrappers__.constructor.ecdsa_ptr": 198,
                            "__wrappers__.constructor.pedersen_ptr": 205,
                            "__wrappers__.constructor.range_check_ptr": 206,
                            "__wrappers__.constructor.ret_value": 207,
                            "__wrappers__.constructor.syscall_ptr": 204
                        }
                    }
                }
            ],
            "347": [
                {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.is_valid_signature"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 32,
                            "offset": 50
                        },
                        "reference_ids": {
                            "__wrappers__.is_valid_signature.__calldata_actual_size": 240,
                            "__wrappers__.is_valid_signature.__calldata_arg_hash": 229,
                            "__wrappers__.is_valid_signature.__calldata_arg_signature": 236,
                            "__wrappers__.is_valid_signature.__calldata_arg_signature_len": 231,
                            "__wrappers__.is_valid_signature.__calldata_ptr": 239,
                            "__wrappers__.is_valid_signature.__temp16": 233,
                            "__wrappers__.is_valid_signature.__temp17": 234,
                            "__wrappers__.is_valid_signature.__temp18": 237,
                            "__wrappers__.is_valid_signature.__temp19": 238,
                            "__wrappers__.is_valid_signature.__temp20": 241,
                            "__wrappers__.is_valid_signature.ecdsa_ptr": 245,
                            "__wrappers__.is_valid_signature.pedersen_ptr": 243,
                            "__wrappers__.is_valid_signature.range_check_ptr": 244,
                            "__wrappers__.is_valid_signature.ret_value": 246,
                            "__wrappers__.is_valid_signature.syscall_ptr": 242
                        }
                    }
                }
            ],
            "380": [
                {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.__validate_declare__"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 34,
                            "offset": 58
                        },
                        "reference_ids": {
                            "__wrappers__.__validate_declare__.__calldata_actual_size": 267,
                            "__wrappers__.__validate_declare__.__calldata_arg_class_hash": 265,
                            "__wrappers__.__validate_declare__.__calldata_ptr": 266,
                            "__wrappers__.__validate_declare__.__temp21": 268,
                            "__wrappers__.__validate_declare__.ecdsa_ptr": 272,
                            "__wrappers__.__validate_declare__.pedersen_ptr": 270,
                            "__wrappers__.__validate_declare__.range_check_ptr": 271,
                            "__wrappers__.__validate_declare__.ret_value": 273,
                            "__wrappers__.__validate_declare__.syscall_ptr": 269
                        }
                    }
                }
            ],
            "434": [
                {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.__validate__"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 36,
                            "offset": 72
                        },
                        "reference_ids": {
                            "__wrappers__.__validate__.__calldata_actual_size": 314,
                            "__wrappers__.__validate__.__calldata_arg_call_array": 300,
                            "__wrappers__.__validate__.__calldata_arg_call_array_len": 295,
                            "__wrappers__.__validate__.__calldata_arg_calldata": 310,
                            "__wrappers__.__validate__.__calldata_arg_calldata_len": 305,
                            "__wrappers__.__validate__.__calldata_ptr": 313,
                            "__wrappers__.__validate__.__temp22": 297,
                            "__wrappers__.__validate__.__temp23": 298,
                            "__wrappers__.__validate__.__temp24": 301,
                            "__wrappers__.__validate__.__temp25": 302,
                            "__wrappers__.__validate__.__temp26": 303,
                            "__wrappers__.__validate__.__temp27": 307,
                            "__wrappers__.__validate__.__temp28": 308,
                            "__wrappers__.__validate__.__temp29": 311,
                            "__wrappers__.__validate__.__temp30": 312,
                            "__wrappers__.__validate__.__temp31": 315,
                            "__wrappers__.__validate__.ecdsa_ptr": 319,
                            "__wrappers__.__validate__.pedersen_ptr": 317,
                            "__wrappers__.__validate__.range_check_ptr": 318,
                            "__wrappers__.__validate__.ret_value": 320,
                            "__wrappers__.__validate__.syscall_ptr": 316
                        }
                    }
                }
            ],
            "536": [
                {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.deploy_contract_encode_return"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 43,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__wrappers__.deploy_contract_encode_return.range_check_ptr": 389,
                            "__wrappers__.deploy_contract_encode_return.ret_value": 388
                        }
                    }
                }
            ]
        },
        "identifiers": {
            "__main__.Call": {
                "full_name": "__main__.Call",
                "members": {
                    "calldata": {
                        "cairo_type": "felt*",
                        "offset": 3
                    },
                    "calldata_len": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "to": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "__main__.CallArray": {
                "full_name": "__main__.CallArray",
                "members": {
                    "data_len": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "data_offset": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "to": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "__main__.HashBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.HashBuiltin",
                "type": "alias"
            },
            "__main__.MultiCall": {
                "full_name": "__main__.MultiCall",
                "members": {
                    "account": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "calls": {
                        "cairo_type": "__main__.Call*",
                        "offset": 2
                    },
                    "calls_len": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "max_fee": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "version": {
                        "cairo_type": "felt",
                        "offset": 4
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "__main__.ORIGIN_ADDRESS": {
                "destination": "starkware.starknet.common.constants.ORIGIN_ADDRESS",
                "type": "alias"
            },
            "__main__.PREFIX_TRANSACTION": {
                "destination": "utils.constants.PREFIX_TRANSACTION",
                "type": "alias"
            },
            "__main__.SignatureBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.SignatureBuiltin",
                "type": "alias"
            },
            "__main__.__execute__": {
                "decorators": [
                    "external",
                    "raw_output"
                ],
                "pc": 444,
                "type": "function"
            },
            "__main__.__execute__.Args": {
                "full_name": "__main__.__execute__.Args",
                "members": {
                    "call_array": {
                        "cairo_type": "__main__.CallArray*",
                        "offset": 1
                    },
                    "call_array_len": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "calldata": {
                        "cairo_type": "felt*",
                        "offset": 3
                    },
                    "calldata_len": {
                        "cairo_type": "felt",
                        "offset": 2
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "__main__.__execute__.ImplicitArgs": {
                "full_name": "__main__.__execute__.ImplicitArgs",
                "members": {
                    "ecdsa_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                        "offset": 3
                    },
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "__main__.__execute__.Return": {
                "cairo_type": "(retdata_size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "__main__.__execute__.SIZEOF_LOCALS": {
                "type": "const",
                "value": 8
            },
            "__main__.__execute__.__fp__": {
                "cairo_type": "felt*",
                "full_name": "__main__.__execute__.__fp__",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 10
                        },
                        "pc": 448,
                        "value": "[cast(ap + (-2), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.call_array": {
                "cairo_type": "__main__.CallArray*",
                "full_name": "__main__.__execute__.call_array",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 0
                        },
                        "pc": 444,
                        "value": "[cast(fp + (-5), __main__.CallArray**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.call_array_len": {
                "cairo_type": "felt",
                "full_name": "__main__.__execute__.call_array_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 0
                        },
                        "pc": 444,
                        "value": "[cast(fp + (-6), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.calldata": {
                "cairo_type": "felt*",
                "full_name": "__main__.__execute__.calldata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 0
                        },
                        "pc": 444,
                        "value": "[cast(fp + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.calldata_len": {
                "cairo_type": "felt",
                "full_name": "__main__.__execute__.calldata_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 0
                        },
                        "pc": 444,
                        "value": "[cast(fp + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.caller": {
                "cairo_type": "felt",
                "full_name": "__main__.__execute__.caller",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 22
                        },
                        "pc": 455,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.calls": {
                "cairo_type": "__main__.Call*",
                "full_name": "__main__.__execute__.calls",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 30
                        },
                        "pc": 464,
                        "value": "[cast(ap + (-1), __main__.Call**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 30
                        },
                        "pc": 465,
                        "value": "[cast(fp + 1, __main__.Call**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.calls_len": {
                "cairo_type": "felt",
                "full_name": "__main__.__execute__.calls_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 38,
                            "offset": 0
                        },
                        "pc": 472,
                        "value": "[cast(fp + (-6), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.ecdsa_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                "full_name": "__main__.__execute__.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 0
                        },
                        "pc": 444,
                        "value": "[cast(fp + (-7), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.multicall": {
                "cairo_type": "__main__.MultiCall",
                "full_name": "__main__.__execute__.multicall",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 38,
                            "offset": 0
                        },
                        "pc": 477,
                        "value": "[cast(fp + 2, __main__.MultiCall*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.__execute__.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 0
                        },
                        "pc": 444,
                        "value": "[cast(fp + (-9), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.__execute__.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 0
                        },
                        "pc": 444,
                        "value": "[cast(fp + (-8), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.response": {
                "cairo_type": "felt*",
                "full_name": "__main__.__execute__.response",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 38,
                            "offset": 3
                        },
                        "pc": 479,
                        "value": "[cast(ap + (-1), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 38,
                            "offset": 3
                        },
                        "pc": 480,
                        "value": "[cast(fp + 7, felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.response_len": {
                "cairo_type": "felt",
                "full_name": "__main__.__execute__.response_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 39,
                            "offset": 0
                        },
                        "pc": 486,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.__execute__.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 0
                        },
                        "pc": 444,
                        "value": "[cast(fp + (-10), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 13
                        },
                        "pc": 451,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 19
                        },
                        "pc": 454,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 38,
                            "offset": 0
                        },
                        "pc": 470,
                        "value": "[cast(ap + (-1), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 39,
                            "offset": 0
                        },
                        "pc": 483,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 16
                        },
                        "pc": 451,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 22
                        },
                        "pc": 455,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 38,
                            "offset": 0
                        },
                        "pc": 472,
                        "value": "[cast(ap + (-1), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 39,
                            "offset": 0
                        },
                        "pc": 486,
                        "value": "[cast(ap + (-2), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__execute__.tx_info": {
                "cairo_type": "starkware.starknet.common.syscalls.TxInfo*",
                "full_name": "__main__.__execute__.tx_info",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 16
                        },
                        "pc": 451,
                        "value": "[cast(ap + (-1), starkware.starknet.common.syscalls.TxInfo**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 37,
                            "offset": 16
                        },
                        "pc": 452,
                        "value": "[cast(fp, starkware.starknet.common.syscalls.TxInfo**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate__": {
                "decorators": [
                    "external"
                ],
                "pc": 390,
                "type": "function"
            },
            "__main__.__validate__.Args": {
                "full_name": "__main__.__validate__.Args",
                "members": {
                    "call_array": {
                        "cairo_type": "__main__.CallArray*",
                        "offset": 1
                    },
                    "call_array_len": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "calldata": {
                        "cairo_type": "felt*",
                        "offset": 3
                    },
                    "calldata_len": {
                        "cairo_type": "felt",
                        "offset": 2
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "__main__.__validate__.ImplicitArgs": {
                "full_name": "__main__.__validate__.ImplicitArgs",
                "members": {
                    "ecdsa_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                        "offset": 3
                    },
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "__main__.__validate__.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "__main__.__validate__.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.__validate__.call_array": {
                "cairo_type": "__main__.CallArray*",
                "full_name": "__main__.__validate__.call_array",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 0
                        },
                        "pc": 390,
                        "value": "[cast(fp + (-5), __main__.CallArray**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate__.call_array_len": {
                "cairo_type": "felt",
                "full_name": "__main__.__validate__.call_array_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 0
                        },
                        "pc": 390,
                        "value": "[cast(fp + (-6), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate__.calldata": {
                "cairo_type": "felt*",
                "full_name": "__main__.__validate__.calldata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 0
                        },
                        "pc": 390,
                        "value": "[cast(fp + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate__.calldata_len": {
                "cairo_type": "felt",
                "full_name": "__main__.__validate__.calldata_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 0
                        },
                        "pc": 390,
                        "value": "[cast(fp + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate__.ecdsa_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                "full_name": "__main__.__validate__.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 0
                        },
                        "pc": 390,
                        "value": "[cast(fp + (-7), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 50
                        },
                        "pc": 402,
                        "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate__.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.__validate__.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 0
                        },
                        "pc": 390,
                        "value": "[cast(fp + (-9), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 50
                        },
                        "pc": 402,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate__.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.__validate__.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 0
                        },
                        "pc": 390,
                        "value": "[cast(fp + (-8), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 50
                        },
                        "pc": 402,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate__.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.__validate__.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 0
                        },
                        "pc": 390,
                        "value": "[cast(fp + (-10), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 6
                        },
                        "pc": 393,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 50
                        },
                        "pc": 402,
                        "value": "[cast(ap + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate__.tx_info": {
                "cairo_type": "starkware.starknet.common.syscalls.TxInfo*",
                "full_name": "__main__.__validate__.tx_info",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 35,
                            "offset": 6
                        },
                        "pc": 393,
                        "value": "[cast(ap + (-1), starkware.starknet.common.syscalls.TxInfo**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate_declare__": {
                "decorators": [
                    "external"
                ],
                "pc": 357,
                "type": "function"
            },
            "__main__.__validate_declare__.Args": {
                "full_name": "__main__.__validate_declare__.Args",
                "members": {
                    "class_hash": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.__validate_declare__.ImplicitArgs": {
                "full_name": "__main__.__validate_declare__.ImplicitArgs",
                "members": {
                    "ecdsa_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                        "offset": 3
                    },
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "__main__.__validate_declare__.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "__main__.__validate_declare__.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.__validate_declare__.class_hash": {
                "cairo_type": "felt",
                "full_name": "__main__.__validate_declare__.class_hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 0
                        },
                        "pc": 357,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate_declare__.ecdsa_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                "full_name": "__main__.__validate_declare__.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 0
                        },
                        "pc": 357,
                        "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 50
                        },
                        "pc": 369,
                        "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate_declare__.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.__validate_declare__.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 0
                        },
                        "pc": 357,
                        "value": "[cast(fp + (-6), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 50
                        },
                        "pc": 369,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate_declare__.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.__validate_declare__.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 0
                        },
                        "pc": 357,
                        "value": "[cast(fp + (-5), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 50
                        },
                        "pc": 369,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate_declare__.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.__validate_declare__.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 0
                        },
                        "pc": 357,
                        "value": "[cast(fp + (-7), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 6
                        },
                        "pc": 360,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 50
                        },
                        "pc": 369,
                        "value": "[cast(ap + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.__validate_declare__.tx_info": {
                "cairo_type": "starkware.starknet.common.syscalls.TxInfo*",
                "full_name": "__main__.__validate_declare__.tx_info",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 33,
                            "offset": 6
                        },
                        "pc": 360,
                        "value": "[cast(ap + (-1), starkware.starknet.common.syscalls.TxInfo**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.alloc": {
                "destination": "starkware.cairo.common.alloc.alloc",
                "type": "alias"
            },
            "__main__.assert_not_equal": {
                "destination": "starkware.cairo.common.math.assert_not_equal",
                "type": "alias"
            },
            "__main__.assert_only_self": {
                "decorators": [
                    "view"
                ],
                "pc": 200,
                "type": "function"
            },
            "__main__.assert_only_self.Args": {
                "full_name": "__main__.assert_only_self.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.assert_only_self.ImplicitArgs": {
                "full_name": "__main__.assert_only_self.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.assert_only_self.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "__main__.assert_only_self.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.assert_only_self.caller": {
                "cairo_type": "felt",
                "full_name": "__main__.assert_only_self.caller",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 22,
                            "offset": 12
                        },
                        "pc": 206,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.assert_only_self.self": {
                "cairo_type": "felt",
                "full_name": "__main__.assert_only_self.self",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 22,
                            "offset": 6
                        },
                        "pc": 203,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.assert_only_self.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.assert_only_self.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 22,
                            "offset": 0
                        },
                        "pc": 200,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 22,
                            "offset": 6
                        },
                        "pc": 203,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 22,
                            "offset": 12
                        },
                        "pc": 206,
                        "value": "[cast(ap + (-2), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.call_contract": {
                "destination": "starkware.starknet.common.syscalls.call_contract",
                "type": "alias"
            },
            "__main__.constructor": {
                "decorators": [
                    "constructor"
                ],
                "pc": 282,
                "type": "function"
            },
            "__main__.constructor.Args": {
                "full_name": "__main__.constructor.Args",
                "members": {
                    "_public_key": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.constructor.ImplicitArgs": {
                "full_name": "__main__.constructor.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.constructor.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "__main__.constructor.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.constructor._public_key": {
                "cairo_type": "felt",
                "full_name": "__main__.constructor._public_key",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 29,
                            "offset": 0
                        },
                        "pc": 282,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.constructor.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.constructor.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 29,
                            "offset": 0
                        },
                        "pc": 282,
                        "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 29,
                            "offset": 22
                        },
                        "pc": 288,
                        "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.constructor.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.constructor.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 29,
                            "offset": 0
                        },
                        "pc": 282,
                        "value": "[cast(fp + (-4), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 29,
                            "offset": 22
                        },
                        "pc": 288,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.constructor.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.constructor.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 29,
                            "offset": 0
                        },
                        "pc": 282,
                        "value": "[cast(fp + (-6), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 29,
                            "offset": 22
                        },
                        "pc": 288,
                        "value": "[cast(ap + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.deploy": {
                "destination": "starkware.starknet.common.syscalls.deploy",
                "type": "alias"
            },
            "__main__.deploy_contract": {
                "decorators": [
                    "external"
                ],
                "pc": 525,
                "type": "function"
            },
            "__main__.deploy_contract.Args": {
                "full_name": "__main__.deploy_contract.Args",
                "members": {
                    "class_hash": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "constructor_calldata": {
                        "cairo_type": "felt*",
                        "offset": 3
                    },
                    "constructor_calldata_len": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "contract_address_salt": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "deploy_from_zero": {
                        "cairo_type": "felt",
                        "offset": 4
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "__main__.deploy_contract.ImplicitArgs": {
                "full_name": "__main__.deploy_contract.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.deploy_contract.Return": {
                "cairo_type": "(contract_address: felt)",
                "type": "type_definition"
            },
            "__main__.deploy_contract.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.deploy_contract.class_hash": {
                "cairo_type": "felt",
                "full_name": "__main__.deploy_contract.class_hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 42,
                            "offset": 0
                        },
                        "pc": 525,
                        "value": "[cast(fp + (-7), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.deploy_contract.constructor_calldata": {
                "cairo_type": "felt*",
                "full_name": "__main__.deploy_contract.constructor_calldata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 42,
                            "offset": 0
                        },
                        "pc": 525,
                        "value": "[cast(fp + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.deploy_contract.constructor_calldata_len": {
                "cairo_type": "felt",
                "full_name": "__main__.deploy_contract.constructor_calldata_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 42,
                            "offset": 0
                        },
                        "pc": 525,
                        "value": "[cast(fp + (-5), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.deploy_contract.contract_address": {
                "cairo_type": "felt",
                "full_name": "__main__.deploy_contract.contract_address",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 42,
                            "offset": 26
                        },
                        "pc": 535,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.deploy_contract.contract_address_salt": {
                "cairo_type": "felt",
                "full_name": "__main__.deploy_contract.contract_address_salt",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 42,
                            "offset": 0
                        },
                        "pc": 525,
                        "value": "[cast(fp + (-6), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.deploy_contract.deploy_from_zero": {
                "cairo_type": "felt",
                "full_name": "__main__.deploy_contract.deploy_from_zero",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 42,
                            "offset": 0
                        },
                        "pc": 525,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.deploy_contract.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.deploy_contract.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 42,
                            "offset": 0
                        },
                        "pc": 525,
                        "value": "[cast(fp + (-8), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 42,
                            "offset": 16
                        },
                        "pc": 528,
                        "value": "[cast(ap + (-1), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 42,
                            "offset": 26
                        },
                        "pc": 535,
                        "value": "[cast(ap + (-2), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.execute_list": {
                "decorators": [],
                "pc": 577,
                "type": "function"
            },
            "__main__.execute_list.Args": {
                "full_name": "__main__.execute_list.Args",
                "members": {
                    "calls": {
                        "cairo_type": "__main__.Call*",
                        "offset": 1
                    },
                    "calls_len": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "felt*",
                        "offset": 2
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.execute_list.ImplicitArgs": {
                "full_name": "__main__.execute_list.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.execute_list.Return": {
                "cairo_type": "(response_len: felt)",
                "type": "type_definition"
            },
            "__main__.execute_list.SIZEOF_LOCALS": {
                "type": "const",
                "value": 3
            },
            "__main__.execute_list.calls": {
                "cairo_type": "__main__.Call*",
                "full_name": "__main__.execute_list.calls",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 45,
                            "offset": 0
                        },
                        "pc": 577,
                        "value": "[cast(fp + (-4), __main__.Call**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.execute_list.calls_len": {
                "cairo_type": "felt",
                "full_name": "__main__.execute_list.calls_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 45,
                            "offset": 0
                        },
                        "pc": 577,
                        "value": "[cast(fp + (-5), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.execute_list.res": {
                "cairo_type": "(retdata_size: felt, retdata: felt*)",
                "full_name": "__main__.execute_list.res",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 45,
                            "offset": 14
                        },
                        "pc": 592,
                        "value": "[cast(ap + (-2), (retdata_size: felt, retdata: felt*)*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 45,
                            "offset": 14
                        },
                        "pc": 594,
                        "value": "[cast(fp, (retdata_size: felt, retdata: felt*)*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.execute_list.response": {
                "cairo_type": "felt*",
                "full_name": "__main__.execute_list.response",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 45,
                            "offset": 0
                        },
                        "pc": 577,
                        "value": "[cast(fp + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.execute_list.response_len": {
                "cairo_type": "felt",
                "full_name": "__main__.execute_list.response_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 47,
                            "offset": 0
                        },
                        "pc": 608,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.execute_list.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.execute_list.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 45,
                            "offset": 0
                        },
                        "pc": 577,
                        "value": "[cast(fp + (-6), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 45,
                            "offset": 11
                        },
                        "pc": 592,
                        "value": "[cast(ap + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 47,
                            "offset": 0
                        },
                        "pc": 605,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 45,
                            "offset": 14
                        },
                        "pc": 592,
                        "value": "[cast(ap + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 45,
                            "offset": 14
                        },
                        "pc": 595,
                        "value": "[cast(fp + 2, felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 47,
                            "offset": 0
                        },
                        "pc": 608,
                        "value": "[cast(ap + (-2), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.execute_list.this_call": {
                "cairo_type": "__main__.Call",
                "full_name": "__main__.execute_list.this_call",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 45,
                            "offset": 3
                        },
                        "pc": 585,
                        "value": "[cast([fp + (-4)], __main__.Call*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.from_call_array_to_call": {
                "decorators": [],
                "pc": 611,
                "type": "function"
            },
            "__main__.from_call_array_to_call.Args": {
                "full_name": "__main__.from_call_array_to_call.Args",
                "members": {
                    "call_array": {
                        "cairo_type": "__main__.CallArray*",
                        "offset": 1
                    },
                    "call_array_len": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "calldata": {
                        "cairo_type": "felt*",
                        "offset": 2
                    },
                    "calls": {
                        "cairo_type": "__main__.Call*",
                        "offset": 3
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "__main__.from_call_array_to_call.ImplicitArgs": {
                "full_name": "__main__.from_call_array_to_call.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.from_call_array_to_call.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "__main__.from_call_array_to_call.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.from_call_array_to_call.__temp49": {
                "cairo_type": "felt",
                "full_name": "__main__.from_call_array_to_call.__temp49",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 48,
                            "offset": 1
                        },
                        "pc": 616,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.from_call_array_to_call.__temp50": {
                "cairo_type": "felt",
                "full_name": "__main__.from_call_array_to_call.__temp50",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 48,
                            "offset": 2
                        },
                        "pc": 618,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.from_call_array_to_call.__temp51": {
                "cairo_type": "felt",
                "full_name": "__main__.from_call_array_to_call.__temp51",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 48,
                            "offset": 3
                        },
                        "pc": 620,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.from_call_array_to_call.__temp52": {
                "cairo_type": "felt",
                "full_name": "__main__.from_call_array_to_call.__temp52",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 48,
                            "offset": 4
                        },
                        "pc": 622,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.from_call_array_to_call.__temp53": {
                "cairo_type": "felt",
                "full_name": "__main__.from_call_array_to_call.__temp53",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 48,
                            "offset": 5
                        },
                        "pc": 623,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.from_call_array_to_call.call_array": {
                "cairo_type": "__main__.CallArray*",
                "full_name": "__main__.from_call_array_to_call.call_array",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 48,
                            "offset": 0
                        },
                        "pc": 611,
                        "value": "[cast(fp + (-5), __main__.CallArray**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.from_call_array_to_call.call_array_len": {
                "cairo_type": "felt",
                "full_name": "__main__.from_call_array_to_call.call_array_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 48,
                            "offset": 0
                        },
                        "pc": 611,
                        "value": "[cast(fp + (-6), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.from_call_array_to_call.calldata": {
                "cairo_type": "felt*",
                "full_name": "__main__.from_call_array_to_call.calldata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 48,
                            "offset": 0
                        },
                        "pc": 611,
                        "value": "[cast(fp + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.from_call_array_to_call.calls": {
                "cairo_type": "__main__.Call*",
                "full_name": "__main__.from_call_array_to_call.calls",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 48,
                            "offset": 0
                        },
                        "pc": 611,
                        "value": "[cast(fp + (-3), __main__.Call**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.from_call_array_to_call.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.from_call_array_to_call.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 48,
                            "offset": 0
                        },
                        "pc": 611,
                        "value": "[cast(fp + (-7), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 49,
                            "offset": 0
                        },
                        "pc": 634,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.get_caller_address": {
                "destination": "starkware.starknet.common.syscalls.get_caller_address",
                "type": "alias"
            },
            "__main__.get_contract_address": {
                "destination": "starkware.starknet.common.syscalls.get_contract_address",
                "type": "alias"
            },
            "__main__.get_fp_and_pc": {
                "destination": "starkware.cairo.common.registers.get_fp_and_pc",
                "type": "alias"
            },
            "__main__.get_public_key": {
                "decorators": [
                    "view"
                ],
                "pc": 223,
                "type": "function"
            },
            "__main__.get_public_key.Args": {
                "full_name": "__main__.get_public_key.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.get_public_key.ImplicitArgs": {
                "full_name": "__main__.get_public_key.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.get_public_key.Return": {
                "cairo_type": "(res: felt)",
                "type": "type_definition"
            },
            "__main__.get_public_key.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.get_public_key.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.get_public_key.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 24,
                            "offset": 0
                        },
                        "pc": 223,
                        "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 24,
                            "offset": 23
                        },
                        "pc": 228,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.get_public_key.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.get_public_key.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 24,
                            "offset": 0
                        },
                        "pc": 223,
                        "value": "[cast(fp + (-3), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 24,
                            "offset": 23
                        },
                        "pc": 228,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.get_public_key.res": {
                "cairo_type": "felt",
                "full_name": "__main__.get_public_key.res",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 24,
                            "offset": 23
                        },
                        "pc": 228,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.get_public_key.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.get_public_key.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 24,
                            "offset": 0
                        },
                        "pc": 223,
                        "value": "[cast(fp + (-5), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 24,
                            "offset": 23
                        },
                        "pc": 228,
                        "value": "[cast(ap + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.get_tx_info": {
                "destination": "starkware.starknet.common.syscalls.get_tx_info",
                "type": "alias"
            },
            "__main__.hash_finalize": {
                "destination": "starkware.cairo.common.hash_state.hash_finalize",
                "type": "alias"
            },
            "__main__.hash_init": {
                "destination": "starkware.cairo.common.hash_state.hash_init",
                "type": "alias"
            },
            "__main__.hash_update": {
                "destination": "starkware.cairo.common.hash_state.hash_update",
                "type": "alias"
            },
            "__main__.hash_update_single": {
                "destination": "starkware.cairo.common.hash_state.hash_update_single",
                "type": "alias"
            },
            "__main__.is_valid_signature": {
                "decorators": [
                    "view"
                ],
                "pc": 308,
                "type": "function"
            },
            "__main__.is_valid_signature.Args": {
                "full_name": "__main__.is_valid_signature.Args",
                "members": {
                    "hash": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "signature": {
                        "cairo_type": "felt*",
                        "offset": 2
                    },
                    "signature_len": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.is_valid_signature.ImplicitArgs": {
                "full_name": "__main__.is_valid_signature.ImplicitArgs",
                "members": {
                    "ecdsa_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                        "offset": 3
                    },
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "__main__.is_valid_signature.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "__main__.is_valid_signature.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.is_valid_signature._public_key": {
                "cairo_type": "felt",
                "full_name": "__main__.is_valid_signature._public_key",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 23
                        },
                        "pc": 313,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.is_valid_signature.ecdsa_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                "full_name": "__main__.is_valid_signature.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 0
                        },
                        "pc": 308,
                        "value": "[cast(fp + (-6), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 31
                        },
                        "pc": 322,
                        "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.is_valid_signature.hash": {
                "cairo_type": "felt",
                "full_name": "__main__.is_valid_signature.hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 0
                        },
                        "pc": 308,
                        "value": "[cast(fp + (-5), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.is_valid_signature.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.is_valid_signature.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 0
                        },
                        "pc": 308,
                        "value": "[cast(fp + (-8), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 23
                        },
                        "pc": 313,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.is_valid_signature.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.is_valid_signature.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 0
                        },
                        "pc": 308,
                        "value": "[cast(fp + (-7), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 23
                        },
                        "pc": 313,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.is_valid_signature.sig_r": {
                "cairo_type": "felt",
                "full_name": "__main__.is_valid_signature.sig_r",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 23
                        },
                        "pc": 315,
                        "value": "[cast([fp + (-3)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.is_valid_signature.sig_s": {
                "cairo_type": "felt",
                "full_name": "__main__.is_valid_signature.sig_s",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 23
                        },
                        "pc": 315,
                        "value": "[cast([fp + (-3)] + 1, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.is_valid_signature.signature": {
                "cairo_type": "felt*",
                "full_name": "__main__.is_valid_signature.signature",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 0
                        },
                        "pc": 308,
                        "value": "[cast(fp + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.is_valid_signature.signature_len": {
                "cairo_type": "felt",
                "full_name": "__main__.is_valid_signature.signature_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 0
                        },
                        "pc": 308,
                        "value": "[cast(fp + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.is_valid_signature.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.is_valid_signature.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 0
                        },
                        "pc": 308,
                        "value": "[cast(fp + (-9), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 31,
                            "offset": 23
                        },
                        "pc": 313,
                        "value": "[cast(ap + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "__main__.public_key": {
                "type": "namespace"
            },
            "__main__.public_key.Args": {
                "full_name": "__main__.public_key.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.public_key.HashBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.HashBuiltin",
                "type": "alias"
            },
            "__main__.public_key.ImplicitArgs": {
                "full_name": "__main__.public_key.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.public_key.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "__main__.public_key.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.public_key.addr": {
                "decorators": [],
                "pc": 170,
                "type": "function"
            },
            "__main__.public_key.addr.Args": {
                "full_name": "__main__.public_key.addr.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.public_key.addr.ImplicitArgs": {
                "full_name": "__main__.public_key.addr.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 0
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "__main__.public_key.addr.Return": {
                "cairo_type": "(res: felt)",
                "type": "type_definition"
            },
            "__main__.public_key.addr.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.public_key.addr.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.public_key.addr.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 19,
                            "offset": 0
                        },
                        "pc": 170,
                        "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.addr.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.public_key.addr.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 19,
                            "offset": 0
                        },
                        "pc": 170,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.addr.res": {
                "cairo_type": "felt",
                "full_name": "__main__.public_key.addr.res",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 19,
                            "offset": 0
                        },
                        "pc": 170,
                        "value": "cast(1672321442399497129215646424919402195095307045612040218489019266998007191460, felt)"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.hash2": {
                "destination": "starkware.cairo.common.hash.hash2",
                "type": "alias"
            },
            "__main__.public_key.normalize_address": {
                "destination": "starkware.starknet.common.storage.normalize_address",
                "type": "alias"
            },
            "__main__.public_key.read": {
                "decorators": [],
                "pc": 175,
                "type": "function"
            },
            "__main__.public_key.read.Args": {
                "full_name": "__main__.public_key.read.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.public_key.read.ImplicitArgs": {
                "full_name": "__main__.public_key.read.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.public_key.read.Return": {
                "cairo_type": "(res: felt)",
                "type": "type_definition"
            },
            "__main__.public_key.read.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.public_key.read.__storage_var_temp0": {
                "cairo_type": "felt",
                "full_name": "__main__.public_key.read.__storage_var_temp0",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 14
                        },
                        "pc": 183,
                        "value": "[cast(ap + (-1), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 18
                        },
                        "pc": 187,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.read.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.public_key.read.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 0
                        },
                        "pc": 175,
                        "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 7
                        },
                        "pc": 179,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 16
                        },
                        "pc": 185,
                        "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.read.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.public_key.read.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 0
                        },
                        "pc": 175,
                        "value": "[cast(fp + (-3), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 7
                        },
                        "pc": 179,
                        "value": "[cast(ap + (-2), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 17
                        },
                        "pc": 186,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.read.storage_addr": {
                "cairo_type": "felt",
                "full_name": "__main__.public_key.read.storage_addr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 7
                        },
                        "pc": 179,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.read.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.public_key.read.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 0
                        },
                        "pc": 175,
                        "value": "[cast(fp + (-5), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 14
                        },
                        "pc": 183,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 20,
                            "offset": 15
                        },
                        "pc": 184,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.storage_read": {
                "destination": "starkware.starknet.common.syscalls.storage_read",
                "type": "alias"
            },
            "__main__.public_key.storage_write": {
                "destination": "starkware.starknet.common.syscalls.storage_write",
                "type": "alias"
            },
            "__main__.public_key.write": {
                "decorators": [],
                "pc": 188,
                "type": "function"
            },
            "__main__.public_key.write.Args": {
                "full_name": "__main__.public_key.write.Args",
                "members": {
                    "value": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.public_key.write.ImplicitArgs": {
                "full_name": "__main__.public_key.write.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.public_key.write.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "__main__.public_key.write.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.public_key.write.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.public_key.write.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 21,
                            "offset": 0
                        },
                        "pc": 188,
                        "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 21,
                            "offset": 7
                        },
                        "pc": 192,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.write.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.public_key.write.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 21,
                            "offset": 0
                        },
                        "pc": 188,
                        "value": "[cast(fp + (-4), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 21,
                            "offset": 7
                        },
                        "pc": 192,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.write.storage_addr": {
                "cairo_type": "felt",
                "full_name": "__main__.public_key.write.storage_addr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 21,
                            "offset": 7
                        },
                        "pc": 192,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.write.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.public_key.write.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 21,
                            "offset": 0
                        },
                        "pc": 188,
                        "value": "[cast(fp + (-6), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 21,
                            "offset": 14
                        },
                        "pc": 197,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.public_key.write.value": {
                "cairo_type": "felt",
                "full_name": "__main__.public_key.write.value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 21,
                            "offset": 0
                        },
                        "pc": 188,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.set_public_key": {
                "decorators": [
                    "external"
                ],
                "pc": 254,
                "type": "function"
            },
            "__main__.set_public_key.Args": {
                "full_name": "__main__.set_public_key.Args",
                "members": {
                    "new_public_key": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.set_public_key.ImplicitArgs": {
                "full_name": "__main__.set_public_key.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.set_public_key.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "__main__.set_public_key.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.set_public_key.new_public_key": {
                "cairo_type": "felt",
                "full_name": "__main__.set_public_key.new_public_key",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 27,
                            "offset": 0
                        },
                        "pc": 254,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.set_public_key.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.set_public_key.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 27,
                            "offset": 0
                        },
                        "pc": 254,
                        "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 27,
                            "offset": 37
                        },
                        "pc": 262,
                        "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.set_public_key.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.set_public_key.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 27,
                            "offset": 0
                        },
                        "pc": 254,
                        "value": "[cast(fp + (-4), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 27,
                            "offset": 37
                        },
                        "pc": 262,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.set_public_key.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.set_public_key.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 27,
                            "offset": 0
                        },
                        "pc": 254,
                        "value": "[cast(fp + (-6), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 27,
                            "offset": 16
                        },
                        "pc": 257,
                        "value": "[cast(ap + (-1), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 27,
                            "offset": 37
                        },
                        "pc": 262,
                        "value": "[cast(ap + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.verify_ecdsa_signature": {
                "destination": "starkware.cairo.common.signature.verify_ecdsa_signature",
                "type": "alias"
            },
            "__wrappers__.__execute__": {
                "decorators": [
                    "external",
                    "raw_output"
                ],
                "pc": 493,
                "type": "function"
            },
            "__wrappers__.__execute__.Args": {
                "full_name": "__wrappers__.__execute__.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.__execute__.ImplicitArgs": {
                "full_name": "__wrappers__.__execute__.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.__execute__.Return": {
                "cairo_type": "(syscall_ptr: felt*, pedersen_ptr: starkware.cairo.common.cairo_builtins.HashBuiltin*, range_check_ptr: felt, ecdsa_ptr: starkware.cairo.common.cairo_builtins.SignatureBuiltin*, size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.__execute__.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.__execute__.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 11
                        },
                        "pc": 509,
                        "value": "cast([ap + (-1)] - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__calldata_arg_call_array": {
                "cairo_type": "__main__.CallArray*",
                "full_name": "__wrappers__.__execute__.__calldata_arg_call_array",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 2
                        },
                        "pc": 496,
                        "value": "cast([fp + (-3)] + 1, __main__.CallArray*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__calldata_arg_call_array_len": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__calldata_arg_call_array_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 0
                        },
                        "pc": 493,
                        "value": "[cast([fp + (-3)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__calldata_arg_calldata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__execute__.__calldata_arg_calldata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 8
                        },
                        "pc": 505,
                        "value": "cast([ap + (-3)] + 1, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__calldata_arg_calldata_len": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__calldata_arg_calldata_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 6
                        },
                        "pc": 502,
                        "value": "[cast([ap + (-1)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__execute__.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 0
                        },
                        "pc": 493,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 0
                        },
                        "pc": 493,
                        "value": "cast([fp + (-3)] + 1, felt*)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 6
                        },
                        "pc": 502,
                        "value": "[cast(ap + (-1), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 6
                        },
                        "pc": 502,
                        "value": "cast([ap + (-1)] + 1, felt*)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 11
                        },
                        "pc": 509,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__temp32": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__temp32",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 1
                        },
                        "pc": 494,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__temp33": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__temp33",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 2
                        },
                        "pc": 495,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__temp34": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__temp34",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 3
                        },
                        "pc": 498,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__temp35": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__temp35",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 4
                        },
                        "pc": 499,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__temp36": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__temp36",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 5
                        },
                        "pc": 501,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__temp37": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__temp37",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 7
                        },
                        "pc": 503,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__temp38": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__temp38",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 8
                        },
                        "pc": 504,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__temp39": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__temp39",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 9
                        },
                        "pc": 507,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__temp40": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__temp40",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 10
                        },
                        "pc": 508,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__temp41": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.__temp41",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 12
                        },
                        "pc": 511,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.__wrapped_func": {
                "destination": "__main__.__execute__",
                "type": "alias"
            },
            "__wrappers__.__execute__.ecdsa_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                "full_name": "__wrappers__.__execute__.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 0
                        },
                        "pc": 493,
                        "value": "[cast([fp + (-5)] + 3, starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 41,
                            "offset": 0
                        },
                        "pc": 524,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__wrappers__.__execute__.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 0
                        },
                        "pc": 493,
                        "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 41,
                            "offset": 0
                        },
                        "pc": 524,
                        "value": "[cast(ap + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 0
                        },
                        "pc": 493,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 2
                        },
                        "pc": 496,
                        "value": "cast([[fp + (-5)] + 2] + 1, felt)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 8
                        },
                        "pc": 505,
                        "value": "cast([[fp + (-5)] + 2] + 2, felt)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 41,
                            "offset": 0
                        },
                        "pc": 524,
                        "value": "[cast(ap + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.ret_value": {
                "cairo_type": "(retdata_size: felt, retdata: felt*)",
                "full_name": "__wrappers__.__execute__.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 41,
                            "offset": 0
                        },
                        "pc": 524,
                        "value": "[cast(ap + (-2), (retdata_size: felt, retdata: felt*)*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__execute__.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 41,
                            "offset": 0
                        },
                        "pc": 524,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__execute__.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 41,
                            "offset": 0
                        },
                        "pc": 524,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute__.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__execute__.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 40,
                            "offset": 0
                        },
                        "pc": 493,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 41,
                            "offset": 0
                        },
                        "pc": 524,
                        "value": "[cast(ap + (-6), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__execute___encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "__wrappers__.__validate__": {
                "decorators": [
                    "external"
                ],
                "pc": 403,
                "type": "function"
            },
            "__wrappers__.__validate__.Args": {
                "full_name": "__wrappers__.__validate__.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.__validate__.ImplicitArgs": {
                "full_name": "__wrappers__.__validate__.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.__validate__.Return": {
                "cairo_type": "(syscall_ptr: felt*, pedersen_ptr: starkware.cairo.common.cairo_builtins.HashBuiltin*, range_check_ptr: felt, ecdsa_ptr: starkware.cairo.common.cairo_builtins.SignatureBuiltin*, size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.__validate__.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.__validate__.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 11
                        },
                        "pc": 419,
                        "value": "cast([ap + (-1)] - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__calldata_arg_call_array": {
                "cairo_type": "__main__.CallArray*",
                "full_name": "__wrappers__.__validate__.__calldata_arg_call_array",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 2
                        },
                        "pc": 406,
                        "value": "cast([fp + (-3)] + 1, __main__.CallArray*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__calldata_arg_call_array_len": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__calldata_arg_call_array_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 0
                        },
                        "pc": 403,
                        "value": "[cast([fp + (-3)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__calldata_arg_calldata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__validate__.__calldata_arg_calldata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 8
                        },
                        "pc": 415,
                        "value": "cast([ap + (-3)] + 1, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__calldata_arg_calldata_len": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__calldata_arg_calldata_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 6
                        },
                        "pc": 412,
                        "value": "[cast([ap + (-1)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__validate__.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 0
                        },
                        "pc": 403,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 0
                        },
                        "pc": 403,
                        "value": "cast([fp + (-3)] + 1, felt*)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 6
                        },
                        "pc": 412,
                        "value": "[cast(ap + (-1), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 6
                        },
                        "pc": 412,
                        "value": "cast([ap + (-1)] + 1, felt*)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 11
                        },
                        "pc": 419,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__temp22": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__temp22",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 1
                        },
                        "pc": 404,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__temp23": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__temp23",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 2
                        },
                        "pc": 405,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__temp24": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__temp24",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 3
                        },
                        "pc": 408,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__temp25": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__temp25",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 4
                        },
                        "pc": 409,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__temp26": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__temp26",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 5
                        },
                        "pc": 411,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__temp27": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__temp27",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 7
                        },
                        "pc": 413,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__temp28": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__temp28",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 8
                        },
                        "pc": 414,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__temp29": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__temp29",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 9
                        },
                        "pc": 417,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__temp30": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__temp30",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 10
                        },
                        "pc": 418,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__temp31": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.__temp31",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 12
                        },
                        "pc": 421,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.__wrapped_func": {
                "destination": "__main__.__validate__",
                "type": "alias"
            },
            "__wrappers__.__validate__.ecdsa_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                "full_name": "__wrappers__.__validate__.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 0
                        },
                        "pc": 403,
                        "value": "[cast([fp + (-5)] + 3, starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 72
                        },
                        "pc": 434,
                        "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__wrappers__.__validate__.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 0
                        },
                        "pc": 403,
                        "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 72
                        },
                        "pc": 434,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 0
                        },
                        "pc": 403,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 2
                        },
                        "pc": 406,
                        "value": "cast([[fp + (-5)] + 2] + 1, felt)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 8
                        },
                        "pc": 415,
                        "value": "cast([[fp + (-5)] + 2] + 2, felt)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 72
                        },
                        "pc": 434,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.ret_value": {
                "cairo_type": "()",
                "full_name": "__wrappers__.__validate__.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 72
                        },
                        "pc": 434,
                        "value": "[cast(ap + 0, ()*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__validate__.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 73
                        },
                        "pc": 436,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate__.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 73
                        },
                        "pc": 436,
                        "value": "cast(0, felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate__.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__validate__.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 0
                        },
                        "pc": 403,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 36,
                            "offset": 72
                        },
                        "pc": 434,
                        "value": "[cast(ap + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate___encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "__wrappers__.__validate_declare__": {
                "decorators": [
                    "external"
                ],
                "pc": 370,
                "type": "function"
            },
            "__wrappers__.__validate_declare__.Args": {
                "full_name": "__wrappers__.__validate_declare__.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.__validate_declare__.ImplicitArgs": {
                "full_name": "__wrappers__.__validate_declare__.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.__validate_declare__.Return": {
                "cairo_type": "(syscall_ptr: felt*, pedersen_ptr: starkware.cairo.common.cairo_builtins.HashBuiltin*, range_check_ptr: felt, ecdsa_ptr: starkware.cairo.common.cairo_builtins.SignatureBuiltin*, size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.__validate_declare__.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.__validate_declare__.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate_declare__.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 0
                        },
                        "pc": 370,
                        "value": "cast([fp + (-3)] + 1 - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare__.__calldata_arg_class_hash": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate_declare__.__calldata_arg_class_hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 0
                        },
                        "pc": 370,
                        "value": "[cast([fp + (-3)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare__.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__validate_declare__.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 0
                        },
                        "pc": 370,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 0
                        },
                        "pc": 370,
                        "value": "cast([fp + (-3)] + 1, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare__.__temp21": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate_declare__.__temp21",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 1
                        },
                        "pc": 372,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare__.__wrapped_func": {
                "destination": "__main__.__validate_declare__",
                "type": "alias"
            },
            "__wrappers__.__validate_declare__.ecdsa_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                "full_name": "__wrappers__.__validate_declare__.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 0
                        },
                        "pc": 370,
                        "value": "[cast([fp + (-5)] + 3, starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 58
                        },
                        "pc": 380,
                        "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare__.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__wrappers__.__validate_declare__.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 0
                        },
                        "pc": 370,
                        "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 58
                        },
                        "pc": 380,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare__.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate_declare__.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 0
                        },
                        "pc": 370,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 58
                        },
                        "pc": 380,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare__.ret_value": {
                "cairo_type": "()",
                "full_name": "__wrappers__.__validate_declare__.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 58
                        },
                        "pc": 380,
                        "value": "[cast(ap + 0, ()*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare__.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__validate_declare__.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 59
                        },
                        "pc": 382,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare__.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.__validate_declare__.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 59
                        },
                        "pc": 382,
                        "value": "cast(0, felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare__.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.__validate_declare__.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 0
                        },
                        "pc": 370,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 34,
                            "offset": 58
                        },
                        "pc": 380,
                        "value": "[cast(ap + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.__validate_declare___encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "__wrappers__.assert_only_self": {
                "decorators": [
                    "view"
                ],
                "pc": 209,
                "type": "function"
            },
            "__wrappers__.assert_only_self.Args": {
                "full_name": "__wrappers__.assert_only_self.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.assert_only_self.ImplicitArgs": {
                "full_name": "__wrappers__.assert_only_self.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.assert_only_self.Return": {
                "cairo_type": "(syscall_ptr: felt*, pedersen_ptr: felt, range_check_ptr: felt, ecdsa_ptr: felt, size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.assert_only_self.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.assert_only_self.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.assert_only_self.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 23,
                            "offset": 0
                        },
                        "pc": 209,
                        "value": "cast([fp + (-3)] - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.assert_only_self.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.assert_only_self.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 23,
                            "offset": 0
                        },
                        "pc": 209,
                        "value": "[cast(fp + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.assert_only_self.__wrapped_func": {
                "destination": "__main__.assert_only_self",
                "type": "alias"
            },
            "__wrappers__.assert_only_self.ecdsa_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.assert_only_self.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 23,
                            "offset": 0
                        },
                        "pc": 209,
                        "value": "[cast([fp + (-5)] + 3, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.assert_only_self.pedersen_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.assert_only_self.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 23,
                            "offset": 0
                        },
                        "pc": 209,
                        "value": "[cast([fp + (-5)] + 1, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.assert_only_self.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.assert_only_self.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 23,
                            "offset": 0
                        },
                        "pc": 209,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.assert_only_self.ret_value": {
                "cairo_type": "()",
                "full_name": "__wrappers__.assert_only_self.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 23,
                            "offset": 16
                        },
                        "pc": 213,
                        "value": "[cast(ap + 0, ()*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.assert_only_self.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.assert_only_self.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 23,
                            "offset": 17
                        },
                        "pc": 215,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.assert_only_self.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.assert_only_self.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 23,
                            "offset": 17
                        },
                        "pc": 215,
                        "value": "cast(0, felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.assert_only_self.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.assert_only_self.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 23,
                            "offset": 0
                        },
                        "pc": 209,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 23,
                            "offset": 16
                        },
                        "pc": 213,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.assert_only_self_encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "__wrappers__.constructor": {
                "decorators": [
                    "constructor"
                ],
                "pc": 289,
                "type": "function"
            },
            "__wrappers__.constructor.Args": {
                "full_name": "__wrappers__.constructor.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.constructor.ImplicitArgs": {
                "full_name": "__wrappers__.constructor.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.constructor.Return": {
                "cairo_type": "(syscall_ptr: felt*, pedersen_ptr: starkware.cairo.common.cairo_builtins.HashBuiltin*, range_check_ptr: felt, ecdsa_ptr: felt, size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.constructor.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.constructor.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.constructor.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 0
                        },
                        "pc": 289,
                        "value": "cast([fp + (-3)] + 1 - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor.__calldata_arg__public_key": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.constructor.__calldata_arg__public_key",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 0
                        },
                        "pc": 289,
                        "value": "[cast([fp + (-3)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.constructor.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 0
                        },
                        "pc": 289,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 0
                        },
                        "pc": 289,
                        "value": "cast([fp + (-3)] + 1, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor.__temp15": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.constructor.__temp15",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 1
                        },
                        "pc": 291,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor.__wrapped_func": {
                "destination": "__main__.constructor",
                "type": "alias"
            },
            "__wrappers__.constructor.ecdsa_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.constructor.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 0
                        },
                        "pc": 289,
                        "value": "[cast([fp + (-5)] + 3, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__wrappers__.constructor.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 0
                        },
                        "pc": 289,
                        "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 29
                        },
                        "pc": 298,
                        "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.constructor.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 0
                        },
                        "pc": 289,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 29
                        },
                        "pc": 298,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor.ret_value": {
                "cairo_type": "()",
                "full_name": "__wrappers__.constructor.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 29
                        },
                        "pc": 298,
                        "value": "[cast(ap + 0, ()*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.constructor.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 30
                        },
                        "pc": 300,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.constructor.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 30
                        },
                        "pc": 300,
                        "value": "cast(0, felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.constructor.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 0
                        },
                        "pc": 289,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 30,
                            "offset": 29
                        },
                        "pc": 298,
                        "value": "[cast(ap + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.constructor_encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "__wrappers__.deploy_contract": {
                "decorators": [
                    "external"
                ],
                "pc": 545,
                "type": "function"
            },
            "__wrappers__.deploy_contract.Args": {
                "full_name": "__wrappers__.deploy_contract.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.deploy_contract.ImplicitArgs": {
                "full_name": "__wrappers__.deploy_contract.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.deploy_contract.Return": {
                "cairo_type": "(syscall_ptr: felt*, pedersen_ptr: felt, range_check_ptr: felt, ecdsa_ptr: felt, size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.deploy_contract.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.deploy_contract.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 5
                        },
                        "pc": 552,
                        "value": "cast([ap + (-1)] + 1 - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__calldata_arg_class_hash": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__calldata_arg_class_hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "[cast([fp + (-3)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__calldata_arg_constructor_calldata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.deploy_contract.__calldata_arg_constructor_calldata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 2
                        },
                        "pc": 548,
                        "value": "cast([fp + (-3)] + 3, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__calldata_arg_constructor_calldata_len": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__calldata_arg_constructor_calldata_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "[cast([fp + (-3)] + 2, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__calldata_arg_contract_address_salt": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__calldata_arg_contract_address_salt",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "[cast([fp + (-3)] + 1, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__calldata_arg_deploy_from_zero": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__calldata_arg_deploy_from_zero",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 5
                        },
                        "pc": 552,
                        "value": "[cast([ap + (-1)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.deploy_contract.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "cast([fp + (-3)] + 1, felt*)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "cast([fp + (-3)] + 2, felt*)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "cast([fp + (-3)] + 3, felt*)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 5
                        },
                        "pc": 552,
                        "value": "[cast(ap + (-1), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 5
                        },
                        "pc": 552,
                        "value": "cast([ap + (-1)] + 1, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__temp43": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__temp43",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 1
                        },
                        "pc": 546,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__temp44": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__temp44",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 2
                        },
                        "pc": 547,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__temp45": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__temp45",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 3
                        },
                        "pc": 550,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__temp46": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__temp46",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 4
                        },
                        "pc": 551,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__temp47": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__temp47",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 6
                        },
                        "pc": 554,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__temp48": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.__temp48",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 41
                        },
                        "pc": 565,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.__wrapped_func": {
                "destination": "__main__.deploy_contract",
                "type": "alias"
            },
            "__wrappers__.deploy_contract.ecdsa_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "[cast([fp + (-5)] + 3, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.pedersen_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "[cast([fp + (-5)] + 1, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 2
                        },
                        "pc": 548,
                        "value": "cast([[fp + (-5)] + 2] + 1, felt)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 50
                        },
                        "pc": 570,
                        "value": "[cast(ap + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.ret_value": {
                "cairo_type": "(contract_address: felt)",
                "full_name": "__wrappers__.deploy_contract.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 40
                        },
                        "pc": 564,
                        "value": "[cast(ap + (-1), (contract_address: felt)*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.deploy_contract.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 50
                        },
                        "pc": 570,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 50
                        },
                        "pc": 570,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.deploy_contract.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 0
                        },
                        "pc": 545,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 44,
                            "offset": 40
                        },
                        "pc": 564,
                        "value": "[cast(ap + (-2), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract_encode_return": {
                "decorators": [],
                "pc": 536,
                "type": "function"
            },
            "__wrappers__.deploy_contract_encode_return.Args": {
                "full_name": "__wrappers__.deploy_contract_encode_return.Args",
                "members": {
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "ret_value": {
                        "cairo_type": "(contract_address: felt)",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "__wrappers__.deploy_contract_encode_return.ImplicitArgs": {
                "full_name": "__wrappers__.deploy_contract_encode_return.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.deploy_contract_encode_return.Return": {
                "cairo_type": "(range_check_ptr: felt, data_len: felt, data: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.deploy_contract_encode_return.SIZEOF_LOCALS": {
                "type": "const",
                "value": 1
            },
            "__wrappers__.deploy_contract_encode_return.__return_value_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.deploy_contract_encode_return.__return_value_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 43,
                            "offset": 1
                        },
                        "pc": 538,
                        "value": "[cast(fp, felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 43,
                            "offset": 1
                        },
                        "pc": 539,
                        "value": "cast([fp] + 1, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract_encode_return.__return_value_ptr_start": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.deploy_contract_encode_return.__return_value_ptr_start",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 43,
                            "offset": 1
                        },
                        "pc": 538,
                        "value": "[cast(fp, felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract_encode_return.__temp42": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract_encode_return.__temp42",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 43,
                            "offset": 2
                        },
                        "pc": 541,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract_encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "__wrappers__.deploy_contract_encode_return.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.deploy_contract_encode_return.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 43,
                            "offset": 0
                        },
                        "pc": 536,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.deploy_contract_encode_return.ret_value": {
                "cairo_type": "(contract_address: felt)",
                "full_name": "__wrappers__.deploy_contract_encode_return.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 43,
                            "offset": 0
                        },
                        "pc": 536,
                        "value": "[cast(fp + (-4), (contract_address: felt)*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key": {
                "decorators": [
                    "view"
                ],
                "pc": 238,
                "type": "function"
            },
            "__wrappers__.get_public_key.Args": {
                "full_name": "__wrappers__.get_public_key.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.get_public_key.ImplicitArgs": {
                "full_name": "__wrappers__.get_public_key.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.get_public_key.Return": {
                "cairo_type": "(syscall_ptr: felt*, pedersen_ptr: starkware.cairo.common.cairo_builtins.HashBuiltin*, range_check_ptr: felt, ecdsa_ptr: felt, size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.get_public_key.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.get_public_key.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_public_key.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 0
                        },
                        "pc": 238,
                        "value": "cast([fp + (-3)] - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.get_public_key.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 0
                        },
                        "pc": 238,
                        "value": "[cast(fp + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key.__wrapped_func": {
                "destination": "__main__.get_public_key",
                "type": "alias"
            },
            "__wrappers__.get_public_key.ecdsa_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_public_key.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 0
                        },
                        "pc": 238,
                        "value": "[cast([fp + (-5)] + 3, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__wrappers__.get_public_key.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 0
                        },
                        "pc": 238,
                        "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 28
                        },
                        "pc": 244,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_public_key.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 0
                        },
                        "pc": 238,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 28
                        },
                        "pc": 244,
                        "value": "[cast(ap + (-2), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 36
                        },
                        "pc": 247,
                        "value": "[cast(ap + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key.ret_value": {
                "cairo_type": "(res: felt)",
                "full_name": "__wrappers__.get_public_key.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 28
                        },
                        "pc": 244,
                        "value": "[cast(ap + (-1), (res: felt)*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.get_public_key.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 36
                        },
                        "pc": 247,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_public_key.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 36
                        },
                        "pc": 247,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.get_public_key.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 0
                        },
                        "pc": 238,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 26,
                            "offset": 28
                        },
                        "pc": 244,
                        "value": "[cast(ap + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key_encode_return": {
                "decorators": [],
                "pc": 229,
                "type": "function"
            },
            "__wrappers__.get_public_key_encode_return.Args": {
                "full_name": "__wrappers__.get_public_key_encode_return.Args",
                "members": {
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "ret_value": {
                        "cairo_type": "(res: felt)",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "__wrappers__.get_public_key_encode_return.ImplicitArgs": {
                "full_name": "__wrappers__.get_public_key_encode_return.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.get_public_key_encode_return.Return": {
                "cairo_type": "(range_check_ptr: felt, data_len: felt, data: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.get_public_key_encode_return.SIZEOF_LOCALS": {
                "type": "const",
                "value": 1
            },
            "__wrappers__.get_public_key_encode_return.__return_value_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.get_public_key_encode_return.__return_value_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 25,
                            "offset": 1
                        },
                        "pc": 231,
                        "value": "[cast(fp, felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 25,
                            "offset": 1
                        },
                        "pc": 232,
                        "value": "cast([fp] + 1, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key_encode_return.__return_value_ptr_start": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.get_public_key_encode_return.__return_value_ptr_start",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 25,
                            "offset": 1
                        },
                        "pc": 231,
                        "value": "[cast(fp, felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key_encode_return.__temp13": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_public_key_encode_return.__temp13",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 25,
                            "offset": 2
                        },
                        "pc": 234,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key_encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "__wrappers__.get_public_key_encode_return.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_public_key_encode_return.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 25,
                            "offset": 0
                        },
                        "pc": 229,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_public_key_encode_return.ret_value": {
                "cairo_type": "(res: felt)",
                "full_name": "__wrappers__.get_public_key_encode_return.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 25,
                            "offset": 0
                        },
                        "pc": 229,
                        "value": "[cast(fp + (-4), (res: felt)*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature": {
                "decorators": [
                    "view"
                ],
                "pc": 327,
                "type": "function"
            },
            "__wrappers__.is_valid_signature.Args": {
                "full_name": "__wrappers__.is_valid_signature.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.is_valid_signature.ImplicitArgs": {
                "full_name": "__wrappers__.is_valid_signature.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.is_valid_signature.Return": {
                "cairo_type": "(syscall_ptr: felt*, pedersen_ptr: starkware.cairo.common.cairo_builtins.HashBuiltin*, range_check_ptr: felt, ecdsa_ptr: starkware.cairo.common.cairo_builtins.SignatureBuiltin*, size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.is_valid_signature.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.is_valid_signature.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.is_valid_signature.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 5
                        },
                        "pc": 334,
                        "value": "cast([ap + (-1)] - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.__calldata_arg_hash": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.is_valid_signature.__calldata_arg_hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 0
                        },
                        "pc": 327,
                        "value": "[cast([fp + (-3)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.__calldata_arg_signature": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.is_valid_signature.__calldata_arg_signature",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 2
                        },
                        "pc": 330,
                        "value": "cast([fp + (-3)] + 2, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.__calldata_arg_signature_len": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.is_valid_signature.__calldata_arg_signature_len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 0
                        },
                        "pc": 327,
                        "value": "[cast([fp + (-3)] + 1, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.is_valid_signature.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 0
                        },
                        "pc": 327,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 0
                        },
                        "pc": 327,
                        "value": "cast([fp + (-3)] + 1, felt*)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 0
                        },
                        "pc": 327,
                        "value": "cast([fp + (-3)] + 2, felt*)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 5
                        },
                        "pc": 334,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.__temp16": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.is_valid_signature.__temp16",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 1
                        },
                        "pc": 328,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.__temp17": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.is_valid_signature.__temp17",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 2
                        },
                        "pc": 329,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.__temp18": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.is_valid_signature.__temp18",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 3
                        },
                        "pc": 332,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.__temp19": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.is_valid_signature.__temp19",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 4
                        },
                        "pc": 333,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.__temp20": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.is_valid_signature.__temp20",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 6
                        },
                        "pc": 336,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.__wrapped_func": {
                "destination": "__main__.is_valid_signature",
                "type": "alias"
            },
            "__wrappers__.is_valid_signature.ecdsa_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                "full_name": "__wrappers__.is_valid_signature.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 0
                        },
                        "pc": 327,
                        "value": "[cast([fp + (-5)] + 3, starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 50
                        },
                        "pc": 347,
                        "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__wrappers__.is_valid_signature.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 0
                        },
                        "pc": 327,
                        "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 50
                        },
                        "pc": 347,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.is_valid_signature.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 0
                        },
                        "pc": 327,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 2
                        },
                        "pc": 330,
                        "value": "cast([[fp + (-5)] + 2] + 1, felt)"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 50
                        },
                        "pc": 347,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.ret_value": {
                "cairo_type": "()",
                "full_name": "__wrappers__.is_valid_signature.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 50
                        },
                        "pc": 347,
                        "value": "[cast(ap + 0, ()*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.is_valid_signature.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 51
                        },
                        "pc": 349,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.is_valid_signature.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 51
                        },
                        "pc": 349,
                        "value": "cast(0, felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.is_valid_signature.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 0
                        },
                        "pc": 327,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 32,
                            "offset": 50
                        },
                        "pc": 347,
                        "value": "[cast(ap + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.is_valid_signature_encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "__wrappers__.set_public_key": {
                "decorators": [
                    "external"
                ],
                "pc": 263,
                "type": "function"
            },
            "__wrappers__.set_public_key.Args": {
                "full_name": "__wrappers__.set_public_key.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.set_public_key.ImplicitArgs": {
                "full_name": "__wrappers__.set_public_key.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.set_public_key.Return": {
                "cairo_type": "(syscall_ptr: felt*, pedersen_ptr: starkware.cairo.common.cairo_builtins.HashBuiltin*, range_check_ptr: felt, ecdsa_ptr: felt, size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "__wrappers__.set_public_key.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.set_public_key.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.set_public_key.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 0
                        },
                        "pc": 263,
                        "value": "cast([fp + (-3)] + 1 - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key.__calldata_arg_new_public_key": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.set_public_key.__calldata_arg_new_public_key",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 0
                        },
                        "pc": 263,
                        "value": "[cast([fp + (-3)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.set_public_key.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 0
                        },
                        "pc": 263,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 0
                        },
                        "pc": 263,
                        "value": "cast([fp + (-3)] + 1, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key.__temp14": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.set_public_key.__temp14",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 1
                        },
                        "pc": 265,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key.__wrapped_func": {
                "destination": "__main__.set_public_key",
                "type": "alias"
            },
            "__wrappers__.set_public_key.ecdsa_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.set_public_key.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 0
                        },
                        "pc": 263,
                        "value": "[cast([fp + (-5)] + 3, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__wrappers__.set_public_key.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 0
                        },
                        "pc": 263,
                        "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 44
                        },
                        "pc": 272,
                        "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.set_public_key.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 0
                        },
                        "pc": 263,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 44
                        },
                        "pc": 272,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key.ret_value": {
                "cairo_type": "()",
                "full_name": "__wrappers__.set_public_key.ret_value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 44
                        },
                        "pc": 272,
                        "value": "[cast(ap + 0, ()*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.set_public_key.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 45
                        },
                        "pc": 274,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.set_public_key.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 45
                        },
                        "pc": 274,
                        "value": "cast(0, felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.set_public_key.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 0
                        },
                        "pc": 263,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 28,
                            "offset": 44
                        },
                        "pc": 272,
                        "value": "[cast(ap + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.set_public_key_encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "starkware.cairo.common.alloc.alloc": {
                "decorators": [],
                "pc": 0,
                "type": "function"
            },
            "starkware.cairo.common.alloc.alloc.Args": {
                "full_name": "starkware.cairo.common.alloc.alloc.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.cairo.common.alloc.alloc.ImplicitArgs": {
                "full_name": "starkware.cairo.common.alloc.alloc.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.cairo.common.alloc.alloc.Return": {
                "cairo_type": "(ptr: felt*)",
                "type": "type_definition"
            },
            "starkware.cairo.common.alloc.alloc.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.cairo.common.bool.FALSE": {
                "type": "const",
                "value": 0
            },
            "starkware.cairo.common.bool.TRUE": {
                "type": "const",
                "value": 1
            },
            "starkware.cairo.common.cairo_builtins.BitwiseBuiltin": {
                "full_name": "starkware.cairo.common.cairo_builtins.BitwiseBuiltin",
                "members": {
                    "x": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "x_and_y": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "x_or_y": {
                        "cairo_type": "felt",
                        "offset": 4
                    },
                    "x_xor_y": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "y": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "starkware.cairo.common.cairo_builtins.EcOpBuiltin": {
                "full_name": "starkware.cairo.common.cairo_builtins.EcOpBuiltin",
                "members": {
                    "m": {
                        "cairo_type": "felt",
                        "offset": 4
                    },
                    "p": {
                        "cairo_type": "starkware.cairo.common.ec_point.EcPoint",
                        "offset": 0
                    },
                    "q": {
                        "cairo_type": "starkware.cairo.common.ec_point.EcPoint",
                        "offset": 2
                    },
                    "r": {
                        "cairo_type": "starkware.cairo.common.ec_point.EcPoint",
                        "offset": 5
                    }
                },
                "size": 7,
                "type": "struct"
            },
            "starkware.cairo.common.cairo_builtins.EcPoint": {
                "destination": "starkware.cairo.common.ec_point.EcPoint",
                "type": "alias"
            },
            "starkware.cairo.common.cairo_builtins.HashBuiltin": {
                "full_name": "starkware.cairo.common.cairo_builtins.HashBuiltin",
                "members": {
                    "result": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "x": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "y": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.cairo.common.cairo_builtins.KeccakBuiltin": {
                "full_name": "starkware.cairo.common.cairo_builtins.KeccakBuiltin",
                "members": {
                    "input": {
                        "cairo_type": "starkware.cairo.common.keccak_state.KeccakBuiltinState",
                        "offset": 0
                    },
                    "output": {
                        "cairo_type": "starkware.cairo.common.keccak_state.KeccakBuiltinState",
                        "offset": 8
                    }
                },
                "size": 16,
                "type": "struct"
            },
            "starkware.cairo.common.cairo_builtins.KeccakBuiltinState": {
                "destination": "starkware.cairo.common.keccak_state.KeccakBuiltinState",
                "type": "alias"
            },
            "starkware.cairo.common.cairo_builtins.SignatureBuiltin": {
                "full_name": "starkware.cairo.common.cairo_builtins.SignatureBuiltin",
                "members": {
                    "message": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "pub_key": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.cairo.common.dict_access.DictAccess": {
                "full_name": "starkware.cairo.common.dict_access.DictAccess",
                "members": {
                    "key": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "new_value": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "prev_value": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.cairo.common.ec.EcOpBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.EcOpBuiltin",
                "type": "alias"
            },
            "starkware.cairo.common.ec.EcPoint": {
                "destination": "starkware.cairo.common.ec_point.EcPoint",
                "type": "alias"
            },
            "starkware.cairo.common.ec.StarkCurve": {
                "type": "namespace"
            },
            "starkware.cairo.common.ec.StarkCurve.ALPHA": {
                "type": "const",
                "value": 1
            },
            "starkware.cairo.common.ec.StarkCurve.Args": {
                "full_name": "starkware.cairo.common.ec.StarkCurve.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.cairo.common.ec.StarkCurve.BETA": {
                "type": "const",
                "value": -476910135076337975234679399815567221425937815956490878998147463828055613816
            },
            "starkware.cairo.common.ec.StarkCurve.GEN_X": {
                "type": "const",
                "value": 874739451078007766457464989774322083649278607533249481151382481072868806602
            },
            "starkware.cairo.common.ec.StarkCurve.GEN_Y": {
                "type": "const",
                "value": 152666792071518830868575557812948353041420400780739481342941381225525861407
            },
            "starkware.cairo.common.ec.StarkCurve.ImplicitArgs": {
                "full_name": "starkware.cairo.common.ec.StarkCurve.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.cairo.common.ec.StarkCurve.ORDER": {
                "type": "const",
                "value": -96363463615509210819012598251359154898
            },
            "starkware.cairo.common.ec.StarkCurve.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "starkware.cairo.common.ec.StarkCurve.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.cairo.common.ec.is_quad_residue": {
                "destination": "starkware.cairo.common.math.is_quad_residue",
                "type": "alias"
            },
            "starkware.cairo.common.ec_point.EcPoint": {
                "full_name": "starkware.cairo.common.ec_point.EcPoint",
                "members": {
                    "x": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "y": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.cairo.common.hash.HashBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.HashBuiltin",
                "type": "alias"
            },
            "starkware.cairo.common.hash.hash2": {
                "decorators": [],
                "pc": 3,
                "type": "function"
            },
            "starkware.cairo.common.hash.hash2.Args": {
                "full_name": "starkware.cairo.common.hash.hash2.Args",
                "members": {
                    "x": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "y": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.cairo.common.hash.hash2.ImplicitArgs": {
                "full_name": "starkware.cairo.common.hash.hash2.ImplicitArgs",
                "members": {
                    "hash_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.cairo.common.hash.hash2.Return": {
                "cairo_type": "(result: felt)",
                "type": "type_definition"
            },
            "starkware.cairo.common.hash.hash2.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.cairo.common.hash.hash2.hash_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "starkware.cairo.common.hash.hash2.hash_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 1,
                            "offset": 0
                        },
                        "pc": 3,
                        "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 1,
                            "offset": 0
                        },
                        "pc": 5,
                        "value": "cast([fp + (-5)] + 3, starkware.cairo.common.cairo_builtins.HashBuiltin*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash.hash2.result": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash.hash2.result",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 1,
                            "offset": 0
                        },
                        "pc": 5,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash.hash2.x": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash.hash2.x",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 1,
                            "offset": 0
                        },
                        "pc": 3,
                        "value": "[cast(fp + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash.hash2.y": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash.hash2.y",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 1,
                            "offset": 0
                        },
                        "pc": 3,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.HashBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.HashBuiltin",
                "type": "alias"
            },
            "starkware.cairo.common.hash_state.HashState": {
                "full_name": "starkware.cairo.common.hash_state.HashState",
                "members": {
                    "current_hash": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "n_words": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.get_fp_and_pc": {
                "destination": "starkware.cairo.common.registers.get_fp_and_pc",
                "type": "alias"
            },
            "starkware.cairo.common.hash_state.hash2": {
                "destination": "starkware.cairo.common.hash.hash2",
                "type": "alias"
            },
            "starkware.cairo.common.hash_state.hash_finalize": {
                "decorators": [],
                "pc": 134,
                "type": "function"
            },
            "starkware.cairo.common.hash_state.hash_finalize.Args": {
                "full_name": "starkware.cairo.common.hash_state.hash_finalize.Args",
                "members": {
                    "hash_state_ptr": {
                        "cairo_type": "starkware.cairo.common.hash_state.HashState*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_finalize.ImplicitArgs": {
                "full_name": "starkware.cairo.common.hash_state.hash_finalize.ImplicitArgs",
                "members": {
                    "hash_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_finalize.Return": {
                "cairo_type": "(hash: felt)",
                "type": "type_definition"
            },
            "starkware.cairo.common.hash_state.hash_finalize.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.cairo.common.hash_state.hash_finalize.hash": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_finalize.hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 16,
                            "offset": 7
                        },
                        "pc": 139,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_finalize.hash_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "starkware.cairo.common.hash_state.hash_finalize.hash_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 16,
                            "offset": 0
                        },
                        "pc": 134,
                        "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 16,
                            "offset": 7
                        },
                        "pc": 139,
                        "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_finalize.hash_state_ptr": {
                "cairo_type": "starkware.cairo.common.hash_state.HashState*",
                "full_name": "starkware.cairo.common.hash_state.hash_finalize.hash_state_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 16,
                            "offset": 0
                        },
                        "pc": 134,
                        "value": "[cast(fp + (-3), starkware.cairo.common.hash_state.HashState**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_init": {
                "decorators": [],
                "pc": 92,
                "type": "function"
            },
            "starkware.cairo.common.hash_state.hash_init.Args": {
                "full_name": "starkware.cairo.common.hash_state.hash_init.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_init.ImplicitArgs": {
                "full_name": "starkware.cairo.common.hash_state.hash_init.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_init.Return": {
                "cairo_type": "(hash_state_ptr: starkware.cairo.common.hash_state.HashState*)",
                "type": "type_definition"
            },
            "starkware.cairo.common.hash_state.hash_init.SIZEOF_LOCALS": {
                "type": "const",
                "value": 2
            },
            "starkware.cairo.common.hash_state.hash_init.__fp__": {
                "cairo_type": "felt*",
                "full_name": "starkware.cairo.common.hash_state.hash_init.__fp__",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 12,
                            "offset": 4
                        },
                        "pc": 96,
                        "value": "[cast(ap + (-2), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_init.hash_state": {
                "cairo_type": "starkware.cairo.common.hash_state.HashState",
                "full_name": "starkware.cairo.common.hash_state.hash_init.hash_state",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 12,
                            "offset": 4
                        },
                        "pc": 96,
                        "value": "[cast(fp, starkware.cairo.common.hash_state.HashState*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update": {
                "decorators": [],
                "pc": 102,
                "type": "function"
            },
            "starkware.cairo.common.hash_state.hash_update.Args": {
                "full_name": "starkware.cairo.common.hash_state.hash_update.Args",
                "members": {
                    "data_length": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "data_ptr": {
                        "cairo_type": "felt*",
                        "offset": 1
                    },
                    "hash_state_ptr": {
                        "cairo_type": "starkware.cairo.common.hash_state.HashState*",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_update.ImplicitArgs": {
                "full_name": "starkware.cairo.common.hash_state.hash_update.ImplicitArgs",
                "members": {
                    "hash_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_update.Return": {
                "cairo_type": "(new_hash_state_ptr: starkware.cairo.common.hash_state.HashState*)",
                "type": "type_definition"
            },
            "starkware.cairo.common.hash_state.hash_update.SIZEOF_LOCALS": {
                "type": "const",
                "value": 2
            },
            "starkware.cairo.common.hash_state.hash_update.__fp__": {
                "cairo_type": "felt*",
                "full_name": "starkware.cairo.common.hash_state.hash_update.__fp__",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 14,
                            "offset": 2
                        },
                        "pc": 112,
                        "value": "[cast(ap + (-2), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update.__temp9": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update.__temp9",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 14,
                            "offset": 3
                        },
                        "pc": 114,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update.data_length": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update.data_length",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 13,
                            "offset": 0
                        },
                        "pc": 102,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update.data_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.cairo.common.hash_state.hash_update.data_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 13,
                            "offset": 0
                        },
                        "pc": 102,
                        "value": "[cast(fp + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update.hash": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update.hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 14,
                            "offset": 0
                        },
                        "pc": 110,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update.hash_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "starkware.cairo.common.hash_state.hash_update.hash_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 13,
                            "offset": 0
                        },
                        "pc": 102,
                        "value": "[cast(fp + (-6), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 14,
                            "offset": 0
                        },
                        "pc": 110,
                        "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update.hash_state_ptr": {
                "cairo_type": "starkware.cairo.common.hash_state.HashState*",
                "full_name": "starkware.cairo.common.hash_state.hash_update.hash_state_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 13,
                            "offset": 0
                        },
                        "pc": 102,
                        "value": "[cast(fp + (-5), starkware.cairo.common.hash_state.HashState**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update.new_hash_state": {
                "cairo_type": "starkware.cairo.common.hash_state.HashState",
                "full_name": "starkware.cairo.common.hash_state.hash_update.new_hash_state",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 14,
                            "offset": 2
                        },
                        "pc": 112,
                        "value": "[cast(fp, starkware.cairo.common.hash_state.HashState*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner": {
                "decorators": [],
                "pc": 140,
                "type": "function"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.Args": {
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.Args",
                "members": {
                    "data_length": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "data_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    },
                    "hash": {
                        "cairo_type": "felt",
                        "offset": 2
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.ImplicitArgs": {
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.ImplicitArgs",
                "members": {
                    "hash_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.LoopLocals": {
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.LoopLocals",
                "members": {
                    "cur_hash": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "data_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    },
                    "hash_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.Return": {
                "cairo_type": "(hash: felt)",
                "type": "type_definition"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.SIZEOF_LOCALS": {
                "type": "const",
                "value": 1
            },
            "starkware.cairo.common.hash_state.hash_update_inner.__temp11": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.__temp11",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 2
                        },
                        "pc": 149,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.__temp12": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.__temp12",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 7
                        },
                        "pc": 156,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.data_last_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.data_last_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 2
                        },
                        "pc": 150,
                        "value": "[cast(fp, felt**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.data_length": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.data_length",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 0
                        },
                        "pc": 140,
                        "value": "[cast(fp + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.data_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.data_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 0
                        },
                        "pc": 140,
                        "value": "[cast(fp + (-5), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.final_locals": {
                "cairo_type": "starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.final_locals",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 10
                        },
                        "pc": 164,
                        "value": "cast(ap + (-3), starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.first_locals": {
                "cairo_type": "starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.first_locals",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 2
                        },
                        "pc": 150,
                        "value": "cast(ap, starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.hash": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 0
                        },
                        "pc": 140,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.hash_loop": {
                "pc": 153,
                "type": "label"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.hash_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.hash_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 0
                        },
                        "pc": 140,
                        "value": "[cast(fp + (-6), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 10
                        },
                        "pc": 164,
                        "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.n_remaining_elements": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.n_remaining_elements",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 6
                        },
                        "pc": 154,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.next_locals": {
                "cairo_type": "starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.next_locals",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 7
                        },
                        "pc": 157,
                        "value": "cast(ap, starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_inner.prev_locals": {
                "cairo_type": "starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*",
                "full_name": "starkware.cairo.common.hash_state.hash_update_inner.prev_locals",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 17,
                            "offset": 5
                        },
                        "pc": 153,
                        "value": "cast(ap + (-3), starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_single": {
                "decorators": [],
                "pc": 118,
                "type": "function"
            },
            "starkware.cairo.common.hash_state.hash_update_single.Args": {
                "full_name": "starkware.cairo.common.hash_state.hash_update_single.Args",
                "members": {
                    "hash_state_ptr": {
                        "cairo_type": "starkware.cairo.common.hash_state.HashState*",
                        "offset": 0
                    },
                    "item": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_update_single.ImplicitArgs": {
                "full_name": "starkware.cairo.common.hash_state.hash_update_single.ImplicitArgs",
                "members": {
                    "hash_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.cairo.common.hash_state.hash_update_single.Return": {
                "cairo_type": "(new_hash_state_ptr: starkware.cairo.common.hash_state.HashState*)",
                "type": "type_definition"
            },
            "starkware.cairo.common.hash_state.hash_update_single.SIZEOF_LOCALS": {
                "type": "const",
                "value": 2
            },
            "starkware.cairo.common.hash_state.hash_update_single.__fp__": {
                "cairo_type": "felt*",
                "full_name": "starkware.cairo.common.hash_state.hash_update_single.__fp__",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 15,
                            "offset": 11
                        },
                        "pc": 127,
                        "value": "[cast(ap + (-2), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_single.__temp10": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update_single.__temp10",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 15,
                            "offset": 12
                        },
                        "pc": 129,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_single.hash": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update_single.hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 15,
                            "offset": 9
                        },
                        "pc": 125,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_single.hash_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "starkware.cairo.common.hash_state.hash_update_single.hash_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 15,
                            "offset": 0
                        },
                        "pc": 118,
                        "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 15,
                            "offset": 9
                        },
                        "pc": 125,
                        "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_single.hash_state_ptr": {
                "cairo_type": "starkware.cairo.common.hash_state.HashState*",
                "full_name": "starkware.cairo.common.hash_state.hash_update_single.hash_state_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 15,
                            "offset": 0
                        },
                        "pc": 118,
                        "value": "[cast(fp + (-4), starkware.cairo.common.hash_state.HashState**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_single.item": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.hash_state.hash_update_single.item",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 15,
                            "offset": 0
                        },
                        "pc": 118,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.hash_state.hash_update_single.new_hash_state": {
                "cairo_type": "starkware.cairo.common.hash_state.HashState",
                "full_name": "starkware.cairo.common.hash_state.hash_update_single.new_hash_state",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 15,
                            "offset": 11
                        },
                        "pc": 127,
                        "value": "[cast(fp, starkware.cairo.common.hash_state.HashState*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.keccak_state.KeccakBuiltinState": {
                "full_name": "starkware.cairo.common.keccak_state.KeccakBuiltinState",
                "members": {
                    "s0": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "s1": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "s2": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "s3": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "s4": {
                        "cairo_type": "felt",
                        "offset": 4
                    },
                    "s5": {
                        "cairo_type": "felt",
                        "offset": 5
                    },
                    "s6": {
                        "cairo_type": "felt",
                        "offset": 6
                    },
                    "s7": {
                        "cairo_type": "felt",
                        "offset": 7
                    }
                },
                "size": 8,
                "type": "struct"
            },
            "starkware.cairo.common.math.FALSE": {
                "destination": "starkware.cairo.common.bool.FALSE",
                "type": "alias"
            },
            "starkware.cairo.common.math.TRUE": {
                "destination": "starkware.cairo.common.bool.TRUE",
                "type": "alias"
            },
            "starkware.cairo.common.math.assert_not_equal": {
                "decorators": [],
                "pc": 25,
                "type": "function"
            },
            "starkware.cairo.common.math.assert_not_equal.Args": {
                "full_name": "starkware.cairo.common.math.assert_not_equal.Args",
                "members": {
                    "a": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "b": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.cairo.common.math.assert_not_equal.ImplicitArgs": {
                "full_name": "starkware.cairo.common.math.assert_not_equal.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.cairo.common.math.assert_not_equal.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "starkware.cairo.common.math.assert_not_equal.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.cairo.common.math.assert_not_equal.__temp1": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.math.assert_not_equal.__temp1",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 1
                        },
                        "pc": 26,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.math.assert_not_equal.a": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.math.assert_not_equal.a",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 0
                        },
                        "pc": 25,
                        "value": "[cast(fp + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.math.assert_not_equal.b": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.math.assert_not_equal.b",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 0
                        },
                        "pc": 25,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.memcpy.memcpy": {
                "decorators": [],
                "pc": 9,
                "type": "function"
            },
            "starkware.cairo.common.memcpy.memcpy.Args": {
                "full_name": "starkware.cairo.common.memcpy.memcpy.Args",
                "members": {
                    "dst": {
                        "cairo_type": "felt*",
                        "offset": 0
                    },
                    "len": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "src": {
                        "cairo_type": "felt*",
                        "offset": 1
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.cairo.common.memcpy.memcpy.ImplicitArgs": {
                "full_name": "starkware.cairo.common.memcpy.memcpy.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.cairo.common.memcpy.memcpy.LoopFrame": {
                "full_name": "starkware.cairo.common.memcpy.memcpy.LoopFrame",
                "members": {
                    "dst": {
                        "cairo_type": "felt*",
                        "offset": 0
                    },
                    "src": {
                        "cairo_type": "felt*",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.cairo.common.memcpy.memcpy.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "starkware.cairo.common.memcpy.memcpy.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.cairo.common.memcpy.memcpy.__temp0": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.memcpy.memcpy.__temp0",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 3
                        },
                        "pc": 15,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.memcpy.memcpy.continue_copying": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.memcpy.memcpy.continue_copying",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 3
                        },
                        "pc": 16,
                        "value": "[cast(ap, felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.memcpy.memcpy.dst": {
                "cairo_type": "felt*",
                "full_name": "starkware.cairo.common.memcpy.memcpy.dst",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 0
                        },
                        "pc": 9,
                        "value": "[cast(fp + (-5), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.memcpy.memcpy.frame": {
                "cairo_type": "starkware.cairo.common.memcpy.memcpy.LoopFrame",
                "full_name": "starkware.cairo.common.memcpy.memcpy.frame",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 2
                        },
                        "pc": 14,
                        "value": "[cast(ap + (-2), starkware.cairo.common.memcpy.memcpy.LoopFrame*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 2
                        },
                        "pc": 14,
                        "value": "[cast(ap + (-2), starkware.cairo.common.memcpy.memcpy.LoopFrame*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.memcpy.memcpy.len": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.memcpy.memcpy.len",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 0
                        },
                        "pc": 9,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.memcpy.memcpy.loop": {
                "pc": 14,
                "type": "label"
            },
            "starkware.cairo.common.memcpy.memcpy.next_frame": {
                "cairo_type": "starkware.cairo.common.memcpy.memcpy.LoopFrame*",
                "full_name": "starkware.cairo.common.memcpy.memcpy.next_frame",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 3
                        },
                        "pc": 16,
                        "value": "cast(ap + 1, starkware.cairo.common.memcpy.memcpy.LoopFrame*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.memcpy.memcpy.src": {
                "cairo_type": "felt*",
                "full_name": "starkware.cairo.common.memcpy.memcpy.src",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 0
                        },
                        "pc": 9,
                        "value": "[cast(fp + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.registers.get_ap": {
                "destination": "starkware.cairo.lang.compiler.lib.registers.get_ap",
                "type": "alias"
            },
            "starkware.cairo.common.registers.get_fp_and_pc": {
                "destination": "starkware.cairo.lang.compiler.lib.registers.get_fp_and_pc",
                "type": "alias"
            },
            "starkware.cairo.common.signature.EcOpBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.EcOpBuiltin",
                "type": "alias"
            },
            "starkware.cairo.common.signature.EcPoint": {
                "destination": "starkware.cairo.common.ec_point.EcPoint",
                "type": "alias"
            },
            "starkware.cairo.common.signature.FALSE": {
                "destination": "starkware.cairo.common.bool.FALSE",
                "type": "alias"
            },
            "starkware.cairo.common.signature.SignatureBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.SignatureBuiltin",
                "type": "alias"
            },
            "starkware.cairo.common.signature.StarkCurve": {
                "destination": "starkware.cairo.common.ec.StarkCurve",
                "type": "alias"
            },
            "starkware.cairo.common.signature.TRUE": {
                "destination": "starkware.cairo.common.bool.TRUE",
                "type": "alias"
            },
            "starkware.cairo.common.signature.ec_add": {
                "destination": "starkware.cairo.common.ec.ec_add",
                "type": "alias"
            },
            "starkware.cairo.common.signature.ec_mul": {
                "destination": "starkware.cairo.common.ec.ec_mul",
                "type": "alias"
            },
            "starkware.cairo.common.signature.ec_sub": {
                "destination": "starkware.cairo.common.ec.ec_sub",
                "type": "alias"
            },
            "starkware.cairo.common.signature.is_x_on_curve": {
                "destination": "starkware.cairo.common.ec.is_x_on_curve",
                "type": "alias"
            },
            "starkware.cairo.common.signature.recover_y": {
                "destination": "starkware.cairo.common.ec.recover_y",
                "type": "alias"
            },
            "starkware.cairo.common.signature.verify_ecdsa_signature": {
                "decorators": [],
                "pc": 165,
                "type": "function"
            },
            "starkware.cairo.common.signature.verify_ecdsa_signature.Args": {
                "full_name": "starkware.cairo.common.signature.verify_ecdsa_signature.Args",
                "members": {
                    "message": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "public_key": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "signature_r": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "signature_s": {
                        "cairo_type": "felt",
                        "offset": 3
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "starkware.cairo.common.signature.verify_ecdsa_signature.ImplicitArgs": {
                "full_name": "starkware.cairo.common.signature.verify_ecdsa_signature.ImplicitArgs",
                "members": {
                    "ecdsa_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.cairo.common.signature.verify_ecdsa_signature.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "starkware.cairo.common.signature.verify_ecdsa_signature.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.cairo.common.signature.verify_ecdsa_signature.ecdsa_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.SignatureBuiltin*",
                "full_name": "starkware.cairo.common.signature.verify_ecdsa_signature.ecdsa_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 18,
                            "offset": 0
                        },
                        "pc": 165,
                        "value": "[cast(fp + (-7), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 18,
                            "offset": 0
                        },
                        "pc": 167,
                        "value": "cast([fp + (-7)] + 2, starkware.cairo.common.cairo_builtins.SignatureBuiltin*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.signature.verify_ecdsa_signature.message": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.signature.verify_ecdsa_signature.message",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 18,
                            "offset": 0
                        },
                        "pc": 165,
                        "value": "[cast(fp + (-6), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.signature.verify_ecdsa_signature.public_key": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.signature.verify_ecdsa_signature.public_key",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 18,
                            "offset": 0
                        },
                        "pc": 165,
                        "value": "[cast(fp + (-5), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.signature.verify_ecdsa_signature.signature_r": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.signature.verify_ecdsa_signature.signature_r",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 18,
                            "offset": 0
                        },
                        "pc": 165,
                        "value": "[cast(fp + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.common.signature.verify_ecdsa_signature.signature_s": {
                "cairo_type": "felt",
                "full_name": "starkware.cairo.common.signature.verify_ecdsa_signature.signature_s",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 18,
                            "offset": 0
                        },
                        "pc": 165,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.cairo.lang.compiler.lib.registers.get_fp_and_pc": {
                "decorators": [],
                "pc": 24,
                "type": "function"
            },
            "starkware.cairo.lang.compiler.lib.registers.get_fp_and_pc.Args": {
                "full_name": "starkware.cairo.lang.compiler.lib.registers.get_fp_and_pc.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.cairo.lang.compiler.lib.registers.get_fp_and_pc.ImplicitArgs": {
                "full_name": "starkware.cairo.lang.compiler.lib.registers.get_fp_and_pc.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.cairo.lang.compiler.lib.registers.get_fp_and_pc.Return": {
                "cairo_type": "(fp_val: felt*, pc_val: felt*)",
                "type": "type_definition"
            },
            "starkware.cairo.lang.compiler.lib.registers.get_fp_and_pc.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.constants.DECLARE_HASH_PREFIX": {
                "type": "const",
                "value": 28258975365558885
            },
            "starkware.starknet.common.constants.DEPLOY_HASH_PREFIX": {
                "type": "const",
                "value": 110386840629113
            },
            "starkware.starknet.common.constants.INVOKE_HASH_PREFIX": {
                "type": "const",
                "value": 115923154332517
            },
            "starkware.starknet.common.constants.L1_HANDLER_HASH_PREFIX": {
                "type": "const",
                "value": 510926345461491391292786
            },
            "starkware.starknet.common.constants.ORIGIN_ADDRESS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.storage.ADDR_BOUND": {
                "type": "const",
                "value": -106710729501573572985208420194530329073740042555888586719489
            },
            "starkware.starknet.common.storage.MAX_STORAGE_ITEM_SIZE": {
                "type": "const",
                "value": 256
            },
            "starkware.starknet.common.storage.assert_250_bit": {
                "destination": "starkware.cairo.common.math.assert_250_bit",
                "type": "alias"
            },
            "starkware.starknet.common.syscalls.CALL_CONTRACT_SELECTOR": {
                "type": "const",
                "value": 20853273475220472486191784820
            },
            "starkware.starknet.common.syscalls.CallContract": {
                "full_name": "starkware.starknet.common.syscalls.CallContract",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.CallContractRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.CallContractResponse",
                        "offset": 5
                    }
                },
                "size": 7,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.CallContractRequest": {
                "full_name": "starkware.starknet.common.syscalls.CallContractRequest",
                "members": {
                    "calldata": {
                        "cairo_type": "felt*",
                        "offset": 4
                    },
                    "calldata_size": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "contract_address": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "function_selector": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.CallContractResponse": {
                "full_name": "starkware.starknet.common.syscalls.CallContractResponse",
                "members": {
                    "retdata": {
                        "cairo_type": "felt*",
                        "offset": 1
                    },
                    "retdata_size": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.DELEGATE_CALL_SELECTOR": {
                "type": "const",
                "value": 21167594061783206823196716140
            },
            "starkware.starknet.common.syscalls.DELEGATE_L1_HANDLER_SELECTOR": {
                "type": "const",
                "value": 23274015802972845247556842986379118667122
            },
            "starkware.starknet.common.syscalls.DEPLOY_SELECTOR": {
                "type": "const",
                "value": 75202468540281
            },
            "starkware.starknet.common.syscalls.Deploy": {
                "full_name": "starkware.starknet.common.syscalls.Deploy",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.DeployRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.DeployResponse",
                        "offset": 6
                    }
                },
                "size": 9,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.DeployRequest": {
                "full_name": "starkware.starknet.common.syscalls.DeployRequest",
                "members": {
                    "class_hash": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "constructor_calldata": {
                        "cairo_type": "felt*",
                        "offset": 4
                    },
                    "constructor_calldata_size": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "contract_address_salt": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "deploy_from_zero": {
                        "cairo_type": "felt",
                        "offset": 5
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 6,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.DeployResponse": {
                "full_name": "starkware.starknet.common.syscalls.DeployResponse",
                "members": {
                    "constructor_retdata": {
                        "cairo_type": "felt*",
                        "offset": 2
                    },
                    "constructor_retdata_size": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "contract_address": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.DictAccess": {
                "destination": "starkware.cairo.common.dict_access.DictAccess",
                "type": "alias"
            },
            "starkware.starknet.common.syscalls.EMIT_EVENT_SELECTOR": {
                "type": "const",
                "value": 1280709301550335749748
            },
            "starkware.starknet.common.syscalls.EmitEvent": {
                "full_name": "starkware.starknet.common.syscalls.EmitEvent",
                "members": {
                    "data": {
                        "cairo_type": "felt*",
                        "offset": 4
                    },
                    "data_len": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "keys": {
                        "cairo_type": "felt*",
                        "offset": 2
                    },
                    "keys_len": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GET_BLOCK_NUMBER_SELECTOR": {
                "type": "const",
                "value": 1448089106835523001438702345020786
            },
            "starkware.starknet.common.syscalls.GET_BLOCK_TIMESTAMP_SELECTOR": {
                "type": "const",
                "value": 24294903732626645868215235778792757751152
            },
            "starkware.starknet.common.syscalls.GET_CALLER_ADDRESS_SELECTOR": {
                "type": "const",
                "value": 94901967781393078444254803017658102643
            },
            "starkware.starknet.common.syscalls.GET_CONTRACT_ADDRESS_SELECTOR": {
                "type": "const",
                "value": 6219495360805491471215297013070624192820083
            },
            "starkware.starknet.common.syscalls.GET_SEQUENCER_ADDRESS_SELECTOR": {
                "type": "const",
                "value": 1592190833581991703053805829594610833820054387
            },
            "starkware.starknet.common.syscalls.GET_TX_INFO_SELECTOR": {
                "type": "const",
                "value": 1317029390204112103023
            },
            "starkware.starknet.common.syscalls.GET_TX_SIGNATURE_SELECTOR": {
                "type": "const",
                "value": 1448089128652340074717162277007973
            },
            "starkware.starknet.common.syscalls.GetBlockNumber": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockNumber",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetBlockNumberRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetBlockNumberResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetBlockNumberRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockNumberRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetBlockNumberResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockNumberResponse",
                "members": {
                    "block_number": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetBlockTimestamp": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockTimestamp",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetBlockTimestampRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetBlockTimestampResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetBlockTimestampRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockTimestampRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetBlockTimestampResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockTimestampResponse",
                "members": {
                    "block_timestamp": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetCallerAddress": {
                "full_name": "starkware.starknet.common.syscalls.GetCallerAddress",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetCallerAddressRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetCallerAddressResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetCallerAddressRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetCallerAddressRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetCallerAddressResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetCallerAddressResponse",
                "members": {
                    "caller_address": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetContractAddress": {
                "full_name": "starkware.starknet.common.syscalls.GetContractAddress",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetContractAddressRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetContractAddressResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetContractAddressRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetContractAddressRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetContractAddressResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetContractAddressResponse",
                "members": {
                    "contract_address": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetSequencerAddress": {
                "full_name": "starkware.starknet.common.syscalls.GetSequencerAddress",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetSequencerAddressRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetSequencerAddressResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetSequencerAddressRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetSequencerAddressRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetSequencerAddressResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetSequencerAddressResponse",
                "members": {
                    "sequencer_address": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxInfo": {
                "full_name": "starkware.starknet.common.syscalls.GetTxInfo",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetTxInfoRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetTxInfoResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxInfoRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetTxInfoRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxInfoResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetTxInfoResponse",
                "members": {
                    "tx_info": {
                        "cairo_type": "starkware.starknet.common.syscalls.TxInfo*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxSignature": {
                "full_name": "starkware.starknet.common.syscalls.GetTxSignature",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetTxSignatureRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetTxSignatureResponse",
                        "offset": 1
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxSignatureRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetTxSignatureRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxSignatureResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetTxSignatureResponse",
                "members": {
                    "signature": {
                        "cairo_type": "felt*",
                        "offset": 1
                    },
                    "signature_len": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.LIBRARY_CALL_L1_HANDLER_SELECTOR": {
                "type": "const",
                "value": 436233452754198157705746250789557519228244616562
            },
            "starkware.starknet.common.syscalls.LIBRARY_CALL_SELECTOR": {
                "type": "const",
                "value": 92376026794327011772951660
            },
            "starkware.starknet.common.syscalls.LibraryCall": {
                "full_name": "starkware.starknet.common.syscalls.LibraryCall",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.LibraryCallRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.CallContractResponse",
                        "offset": 5
                    }
                },
                "size": 7,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.LibraryCallRequest": {
                "full_name": "starkware.starknet.common.syscalls.LibraryCallRequest",
                "members": {
                    "calldata": {
                        "cairo_type": "felt*",
                        "offset": 4
                    },
                    "calldata_size": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "class_hash": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "function_selector": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.SEND_MESSAGE_TO_L1_SELECTOR": {
                "type": "const",
                "value": 433017908768303439907196859243777073
            },
            "starkware.starknet.common.syscalls.STORAGE_READ_SELECTOR": {
                "type": "const",
                "value": 100890693370601760042082660
            },
            "starkware.starknet.common.syscalls.STORAGE_WRITE_SELECTOR": {
                "type": "const",
                "value": 25828017502874050592466629733
            },
            "starkware.starknet.common.syscalls.SendMessageToL1SysCall": {
                "full_name": "starkware.starknet.common.syscalls.SendMessageToL1SysCall",
                "members": {
                    "payload_ptr": {
                        "cairo_type": "felt*",
                        "offset": 3
                    },
                    "payload_size": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "to_address": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.StorageRead": {
                "full_name": "starkware.starknet.common.syscalls.StorageRead",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.StorageReadRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.StorageReadResponse",
                        "offset": 2
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.StorageReadRequest": {
                "full_name": "starkware.starknet.common.syscalls.StorageReadRequest",
                "members": {
                    "address": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.StorageReadResponse": {
                "full_name": "starkware.starknet.common.syscalls.StorageReadResponse",
                "members": {
                    "value": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.StorageWrite": {
                "full_name": "starkware.starknet.common.syscalls.StorageWrite",
                "members": {
                    "address": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "value": {
                        "cairo_type": "felt",
                        "offset": 2
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.TxInfo": {
                "full_name": "starkware.starknet.common.syscalls.TxInfo",
                "members": {
                    "account_contract_address": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "chain_id": {
                        "cairo_type": "felt",
                        "offset": 6
                    },
                    "max_fee": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "nonce": {
                        "cairo_type": "felt",
                        "offset": 7
                    },
                    "signature": {
                        "cairo_type": "felt*",
                        "offset": 4
                    },
                    "signature_len": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "transaction_hash": {
                        "cairo_type": "felt",
                        "offset": 5
                    },
                    "version": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 8,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.call_contract": {
                "decorators": [],
                "pc": 31,
                "type": "function"
            },
            "starkware.starknet.common.syscalls.call_contract.Args": {
                "full_name": "starkware.starknet.common.syscalls.call_contract.Args",
                "members": {
                    "calldata": {
                        "cairo_type": "felt*",
                        "offset": 3
                    },
                    "calldata_size": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "contract_address": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "function_selector": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.call_contract.ImplicitArgs": {
                "full_name": "starkware.starknet.common.syscalls.call_contract.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.call_contract.Return": {
                "cairo_type": "(retdata_size: felt, retdata: felt*)",
                "type": "type_definition"
            },
            "starkware.starknet.common.syscalls.call_contract.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.syscalls.call_contract.__temp2": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.call_contract.__temp2",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 1
                        },
                        "pc": 33,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.call_contract.calldata": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.call_contract.calldata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 0
                        },
                        "pc": 31,
                        "value": "[cast(fp + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.call_contract.calldata_size": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.call_contract.calldata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 0
                        },
                        "pc": 31,
                        "value": "[cast(fp + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.call_contract.contract_address": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.call_contract.contract_address",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 0
                        },
                        "pc": 31,
                        "value": "[cast(fp + (-6), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.call_contract.function_selector": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.call_contract.function_selector",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 0
                        },
                        "pc": 31,
                        "value": "[cast(fp + (-5), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.call_contract.response": {
                "cairo_type": "starkware.starknet.common.syscalls.CallContractResponse",
                "full_name": "starkware.starknet.common.syscalls.call_contract.response",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 1
                        },
                        "pc": 38,
                        "value": "[cast([fp + (-7)] + 5, starkware.starknet.common.syscalls.CallContractResponse*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.call_contract.syscall": {
                "cairo_type": "starkware.starknet.common.syscalls.CallContract",
                "full_name": "starkware.starknet.common.syscalls.call_contract.syscall",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 0
                        },
                        "pc": 31,
                        "value": "[cast([fp + (-7)], starkware.starknet.common.syscalls.CallContract*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.call_contract.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.call_contract.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 0
                        },
                        "pc": 31,
                        "value": "[cast(fp + (-7), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 1
                        },
                        "pc": 38,
                        "value": "cast([fp + (-7)] + 7, felt*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.deploy": {
                "decorators": [],
                "pc": 43,
                "type": "function"
            },
            "starkware.starknet.common.syscalls.deploy.Args": {
                "full_name": "starkware.starknet.common.syscalls.deploy.Args",
                "members": {
                    "class_hash": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "constructor_calldata": {
                        "cairo_type": "felt*",
                        "offset": 3
                    },
                    "constructor_calldata_size": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "contract_address_salt": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "deploy_from_zero": {
                        "cairo_type": "felt",
                        "offset": 4
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.deploy.ImplicitArgs": {
                "full_name": "starkware.starknet.common.syscalls.deploy.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.deploy.Return": {
                "cairo_type": "(contract_address: felt)",
                "type": "type_definition"
            },
            "starkware.starknet.common.syscalls.deploy.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.syscalls.deploy.__temp3": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.deploy.__temp3",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 1
                        },
                        "pc": 45,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.deploy.class_hash": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.deploy.class_hash",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 43,
                        "value": "[cast(fp + (-7), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.deploy.constructor_calldata": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.deploy.constructor_calldata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 43,
                        "value": "[cast(fp + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.deploy.constructor_calldata_size": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.deploy.constructor_calldata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 43,
                        "value": "[cast(fp + (-5), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.deploy.contract_address_salt": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.deploy.contract_address_salt",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 43,
                        "value": "[cast(fp + (-6), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.deploy.deploy_from_zero": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.deploy.deploy_from_zero",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 43,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.deploy.response": {
                "cairo_type": "starkware.starknet.common.syscalls.DeployResponse",
                "full_name": "starkware.starknet.common.syscalls.deploy.response",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 1
                        },
                        "pc": 51,
                        "value": "[cast([fp + (-8)] + 6, starkware.starknet.common.syscalls.DeployResponse*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.deploy.syscall": {
                "cairo_type": "starkware.starknet.common.syscalls.Deploy",
                "full_name": "starkware.starknet.common.syscalls.deploy.syscall",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 43,
                        "value": "[cast([fp + (-8)], starkware.starknet.common.syscalls.Deploy*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.deploy.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.deploy.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 43,
                        "value": "[cast(fp + (-8), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 1
                        },
                        "pc": 51,
                        "value": "cast([fp + (-8)] + 9, felt*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.get_caller_address": {
                "decorators": [],
                "pc": 55,
                "type": "function"
            },
            "starkware.starknet.common.syscalls.get_caller_address.Args": {
                "full_name": "starkware.starknet.common.syscalls.get_caller_address.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.get_caller_address.ImplicitArgs": {
                "full_name": "starkware.starknet.common.syscalls.get_caller_address.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.get_caller_address.Return": {
                "cairo_type": "(caller_address: felt)",
                "type": "type_definition"
            },
            "starkware.starknet.common.syscalls.get_caller_address.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.syscalls.get_caller_address.__temp4": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.get_caller_address.__temp4",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 1
                        },
                        "pc": 57,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.get_caller_address.syscall": {
                "cairo_type": "starkware.starknet.common.syscalls.GetCallerAddress",
                "full_name": "starkware.starknet.common.syscalls.get_caller_address.syscall",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 0
                        },
                        "pc": 55,
                        "value": "[cast([fp + (-3)], starkware.starknet.common.syscalls.GetCallerAddress*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.get_caller_address.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.get_caller_address.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 0
                        },
                        "pc": 55,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 1
                        },
                        "pc": 58,
                        "value": "cast([fp + (-3)] + 2, felt*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.get_contract_address": {
                "decorators": [],
                "pc": 62,
                "type": "function"
            },
            "starkware.starknet.common.syscalls.get_contract_address.Args": {
                "full_name": "starkware.starknet.common.syscalls.get_contract_address.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.get_contract_address.ImplicitArgs": {
                "full_name": "starkware.starknet.common.syscalls.get_contract_address.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.get_contract_address.Return": {
                "cairo_type": "(contract_address: felt)",
                "type": "type_definition"
            },
            "starkware.starknet.common.syscalls.get_contract_address.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.syscalls.get_contract_address.__temp5": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.get_contract_address.__temp5",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 8,
                            "offset": 1
                        },
                        "pc": 64,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.get_contract_address.syscall": {
                "cairo_type": "starkware.starknet.common.syscalls.GetContractAddress",
                "full_name": "starkware.starknet.common.syscalls.get_contract_address.syscall",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 8,
                            "offset": 0
                        },
                        "pc": 62,
                        "value": "[cast([fp + (-3)], starkware.starknet.common.syscalls.GetContractAddress*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.get_contract_address.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.get_contract_address.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 8,
                            "offset": 0
                        },
                        "pc": 62,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 8,
                            "offset": 1
                        },
                        "pc": 65,
                        "value": "cast([fp + (-3)] + 2, felt*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.get_tx_info": {
                "decorators": [],
                "pc": 85,
                "type": "function"
            },
            "starkware.starknet.common.syscalls.get_tx_info.Args": {
                "full_name": "starkware.starknet.common.syscalls.get_tx_info.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.get_tx_info.ImplicitArgs": {
                "full_name": "starkware.starknet.common.syscalls.get_tx_info.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.get_tx_info.Return": {
                "cairo_type": "(tx_info: starkware.starknet.common.syscalls.TxInfo*)",
                "type": "type_definition"
            },
            "starkware.starknet.common.syscalls.get_tx_info.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.syscalls.get_tx_info.__temp8": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.get_tx_info.__temp8",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 11,
                            "offset": 1
                        },
                        "pc": 87,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.get_tx_info.response": {
                "cairo_type": "starkware.starknet.common.syscalls.GetTxInfoResponse",
                "full_name": "starkware.starknet.common.syscalls.get_tx_info.response",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 11,
                            "offset": 1
                        },
                        "pc": 88,
                        "value": "[cast([fp + (-3)] + 1, starkware.starknet.common.syscalls.GetTxInfoResponse*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.get_tx_info.syscall": {
                "cairo_type": "starkware.starknet.common.syscalls.GetTxInfo",
                "full_name": "starkware.starknet.common.syscalls.get_tx_info.syscall",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 11,
                            "offset": 0
                        },
                        "pc": 85,
                        "value": "[cast([fp + (-3)], starkware.starknet.common.syscalls.GetTxInfo*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.get_tx_info.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.get_tx_info.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 11,
                            "offset": 0
                        },
                        "pc": 85,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 11,
                            "offset": 1
                        },
                        "pc": 88,
                        "value": "cast([fp + (-3)] + 2, felt*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_read": {
                "decorators": [],
                "pc": 69,
                "type": "function"
            },
            "starkware.starknet.common.syscalls.storage_read.Args": {
                "full_name": "starkware.starknet.common.syscalls.storage_read.Args",
                "members": {
                    "address": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_read.ImplicitArgs": {
                "full_name": "starkware.starknet.common.syscalls.storage_read.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_read.Return": {
                "cairo_type": "(value: felt)",
                "type": "type_definition"
            },
            "starkware.starknet.common.syscalls.storage_read.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.syscalls.storage_read.__temp6": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.storage_read.__temp6",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 1
                        },
                        "pc": 71,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_read.address": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.storage_read.address",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 0
                        },
                        "pc": 69,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_read.response": {
                "cairo_type": "starkware.starknet.common.syscalls.StorageReadResponse",
                "full_name": "starkware.starknet.common.syscalls.storage_read.response",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 1
                        },
                        "pc": 73,
                        "value": "[cast([fp + (-4)] + 2, starkware.starknet.common.syscalls.StorageReadResponse*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_read.syscall": {
                "cairo_type": "starkware.starknet.common.syscalls.StorageRead",
                "full_name": "starkware.starknet.common.syscalls.storage_read.syscall",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 0
                        },
                        "pc": 69,
                        "value": "[cast([fp + (-4)], starkware.starknet.common.syscalls.StorageRead*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_read.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.storage_read.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 0
                        },
                        "pc": 69,
                        "value": "[cast(fp + (-4), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 1
                        },
                        "pc": 73,
                        "value": "cast([fp + (-4)] + 3, felt*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_write": {
                "decorators": [],
                "pc": 77,
                "type": "function"
            },
            "starkware.starknet.common.syscalls.storage_write.Args": {
                "full_name": "starkware.starknet.common.syscalls.storage_write.Args",
                "members": {
                    "address": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "value": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_write.ImplicitArgs": {
                "full_name": "starkware.starknet.common.syscalls.storage_write.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_write.Return": {
                "cairo_type": "()",
                "type": "type_definition"
            },
            "starkware.starknet.common.syscalls.storage_write.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.syscalls.storage_write.__temp7": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.storage_write.__temp7",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 10,
                            "offset": 1
                        },
                        "pc": 79,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_write.address": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.storage_write.address",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 10,
                            "offset": 0
                        },
                        "pc": 77,
                        "value": "[cast(fp + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_write.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.storage_write.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 10,
                            "offset": 0
                        },
                        "pc": 77,
                        "value": "[cast(fp + (-5), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 10,
                            "offset": 1
                        },
                        "pc": 82,
                        "value": "cast([fp + (-5)] + 3, felt*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_write.value": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.storage_write.value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 10,
                            "offset": 0
                        },
                        "pc": 77,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "utils.constants.FALSE": {
                "type": "const",
                "value": 0
            },
            "utils.constants.PREFIX_TRANSACTION": {
                "type": "const",
                "value": 476441609247967894954472788179128007176248455022
            },
            "utils.constants.TRUE": {
                "type": "const",
                "value": 1
            },
            "utils.constants.UINT8_MAX": {
                "type": "const",
                "value": 256
            }
        },
        "main_scope": "__main__",
        "prime": "0x800000000000011000000000000000000000000000000000000000000000001",
        "reference_manager": {
            "references": [
                {
                    "ap_tracking_data": {
                        "group": 1,
                        "offset": 0
                    },
                    "pc": 3,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 1,
                        "offset": 0
                    },
                    "pc": 3,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 1,
                        "offset": 0
                    },
                    "pc": 3,
                    "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 1,
                        "offset": 0
                    },
                    "pc": 5,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 1,
                        "offset": 0
                    },
                    "pc": 5,
                    "value": "cast([fp + (-5)] + 3, starkware.cairo.common.cairo_builtins.HashBuiltin*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 0
                    },
                    "pc": 9,
                    "value": "[cast(fp + (-5), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 0
                    },
                    "pc": 9,
                    "value": "[cast(fp + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 0
                    },
                    "pc": 9,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 2
                    },
                    "pc": 14,
                    "value": "[cast(ap + (-2), starkware.cairo.common.memcpy.memcpy.LoopFrame*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 2
                    },
                    "pc": 14,
                    "value": "[cast(ap + (-2), starkware.cairo.common.memcpy.memcpy.LoopFrame*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 3
                    },
                    "pc": 15,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 3
                    },
                    "pc": 16,
                    "value": "[cast(ap, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 3
                    },
                    "pc": 16,
                    "value": "cast(ap + 1, starkware.cairo.common.memcpy.memcpy.LoopFrame*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 0
                    },
                    "pc": 25,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 0
                    },
                    "pc": 25,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 1
                    },
                    "pc": 26,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 0
                    },
                    "pc": 31,
                    "value": "[cast(fp + (-6), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 0
                    },
                    "pc": 31,
                    "value": "[cast(fp + (-5), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 0
                    },
                    "pc": 31,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 0
                    },
                    "pc": 31,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 0
                    },
                    "pc": 31,
                    "value": "[cast(fp + (-7), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 0
                    },
                    "pc": 31,
                    "value": "[cast([fp + (-7)], starkware.starknet.common.syscalls.CallContract*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 1
                    },
                    "pc": 33,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 1
                    },
                    "pc": 38,
                    "value": "[cast([fp + (-7)] + 5, starkware.starknet.common.syscalls.CallContractResponse*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 1
                    },
                    "pc": 38,
                    "value": "cast([fp + (-7)] + 7, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 43,
                    "value": "[cast(fp + (-7), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 43,
                    "value": "[cast(fp + (-6), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 43,
                    "value": "[cast(fp + (-5), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 43,
                    "value": "[cast(fp + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 43,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 43,
                    "value": "[cast(fp + (-8), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 43,
                    "value": "[cast([fp + (-8)], starkware.starknet.common.syscalls.Deploy*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 1
                    },
                    "pc": 45,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 1
                    },
                    "pc": 51,
                    "value": "[cast([fp + (-8)] + 6, starkware.starknet.common.syscalls.DeployResponse*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 1
                    },
                    "pc": 51,
                    "value": "cast([fp + (-8)] + 9, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 0
                    },
                    "pc": 55,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 0
                    },
                    "pc": 55,
                    "value": "[cast([fp + (-3)], starkware.starknet.common.syscalls.GetCallerAddress*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 1
                    },
                    "pc": 57,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 1
                    },
                    "pc": 58,
                    "value": "cast([fp + (-3)] + 2, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 8,
                        "offset": 0
                    },
                    "pc": 62,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 8,
                        "offset": 0
                    },
                    "pc": 62,
                    "value": "[cast([fp + (-3)], starkware.starknet.common.syscalls.GetContractAddress*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 8,
                        "offset": 1
                    },
                    "pc": 64,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 8,
                        "offset": 1
                    },
                    "pc": 65,
                    "value": "cast([fp + (-3)] + 2, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 0
                    },
                    "pc": 69,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 0
                    },
                    "pc": 69,
                    "value": "[cast(fp + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 0
                    },
                    "pc": 69,
                    "value": "[cast([fp + (-4)], starkware.starknet.common.syscalls.StorageRead*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 1
                    },
                    "pc": 71,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 1
                    },
                    "pc": 73,
                    "value": "[cast([fp + (-4)] + 2, starkware.starknet.common.syscalls.StorageReadResponse*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 1
                    },
                    "pc": 73,
                    "value": "cast([fp + (-4)] + 3, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 10,
                        "offset": 0
                    },
                    "pc": 77,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 10,
                        "offset": 0
                    },
                    "pc": 77,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 10,
                        "offset": 0
                    },
                    "pc": 77,
                    "value": "[cast(fp + (-5), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 10,
                        "offset": 1
                    },
                    "pc": 79,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 10,
                        "offset": 1
                    },
                    "pc": 82,
                    "value": "cast([fp + (-5)] + 3, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 11,
                        "offset": 0
                    },
                    "pc": 85,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 11,
                        "offset": 0
                    },
                    "pc": 85,
                    "value": "[cast([fp + (-3)], starkware.starknet.common.syscalls.GetTxInfo*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 11,
                        "offset": 1
                    },
                    "pc": 87,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 11,
                        "offset": 1
                    },
                    "pc": 88,
                    "value": "[cast([fp + (-3)] + 1, starkware.starknet.common.syscalls.GetTxInfoResponse*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 11,
                        "offset": 1
                    },
                    "pc": 88,
                    "value": "cast([fp + (-3)] + 2, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 12,
                        "offset": 4
                    },
                    "pc": 96,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 12,
                        "offset": 4
                    },
                    "pc": 96,
                    "value": "[cast(fp, starkware.cairo.common.hash_state.HashState*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 13,
                        "offset": 0
                    },
                    "pc": 102,
                    "value": "[cast(fp + (-5), starkware.cairo.common.hash_state.HashState**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 13,
                        "offset": 0
                    },
                    "pc": 102,
                    "value": "[cast(fp + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 13,
                        "offset": 0
                    },
                    "pc": 102,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 13,
                        "offset": 0
                    },
                    "pc": 102,
                    "value": "[cast(fp + (-6), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 14,
                        "offset": 0
                    },
                    "pc": 110,
                    "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 14,
                        "offset": 0
                    },
                    "pc": 110,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 14,
                        "offset": 2
                    },
                    "pc": 112,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 14,
                        "offset": 2
                    },
                    "pc": 112,
                    "value": "[cast(fp, starkware.cairo.common.hash_state.HashState*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 14,
                        "offset": 3
                    },
                    "pc": 114,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 15,
                        "offset": 0
                    },
                    "pc": 118,
                    "value": "[cast(fp + (-4), starkware.cairo.common.hash_state.HashState**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 15,
                        "offset": 0
                    },
                    "pc": 118,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 15,
                        "offset": 0
                    },
                    "pc": 118,
                    "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 15,
                        "offset": 9
                    },
                    "pc": 125,
                    "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 15,
                        "offset": 9
                    },
                    "pc": 125,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 15,
                        "offset": 11
                    },
                    "pc": 127,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 15,
                        "offset": 11
                    },
                    "pc": 127,
                    "value": "[cast(fp, starkware.cairo.common.hash_state.HashState*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 15,
                        "offset": 12
                    },
                    "pc": 129,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 16,
                        "offset": 0
                    },
                    "pc": 134,
                    "value": "[cast(fp + (-3), starkware.cairo.common.hash_state.HashState**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 16,
                        "offset": 0
                    },
                    "pc": 134,
                    "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 16,
                        "offset": 7
                    },
                    "pc": 139,
                    "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 16,
                        "offset": 7
                    },
                    "pc": 139,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 0
                    },
                    "pc": 140,
                    "value": "[cast(fp + (-5), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 0
                    },
                    "pc": 140,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 0
                    },
                    "pc": 140,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 0
                    },
                    "pc": 140,
                    "value": "[cast(fp + (-6), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 2
                    },
                    "pc": 149,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 2
                    },
                    "pc": 150,
                    "value": "[cast(fp, felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 2
                    },
                    "pc": 150,
                    "value": "cast(ap, starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 5
                    },
                    "pc": 153,
                    "value": "cast(ap + (-3), starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 6
                    },
                    "pc": 154,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 7
                    },
                    "pc": 156,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 7
                    },
                    "pc": 157,
                    "value": "cast(ap, starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 10
                    },
                    "pc": 164,
                    "value": "cast(ap + (-3), starkware.cairo.common.hash_state.hash_update_inner.LoopLocals*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 17,
                        "offset": 10
                    },
                    "pc": 164,
                    "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 18,
                        "offset": 0
                    },
                    "pc": 165,
                    "value": "[cast(fp + (-6), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 18,
                        "offset": 0
                    },
                    "pc": 165,
                    "value": "[cast(fp + (-5), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 18,
                        "offset": 0
                    },
                    "pc": 165,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 18,
                        "offset": 0
                    },
                    "pc": 165,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 18,
                        "offset": 0
                    },
                    "pc": 165,
                    "value": "[cast(fp + (-7), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 18,
                        "offset": 0
                    },
                    "pc": 167,
                    "value": "cast([fp + (-7)] + 2, starkware.cairo.common.cairo_builtins.SignatureBuiltin*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 19,
                        "offset": 0
                    },
                    "pc": 170,
                    "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 19,
                        "offset": 0
                    },
                    "pc": 170,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 19,
                        "offset": 0
                    },
                    "pc": 170,
                    "value": "cast(1672321442399497129215646424919402195095307045612040218489019266998007191460, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 0
                    },
                    "pc": 175,
                    "value": "[cast(fp + (-5), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 0
                    },
                    "pc": 175,
                    "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 0
                    },
                    "pc": 175,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 7
                    },
                    "pc": 179,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 7
                    },
                    "pc": 179,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 7
                    },
                    "pc": 179,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 14
                    },
                    "pc": 183,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 14
                    },
                    "pc": 183,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 15
                    },
                    "pc": 184,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 16
                    },
                    "pc": 185,
                    "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 17
                    },
                    "pc": 186,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 20,
                        "offset": 18
                    },
                    "pc": 187,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 21,
                        "offset": 0
                    },
                    "pc": 188,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 21,
                        "offset": 0
                    },
                    "pc": 188,
                    "value": "[cast(fp + (-6), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 21,
                        "offset": 0
                    },
                    "pc": 188,
                    "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 21,
                        "offset": 0
                    },
                    "pc": 188,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 21,
                        "offset": 7
                    },
                    "pc": 192,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 21,
                        "offset": 7
                    },
                    "pc": 192,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 21,
                        "offset": 7
                    },
                    "pc": 192,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 21,
                        "offset": 14
                    },
                    "pc": 197,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 22,
                        "offset": 0
                    },
                    "pc": 200,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 22,
                        "offset": 6
                    },
                    "pc": 203,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 22,
                        "offset": 6
                    },
                    "pc": 203,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 22,
                        "offset": 12
                    },
                    "pc": 206,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 22,
                        "offset": 12
                    },
                    "pc": 206,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 23,
                        "offset": 0
                    },
                    "pc": 209,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 23,
                        "offset": 0
                    },
                    "pc": 209,
                    "value": "[cast([fp + (-5)] + 1, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 23,
                        "offset": 0
                    },
                    "pc": 209,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 23,
                        "offset": 0
                    },
                    "pc": 209,
                    "value": "[cast([fp + (-5)] + 3, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 23,
                        "offset": 0
                    },
                    "pc": 209,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 23,
                        "offset": 0
                    },
                    "pc": 209,
                    "value": "cast([fp + (-3)] - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 23,
                        "offset": 16
                    },
                    "pc": 213,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 23,
                        "offset": 16
                    },
                    "pc": 213,
                    "value": "[cast(ap + 0, ()*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 23,
                        "offset": 17
                    },
                    "pc": 215,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 23,
                        "offset": 17
                    },
                    "pc": 215,
                    "value": "cast(0, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 24,
                        "offset": 0
                    },
                    "pc": 223,
                    "value": "[cast(fp + (-5), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 24,
                        "offset": 0
                    },
                    "pc": 223,
                    "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 24,
                        "offset": 0
                    },
                    "pc": 223,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 24,
                        "offset": 23
                    },
                    "pc": 228,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 24,
                        "offset": 23
                    },
                    "pc": 228,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 24,
                        "offset": 23
                    },
                    "pc": 228,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 24,
                        "offset": 23
                    },
                    "pc": 228,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 25,
                        "offset": 0
                    },
                    "pc": 229,
                    "value": "[cast(fp + (-4), (res: felt)*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 25,
                        "offset": 0
                    },
                    "pc": 229,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 25,
                        "offset": 1
                    },
                    "pc": 231,
                    "value": "[cast(fp, felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 25,
                        "offset": 1
                    },
                    "pc": 231,
                    "value": "[cast(fp, felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 25,
                        "offset": 1
                    },
                    "pc": 232,
                    "value": "cast([fp] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 25,
                        "offset": 2
                    },
                    "pc": 234,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 0
                    },
                    "pc": 238,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 0
                    },
                    "pc": 238,
                    "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 0
                    },
                    "pc": 238,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 0
                    },
                    "pc": 238,
                    "value": "[cast([fp + (-5)] + 3, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 0
                    },
                    "pc": 238,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 0
                    },
                    "pc": 238,
                    "value": "cast([fp + (-3)] - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 28
                    },
                    "pc": 244,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 28
                    },
                    "pc": 244,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 28
                    },
                    "pc": 244,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 28
                    },
                    "pc": 244,
                    "value": "[cast(ap + (-1), (res: felt)*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 36
                    },
                    "pc": 247,
                    "value": "[cast(ap + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 36
                    },
                    "pc": 247,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 26,
                        "offset": 36
                    },
                    "pc": 247,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 27,
                        "offset": 0
                    },
                    "pc": 254,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 27,
                        "offset": 0
                    },
                    "pc": 254,
                    "value": "[cast(fp + (-6), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 27,
                        "offset": 0
                    },
                    "pc": 254,
                    "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 27,
                        "offset": 0
                    },
                    "pc": 254,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 27,
                        "offset": 16
                    },
                    "pc": 257,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 27,
                        "offset": 37
                    },
                    "pc": 262,
                    "value": "[cast(ap + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 27,
                        "offset": 37
                    },
                    "pc": 262,
                    "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 27,
                        "offset": 37
                    },
                    "pc": 262,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 0
                    },
                    "pc": 263,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 0
                    },
                    "pc": 263,
                    "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 0
                    },
                    "pc": 263,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 0
                    },
                    "pc": 263,
                    "value": "[cast([fp + (-5)] + 3, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 0
                    },
                    "pc": 263,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 0
                    },
                    "pc": 263,
                    "value": "[cast([fp + (-3)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 0
                    },
                    "pc": 263,
                    "value": "cast([fp + (-3)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 0
                    },
                    "pc": 263,
                    "value": "cast([fp + (-3)] + 1 - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 1
                    },
                    "pc": 265,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 44
                    },
                    "pc": 272,
                    "value": "[cast(ap + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 44
                    },
                    "pc": 272,
                    "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 44
                    },
                    "pc": 272,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 44
                    },
                    "pc": 272,
                    "value": "[cast(ap + 0, ()*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 45
                    },
                    "pc": 274,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 28,
                        "offset": 45
                    },
                    "pc": 274,
                    "value": "cast(0, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 29,
                        "offset": 0
                    },
                    "pc": 282,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 29,
                        "offset": 0
                    },
                    "pc": 282,
                    "value": "[cast(fp + (-6), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 29,
                        "offset": 0
                    },
                    "pc": 282,
                    "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 29,
                        "offset": 0
                    },
                    "pc": 282,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 29,
                        "offset": 22
                    },
                    "pc": 288,
                    "value": "[cast(ap + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 29,
                        "offset": 22
                    },
                    "pc": 288,
                    "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 29,
                        "offset": 22
                    },
                    "pc": 288,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 0
                    },
                    "pc": 289,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 0
                    },
                    "pc": 289,
                    "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 0
                    },
                    "pc": 289,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 0
                    },
                    "pc": 289,
                    "value": "[cast([fp + (-5)] + 3, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 0
                    },
                    "pc": 289,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 0
                    },
                    "pc": 289,
                    "value": "[cast([fp + (-3)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 0
                    },
                    "pc": 289,
                    "value": "cast([fp + (-3)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 0
                    },
                    "pc": 289,
                    "value": "cast([fp + (-3)] + 1 - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 1
                    },
                    "pc": 291,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 29
                    },
                    "pc": 298,
                    "value": "[cast(ap + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 29
                    },
                    "pc": 298,
                    "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 29
                    },
                    "pc": 298,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 29
                    },
                    "pc": 298,
                    "value": "[cast(ap + 0, ()*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 30
                    },
                    "pc": 300,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 30,
                        "offset": 30
                    },
                    "pc": 300,
                    "value": "cast(0, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 0
                    },
                    "pc": 308,
                    "value": "[cast(fp + (-5), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 0
                    },
                    "pc": 308,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 0
                    },
                    "pc": 308,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 0
                    },
                    "pc": 308,
                    "value": "[cast(fp + (-9), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 0
                    },
                    "pc": 308,
                    "value": "[cast(fp + (-8), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 0
                    },
                    "pc": 308,
                    "value": "[cast(fp + (-7), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 0
                    },
                    "pc": 308,
                    "value": "[cast(fp + (-6), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 23
                    },
                    "pc": 313,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 23
                    },
                    "pc": 313,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 23
                    },
                    "pc": 313,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 23
                    },
                    "pc": 313,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 23
                    },
                    "pc": 315,
                    "value": "[cast([fp + (-3)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 23
                    },
                    "pc": 315,
                    "value": "[cast([fp + (-3)] + 1, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 31,
                        "offset": 31
                    },
                    "pc": 322,
                    "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 0
                    },
                    "pc": 327,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 0
                    },
                    "pc": 327,
                    "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 0
                    },
                    "pc": 327,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 0
                    },
                    "pc": 327,
                    "value": "[cast([fp + (-5)] + 3, starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 0
                    },
                    "pc": 327,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 0
                    },
                    "pc": 327,
                    "value": "[cast([fp + (-3)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 0
                    },
                    "pc": 327,
                    "value": "cast([fp + (-3)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 0
                    },
                    "pc": 327,
                    "value": "[cast([fp + (-3)] + 1, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 0
                    },
                    "pc": 327,
                    "value": "cast([fp + (-3)] + 2, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 1
                    },
                    "pc": 328,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 2
                    },
                    "pc": 329,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 2
                    },
                    "pc": 330,
                    "value": "cast([[fp + (-5)] + 2] + 1, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 2
                    },
                    "pc": 330,
                    "value": "cast([fp + (-3)] + 2, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 3
                    },
                    "pc": 332,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 4
                    },
                    "pc": 333,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 5
                    },
                    "pc": 334,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 5
                    },
                    "pc": 334,
                    "value": "cast([ap + (-1)] - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 6
                    },
                    "pc": 336,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 50
                    },
                    "pc": 347,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 50
                    },
                    "pc": 347,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 50
                    },
                    "pc": 347,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 50
                    },
                    "pc": 347,
                    "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 50
                    },
                    "pc": 347,
                    "value": "[cast(ap + 0, ()*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 51
                    },
                    "pc": 349,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 32,
                        "offset": 51
                    },
                    "pc": 349,
                    "value": "cast(0, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 0
                    },
                    "pc": 357,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 0
                    },
                    "pc": 357,
                    "value": "[cast(fp + (-7), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 0
                    },
                    "pc": 357,
                    "value": "[cast(fp + (-6), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 0
                    },
                    "pc": 357,
                    "value": "[cast(fp + (-5), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 0
                    },
                    "pc": 357,
                    "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 6
                    },
                    "pc": 360,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 6
                    },
                    "pc": 360,
                    "value": "[cast(ap + (-1), starkware.starknet.common.syscalls.TxInfo**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 50
                    },
                    "pc": 369,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 50
                    },
                    "pc": 369,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 50
                    },
                    "pc": 369,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 33,
                        "offset": 50
                    },
                    "pc": 369,
                    "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 0
                    },
                    "pc": 370,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 0
                    },
                    "pc": 370,
                    "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 0
                    },
                    "pc": 370,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 0
                    },
                    "pc": 370,
                    "value": "[cast([fp + (-5)] + 3, starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 0
                    },
                    "pc": 370,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 0
                    },
                    "pc": 370,
                    "value": "[cast([fp + (-3)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 0
                    },
                    "pc": 370,
                    "value": "cast([fp + (-3)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 0
                    },
                    "pc": 370,
                    "value": "cast([fp + (-3)] + 1 - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 1
                    },
                    "pc": 372,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 58
                    },
                    "pc": 380,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 58
                    },
                    "pc": 380,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 58
                    },
                    "pc": 380,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 58
                    },
                    "pc": 380,
                    "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 58
                    },
                    "pc": 380,
                    "value": "[cast(ap + 0, ()*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 59
                    },
                    "pc": 382,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 34,
                        "offset": 59
                    },
                    "pc": 382,
                    "value": "cast(0, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 0
                    },
                    "pc": 390,
                    "value": "[cast(fp + (-6), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 0
                    },
                    "pc": 390,
                    "value": "[cast(fp + (-5), __main__.CallArray**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 0
                    },
                    "pc": 390,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 0
                    },
                    "pc": 390,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 0
                    },
                    "pc": 390,
                    "value": "[cast(fp + (-10), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 0
                    },
                    "pc": 390,
                    "value": "[cast(fp + (-9), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 0
                    },
                    "pc": 390,
                    "value": "[cast(fp + (-8), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 0
                    },
                    "pc": 390,
                    "value": "[cast(fp + (-7), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 6
                    },
                    "pc": 393,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 6
                    },
                    "pc": 393,
                    "value": "[cast(ap + (-1), starkware.starknet.common.syscalls.TxInfo**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 50
                    },
                    "pc": 402,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 50
                    },
                    "pc": 402,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 50
                    },
                    "pc": 402,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 35,
                        "offset": 50
                    },
                    "pc": 402,
                    "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 0
                    },
                    "pc": 403,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 0
                    },
                    "pc": 403,
                    "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 0
                    },
                    "pc": 403,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 0
                    },
                    "pc": 403,
                    "value": "[cast([fp + (-5)] + 3, starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 0
                    },
                    "pc": 403,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 0
                    },
                    "pc": 403,
                    "value": "[cast([fp + (-3)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 0
                    },
                    "pc": 403,
                    "value": "cast([fp + (-3)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 1
                    },
                    "pc": 404,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 2
                    },
                    "pc": 405,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 2
                    },
                    "pc": 406,
                    "value": "cast([[fp + (-5)] + 2] + 1, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 2
                    },
                    "pc": 406,
                    "value": "cast([fp + (-3)] + 1, __main__.CallArray*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 3
                    },
                    "pc": 408,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 4
                    },
                    "pc": 409,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 5
                    },
                    "pc": 411,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 6
                    },
                    "pc": 412,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 6
                    },
                    "pc": 412,
                    "value": "[cast([ap + (-1)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 6
                    },
                    "pc": 412,
                    "value": "cast([ap + (-1)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 7
                    },
                    "pc": 413,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 8
                    },
                    "pc": 414,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 8
                    },
                    "pc": 415,
                    "value": "cast([[fp + (-5)] + 2] + 2, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 8
                    },
                    "pc": 415,
                    "value": "cast([ap + (-3)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 9
                    },
                    "pc": 417,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 10
                    },
                    "pc": 418,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 11
                    },
                    "pc": 419,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 11
                    },
                    "pc": 419,
                    "value": "cast([ap + (-1)] - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 12
                    },
                    "pc": 421,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 72
                    },
                    "pc": 434,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 72
                    },
                    "pc": 434,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 72
                    },
                    "pc": 434,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 72
                    },
                    "pc": 434,
                    "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 72
                    },
                    "pc": 434,
                    "value": "[cast(ap + 0, ()*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 73
                    },
                    "pc": 436,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 36,
                        "offset": 73
                    },
                    "pc": 436,
                    "value": "cast(0, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 0
                    },
                    "pc": 444,
                    "value": "[cast(fp + (-6), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 0
                    },
                    "pc": 444,
                    "value": "[cast(fp + (-5), __main__.CallArray**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 0
                    },
                    "pc": 444,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 0
                    },
                    "pc": 444,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 0
                    },
                    "pc": 444,
                    "value": "[cast(fp + (-10), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 0
                    },
                    "pc": 444,
                    "value": "[cast(fp + (-9), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 0
                    },
                    "pc": 444,
                    "value": "[cast(fp + (-8), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 0
                    },
                    "pc": 444,
                    "value": "[cast(fp + (-7), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 10
                    },
                    "pc": 448,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 16
                    },
                    "pc": 451,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 16
                    },
                    "pc": 451,
                    "value": "[cast(ap + (-1), starkware.starknet.common.syscalls.TxInfo**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 16
                    },
                    "pc": 452,
                    "value": "[cast(fp, starkware.starknet.common.syscalls.TxInfo**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 22
                    },
                    "pc": 455,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 22
                    },
                    "pc": 455,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 30
                    },
                    "pc": 464,
                    "value": "[cast(ap + (-1), __main__.Call**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 37,
                        "offset": 30
                    },
                    "pc": 465,
                    "value": "[cast(fp + 1, __main__.Call**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 38,
                        "offset": 0
                    },
                    "pc": 472,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 38,
                        "offset": 0
                    },
                    "pc": 472,
                    "value": "[cast(fp + (-6), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 38,
                        "offset": 0
                    },
                    "pc": 477,
                    "value": "[cast(fp + 2, __main__.MultiCall*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 38,
                        "offset": 3
                    },
                    "pc": 479,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 38,
                        "offset": 3
                    },
                    "pc": 480,
                    "value": "[cast(fp + 7, felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 39,
                        "offset": 0
                    },
                    "pc": 486,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 39,
                        "offset": 0
                    },
                    "pc": 486,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 0
                    },
                    "pc": 493,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 0
                    },
                    "pc": 493,
                    "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 0
                    },
                    "pc": 493,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 0
                    },
                    "pc": 493,
                    "value": "[cast([fp + (-5)] + 3, starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 0
                    },
                    "pc": 493,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 0
                    },
                    "pc": 493,
                    "value": "[cast([fp + (-3)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 0
                    },
                    "pc": 493,
                    "value": "cast([fp + (-3)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 1
                    },
                    "pc": 494,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 2
                    },
                    "pc": 495,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 2
                    },
                    "pc": 496,
                    "value": "cast([[fp + (-5)] + 2] + 1, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 2
                    },
                    "pc": 496,
                    "value": "cast([fp + (-3)] + 1, __main__.CallArray*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 3
                    },
                    "pc": 498,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 4
                    },
                    "pc": 499,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 5
                    },
                    "pc": 501,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 6
                    },
                    "pc": 502,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 6
                    },
                    "pc": 502,
                    "value": "[cast([ap + (-1)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 6
                    },
                    "pc": 502,
                    "value": "cast([ap + (-1)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 7
                    },
                    "pc": 503,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 8
                    },
                    "pc": 504,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 8
                    },
                    "pc": 505,
                    "value": "cast([[fp + (-5)] + 2] + 2, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 8
                    },
                    "pc": 505,
                    "value": "cast([ap + (-3)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 9
                    },
                    "pc": 507,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 10
                    },
                    "pc": 508,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 11
                    },
                    "pc": 509,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 11
                    },
                    "pc": 509,
                    "value": "cast([ap + (-1)] - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 40,
                        "offset": 12
                    },
                    "pc": 511,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 41,
                        "offset": 0
                    },
                    "pc": 524,
                    "value": "[cast(ap + (-6), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 41,
                        "offset": 0
                    },
                    "pc": 524,
                    "value": "[cast(ap + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 41,
                        "offset": 0
                    },
                    "pc": 524,
                    "value": "[cast(ap + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 41,
                        "offset": 0
                    },
                    "pc": 524,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.SignatureBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 41,
                        "offset": 0
                    },
                    "pc": 524,
                    "value": "[cast(ap + (-2), (retdata_size: felt, retdata: felt*)*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 41,
                        "offset": 0
                    },
                    "pc": 524,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 41,
                        "offset": 0
                    },
                    "pc": 524,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 42,
                        "offset": 0
                    },
                    "pc": 525,
                    "value": "[cast(fp + (-7), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 42,
                        "offset": 0
                    },
                    "pc": 525,
                    "value": "[cast(fp + (-6), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 42,
                        "offset": 0
                    },
                    "pc": 525,
                    "value": "[cast(fp + (-5), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 42,
                        "offset": 0
                    },
                    "pc": 525,
                    "value": "[cast(fp + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 42,
                        "offset": 0
                    },
                    "pc": 525,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 42,
                        "offset": 0
                    },
                    "pc": 525,
                    "value": "[cast(fp + (-8), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 42,
                        "offset": 16
                    },
                    "pc": 528,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 42,
                        "offset": 26
                    },
                    "pc": 535,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 42,
                        "offset": 26
                    },
                    "pc": 535,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 43,
                        "offset": 0
                    },
                    "pc": 536,
                    "value": "[cast(fp + (-4), (contract_address: felt)*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 43,
                        "offset": 0
                    },
                    "pc": 536,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 43,
                        "offset": 1
                    },
                    "pc": 538,
                    "value": "[cast(fp, felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 43,
                        "offset": 1
                    },
                    "pc": 538,
                    "value": "[cast(fp, felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 43,
                        "offset": 1
                    },
                    "pc": 539,
                    "value": "cast([fp] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 43,
                        "offset": 2
                    },
                    "pc": 541,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "[cast([fp + (-5)] + 1, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "[cast([fp + (-5)] + 3, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "[cast([fp + (-3)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "cast([fp + (-3)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "[cast([fp + (-3)] + 1, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "cast([fp + (-3)] + 2, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "[cast([fp + (-3)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 0
                    },
                    "pc": 545,
                    "value": "cast([fp + (-3)] + 3, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 1
                    },
                    "pc": 546,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 2
                    },
                    "pc": 547,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 2
                    },
                    "pc": 548,
                    "value": "cast([[fp + (-5)] + 2] + 1, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 2
                    },
                    "pc": 548,
                    "value": "cast([fp + (-3)] + 3, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 3
                    },
                    "pc": 550,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 4
                    },
                    "pc": 551,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 5
                    },
                    "pc": 552,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 5
                    },
                    "pc": 552,
                    "value": "[cast([ap + (-1)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 5
                    },
                    "pc": 552,
                    "value": "cast([ap + (-1)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 5
                    },
                    "pc": 552,
                    "value": "cast([ap + (-1)] + 1 - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 6
                    },
                    "pc": 554,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 40
                    },
                    "pc": 564,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 40
                    },
                    "pc": 564,
                    "value": "[cast(ap + (-1), (contract_address: felt)*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 41
                    },
                    "pc": 565,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 50
                    },
                    "pc": 570,
                    "value": "[cast(ap + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 50
                    },
                    "pc": 570,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 44,
                        "offset": 50
                    },
                    "pc": 570,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 45,
                        "offset": 0
                    },
                    "pc": 577,
                    "value": "[cast(fp + (-5), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 45,
                        "offset": 0
                    },
                    "pc": 577,
                    "value": "[cast(fp + (-4), __main__.Call**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 45,
                        "offset": 0
                    },
                    "pc": 577,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 45,
                        "offset": 0
                    },
                    "pc": 577,
                    "value": "[cast(fp + (-6), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 45,
                        "offset": 3
                    },
                    "pc": 585,
                    "value": "[cast([fp + (-4)], __main__.Call*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 45,
                        "offset": 14
                    },
                    "pc": 592,
                    "value": "[cast(ap + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 45,
                        "offset": 14
                    },
                    "pc": 592,
                    "value": "[cast(ap + (-2), (retdata_size: felt, retdata: felt*)*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 45,
                        "offset": 14
                    },
                    "pc": 594,
                    "value": "[cast(fp, (retdata_size: felt, retdata: felt*)*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 45,
                        "offset": 14
                    },
                    "pc": 595,
                    "value": "[cast(fp + 2, felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 47,
                        "offset": 0
                    },
                    "pc": 608,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 47,
                        "offset": 0
                    },
                    "pc": 608,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 48,
                        "offset": 0
                    },
                    "pc": 611,
                    "value": "[cast(fp + (-6), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 48,
                        "offset": 0
                    },
                    "pc": 611,
                    "value": "[cast(fp + (-5), __main__.CallArray**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 48,
                        "offset": 0
                    },
                    "pc": 611,
                    "value": "[cast(fp + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 48,
                        "offset": 0
                    },
                    "pc": 611,
                    "value": "[cast(fp + (-3), __main__.Call**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 48,
                        "offset": 0
                    },
                    "pc": 611,
                    "value": "[cast(fp + (-7), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 48,
                        "offset": 1
                    },
                    "pc": 616,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 48,
                        "offset": 2
                    },
                    "pc": 618,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 48,
                        "offset": 3
                    },
                    "pc": 620,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 48,
                        "offset": 4
                    },
                    "pc": 622,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 48,
                        "offset": 5
                    },
                    "pc": 623,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 49,
                        "offset": 0
                    },
                    "pc": 634,
                    "value": "[cast(ap + (-1), felt**)]"
                }
            ]
        }
    }
}
"""
