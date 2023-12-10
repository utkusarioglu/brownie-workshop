from solcx import compile_files
from web3 import Web3
from json import dumps


class ContractDeployer:
    def __init__(self, source_relpath: str, contract_name: str) -> None:
        self.source_relpath = source_relpath
        self.contract_name = contract_name
        self.identifier = f"{source_relpath}:{contract_name}"

    def compile(self):
        self.compiled = compile_files(
            source_files=[self.source_relpath], output_values=["abi", "bin"]
        )[self.identifier]

    def deploy(self, node_url: str) -> None:
        web3 = Web3(Web3.HTTPProvider(node_url))
        deployer = web3.eth.contract(
            abi=self.compiled.get("abi", ""),
            bytecode=self.compiled.get("bin", ""),
        )
        deploy_tx_hash = deployer.constructor().transact()
        deploy_tx_receipt = web3.eth.wait_for_transaction_receipt(
            deploy_tx_hash
        )
        self.contract_address = deploy_tx_receipt["contractAddress"]

    def publish(self, publish_path: str) -> None:
        with open(publish_path, "w+") as artifact_file:
            artifact = {
                "address": self.contract_address,
                "abi": self.compiled["abi"],
                "bin": self.compiled["bin"],
            }
            artifact_file.write(dumps(artifact))
