from json import loads
from os import environ
from dotenv import load_dotenv

load_dotenv(".env")


class Config:
    @staticmethod
    def get_node_url() -> str:
        HOST_IP = environ.get("HOST_IP")
        if not HOST_IP:
            raise ValueError("HOST_IP_NOT_DEFINED")

        HOST_PORT = environ.get("HOST_PORT")
        if not HOST_PORT:
            raise ValueError("HOST_PORT_NOT_DEFINED")

        return f"http://{HOST_IP}:{HOST_PORT}"

    @staticmethod
    def get_artifacts_file_relpath() -> str:
        ARTIFACTS_FILE = environ.get("ARTIFACTS_FILE")
        if not ARTIFACTS_FILE:
            raise ValueError("ARTIFACTS_FILE_NOT_DEFINED")
        return ARTIFACTS_FILE

    @staticmethod
    def get_artifacts() -> dict[str, str]:
        return loads(open(Config.get_artifacts_file_relpath()).read())
