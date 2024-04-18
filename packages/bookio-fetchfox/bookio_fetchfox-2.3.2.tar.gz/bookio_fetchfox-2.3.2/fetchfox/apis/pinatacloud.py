from fetchfox import rest

BASE_URL = "https://book.mypinata.cloud/ipfs"


def get_metadata(uri: str) -> dict:
    uri = uri.replace("ipfs://", "")

    response, status_code = rest.get(f"{BASE_URL}/{uri}")

    return response
