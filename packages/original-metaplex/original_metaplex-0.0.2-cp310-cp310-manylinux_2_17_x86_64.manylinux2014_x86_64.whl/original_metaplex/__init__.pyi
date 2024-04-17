from typing import Optional, Tuple

def call_metaplex_function() -> str: ...
def create_collection_v1(
    payer: str,
    name: str,
    uri: str,
    latest_blockhash: str,
    update_delegate: Optional[str] = None,
) -> Tuple[str, str]: ...
def fetch_collection_v1(collection_account: bytes) -> str: ...
def create_v1(
    payer: str, name: str, uri: str, owner: str, collection: str, latest_blockhash: str
) -> Tuple[str, str]: ...
