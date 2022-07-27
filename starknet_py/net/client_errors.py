from typing import Optional, Union


class ClientError(Exception):
    """
    Base class for all errors raised while attempting to communicate with StarkNet through Client.
    """

    def __init__(self, message: str, code: Optional[str] = None):
        self.code = code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return (
            f"Client failed{f' with code {self.code}' if self.code is not None else ''}"
            f": {self.message}"
        )


class ContractNotFoundError(ClientError):
    """
    Requested contract was not found.
    """

    def __init__(
        self,
        block_hash: Optional[Union[int, str]] = None,
        block_number: Optional[int] = None,
    ):
        require_block_identifier(block_hash, block_number)

        identifier = block_hash or block_number
        self.identifier = str(identifier) if isinstance(identifier, int) else identifier

        super().__init__(f"No contract found for identifier: {self.identifier}")

    def __str__(self):
        return f"No contract found for identifier: {self.identifier}"


def require_block_identifier(block_hash, block_number):
    if block_hash is None and block_number is None:
        raise ValueError("One of block hash or number must be provided")
