#!/home/python/venv/main/bin/python

from dotenv import load_dotenv
from os import environ
from web3 import Web3

load_dotenv(".env")

INFURA_API_KEY = environ.get("INFURA_API_KEY")
INFURA_SEPOLIA_URL = f"https://sepolia.infura.io/v3/${INFURA_API_KEY}"


def main() -> str    :
    Web3.HTTPProvider()

if __name__ == "__main__":
  print(main())
