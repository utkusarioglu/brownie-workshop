from web3 import Web3
from config import Config


def get_instance():
    web3 = Web3(Web3.HTTPProvider(Config.get_node_url()))
    artifacts = Config.get_artifacts()
    address = artifacts["address"]
    abi = artifacts["abi"]
    instance = web3.eth.contract(address, abi=abi)
    return instance
