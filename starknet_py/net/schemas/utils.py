def replace_invoke_contract_address_with_sender_address(data: dict):
    data["contract_address"] = data.get("contract_address") or data.get(
        "sender_address"
    )

    if data["contract_address"] is None:
        raise ValueError(
            "Missing field `contract_address` or `sender_address` for InvokeTransactionSchema."
        )

    del data["sender_address"]
