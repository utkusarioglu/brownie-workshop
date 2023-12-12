#!/home/python/venv/main/bin/python

from dotenv import load_dotenv
from os import environ
from web3 import Web3

load_dotenv(".env")

INFURA_API_KEY = environ.get("INFURA_API_KEY")
INFURA_SEPOLIA_URL = f"https://sepolia.infura.io/v3/{INFURA_API_KEY}"


def get_account_alias(account) -> str:
    return account[0:4] + "…" + account[-5:-1]


def log_transaction(
    transaction_from: str, transaction_to: str, balance_wei: int
):
    balance_ether = Web3.from_wei(balance_wei, "ether")
    account_alias_from = get_account_alias(transaction_from)
    account_alias_to = get_account_alias(transaction_to)

    log_text = [
        account_alias_from,
        " -> ",
        account_alias_to,
        ": ",
        format(balance_ether, ".2f").rjust(6, " "),
        " ETH",
    ]
    print("".join(log_text))


def main() -> str:
    w3 = Web3(Web3.HTTPProvider(INFURA_SEPOLIA_URL))
    latest = w3.eth.get_block("latest")

    if "transactions" in latest:
        transaction_count = len(latest["transactions"])
        print(f"Transaction count: {transaction_count}")

        for item in latest["transactions"][0:3]:
            transaction = w3.eth.get_transaction(item)
            transaction_from = transaction.get("from", "")
            transaction_to = transaction.get("to", "")
            balance_wei = w3.eth.get_balance(transaction_from)

            log_transaction(transaction_from, transaction_to, balance_wei)

    return "-done"


if __name__ == "__main__":
    print(main())
