# -*- encoding: utf-8 -*-
from zerocs.common import BaseSetattr


class GetClusterRpcProxy(BaseSetattr):

    @staticmethod
    def get_cluster_rpc_proxy(config: dict):
        """
        get_cluster_rpc_proxy
        """


class ZeroProxy(BaseSetattr):
    rpc_config = None
    service_id = None

    @staticmethod
    def init_rpc_proxy(rpc_config: dict, service_id=None) -> object:
        """
        init_rpc_proxy
        """

    @staticmethod
    def remote_call(service_name: str, method_name: str, **params):
        """
        remote_call
        """


class Utils(BaseSetattr):
    obj = None

    @staticmethod
    def get_b64encode(encoded_str: str) -> str:
        """
        b64encode
        """

    @staticmethod
    def get_b64decode(encrypted_str: str) -> str:
        """
        b64decode
        """

    @staticmethod
    def get_ipaddr() -> str:
        """
        Get localhost IP
        """

    @staticmethod
    def get_service_id(service_name: str, service_ip: str) -> str:
        """
        Get ServiceID , service_name+service_ip.md5
        """

    @staticmethod
    def is_port_open(work_ip: str, port: int) -> bool:
        """
        Is Port Open
        """

    @staticmethod
    def get_snowflake_id() -> str:
        """
        Get UUID
        """

    @staticmethod
    def get_time_str(fmt: str, timezone: str) -> str:
        """
        get time
        """

    @staticmethod
    def get_python_path() -> str:
        """
        get python bin path
        """
