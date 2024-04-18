# -*- encoding: utf-8 -*-
from zerocs.common import BaseSetattr


class Interface(BaseSetattr):

    @staticmethod
    def run_service(configs: dict, services: list) -> None:
        """
        Run Service
        """

    @staticmethod
    def init_proxy(configs: dict) -> None:
        """
        Init proxy Boj
        """

    @staticmethod
    def init_rpc_proxy(rpc_config: dict, service_id=None) -> object:
        """
        Init proxy rpc
        """

    @staticmethod
    def get_ipaddr() -> str:
        """
        Get localhost IP
        """

    @staticmethod
    def get_snowflake_id() -> str:
        """
        Get UUID
        """

    @staticmethod
    def rabbitmq_init(config: str) -> None:
        """
        RabbitMQ Init
        """

    @staticmethod
    def restart_service(service_name: str) -> None:
        """
        Restart the node service. If the service is running on multiple nodes,
        only the current node will be restarted
        """

    @staticmethod
    def remote_call_by_name_and_ip(service_name: str, service_ip: str) -> object:
        """
        remote call rpc Interface
        """

    @staticmethod
    def send_message(queue: str, message: dict) -> None:
        """
        Send Queue Message
        """

    @staticmethod
    def get_service_list(query: dict, field: dict, limit: int, skip_no: int) -> tuple:
        """
        get service list
        """

    @staticmethod
    def update_max_work_by_name_and_ip(service_name: str, service_ip: str, max_work: int) -> None:
        """
        Update service max work
        """

    @staticmethod
    def update_service_by_name_and_ip(service_name: str, service_ip: str, data: dict) -> None:
        """
        Update service
        """

    @staticmethod
    def get_stop_tasks_by_task_id(task_id: str) -> list:
        """
        get stop task list
        """

    @staticmethod
    def insert_stop_tasks(task_id: str) -> None:
        """
        stop task
        """

    @staticmethod
    def delete_stop_tasks(task_id: str) -> None:
        """
        del stop task
        """
