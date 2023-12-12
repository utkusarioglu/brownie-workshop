from os import environ
from .contract_deployer import ContractDeployer
from ..config import Config

PYTHONPATH = environ.get("PYTHONPATH")


def deploy_contract():
    deployer = ContractDeployer("src/contracts/Sample.sol", "Sample")
    deployer.compile()
    deployer.deploy(Config.get_node_url())
    deployer.publish(Config.get_artifacts_file_relpath())

    return deployer.get_artifact()
