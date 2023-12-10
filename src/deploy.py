#!/home/python/venv/main/bin/python

from contract_deployer import ContractDeployer
from printer import Printer
from config import Config


def main():
    Printer.print("Starting…")
    Printer.print(Config.get_node_url())

    deployer = ContractDeployer("src/contracts/Sample.sol", "Sample")
    deployer.compile()
    deployer.deploy(Config.get_node_url())
    deployer.publish(Config.get_artifacts_file_relpath())


if __name__ == "__main__":
    main()
