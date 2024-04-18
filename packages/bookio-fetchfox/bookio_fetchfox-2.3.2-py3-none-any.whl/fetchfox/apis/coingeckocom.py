import logging
import time
from typing import Tuple

from cachetools.func import ttl_cache

from fetchfox import rest
from fetchfox.constants.currencies import ALGO, ADA, BOOK, ETH, MATIC

BASE_URL = "https://api.coingecko.com/api/v3"

IDS = {
    ALGO: "algorand",
    ADA: "cardano",
    BOOK: "book-2",
    ETH: "ethereum",
    MATIC: "matic-network",
}

logger = logging.getLogger(__name__)


def get(service: str, params: dict = None) -> Tuple[dict, int]:
    return rest.get(
        url=f"{BASE_URL}/{service}",
        params=params,
    )


@ttl_cache(ttl=60 * 60)
def get_currency_usd_exchange(currency: str):
    time.sleep(5)

    currency = currency.strip().upper()

    id = IDS[currency]

    logger.info("fetching exchange for %s (%s)", currency, id)

    response, status_code = get(
        service="simple/price",
        params={
            "ids": id,
            "vs_currencies": "usd",
        },
    )

    return response[id]["usd"]


@ttl_cache(ttl=60 * 60)
def get_currency_ath_usd(currency: str):
    time.sleep(5)

    currency = currency.strip().upper()

    id = IDS[currency]

    logger.info("fetching ath for %s (%s)", currency, id)

    response, status_code = get(
        service=f"coins/{id}",
    )

    return response["market_data"]["ath"]["usd"]


def get_currency_history(currency: str, days: int = 7):
    id = IDS[currency]

    response, status_code = get(
        service=f"coins/{id}/market_chart",
        params={
            "vs_currency": "usd",
            "days": days,
        },
    )

    return response["prices"]
