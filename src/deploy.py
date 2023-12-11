from os import environ
from src.contract_deployer import ContractDeployer
from src.printer import Printer
from src.config import Config

PYTHONPATH = environ.get("PYTHONPATH")


def deploy_contract():
    Printer.print("Starting…")
    Printer.print(Config.get_node_url())

    deployer = ContractDeployer("src/contracts/Sample.sol", "Sample")
    deployer.compile()
    deployer.deploy(Config.get_node_url())
    deployer.publish(Config.get_artifacts_file_relpath())

    return deployer.get_artifact()
