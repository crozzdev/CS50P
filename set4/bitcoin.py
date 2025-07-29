import sys

import dotenv
import requests

COIN_API_KEY = dotenv.get_key(".env", "COIN_API_KEY")


def get_n() -> float:
    """Get the n amount of bitcoins to buy from CLI parameter"""

    args = sys.argv

    if len(args) < 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(args[1])
        return n
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_bitcoin_price() -> float | None:
    """Get the price of the bitcoin using the coincap API"""
    try:
        response = requests.get(
            f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={COIN_API_KEY}",
            timeout=30,
        )
        json_r = response.json()
        price = float(json_r["data"]["priceUsd"])
        return price

    except requests.RequestException:
        sys.exit("There was a problem connecting to the API")


def main():
    n = get_n()
    bitcoin_price = get_bitcoin_price()

    if bitcoin_price:
        print(f"${n * bitcoin_price:,.4f}")


if __name__ == "__main__":
    main()
