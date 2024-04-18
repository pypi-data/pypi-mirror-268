# -*- encoding: utf-8 -*-
from zerocs.common import BaseSetattr


class MongoDB(BaseSetattr):
    db_config = None
    mongo_interface = None

    database = None
    table_tasks = None
    table_system = None
    table_services = None
    table_stop_task = None
    config_key = None

    @staticmethod
    def init(db_config: str) -> None:
        """
        Init Mongo Obj
        """

    @staticmethod
    def update(subject: object) -> None:
        """
        ObserverBase Update
        """

    @staticmethod
    def get_service_by_id(service_id: str) -> dict:
        """
        Get Service BY ServiceID
        """

    @staticmethod
    def get_service_list(query: dict, field: dict, limit: int, skip_no: int) -> tuple:
        """
        get service list
        """

    @staticmethod
    def get_service_by_name_and_ip(service_name: str, service_ip: str) -> dict:
        """
        Get Service BY ServiceID And ServiceIP
        """

    @staticmethod
    def get_service_id_by_name_and_ip(service_name: str, service_ip: str) -> str:
        """
        Get ServiceID BY ServiceID And ServiceIP
        """

    @staticmethod
    def get_service_by_name(service_name: str) -> list:
        """
        Get Service BY service name
        """

    @staticmethod
    def update_service_by_service_id(service_id: str, data: dict) -> None:
        """
        Update service
        """

    @staticmethod
    def update_run_task(service_name: str, service_ip: str, task_id: str) -> None:
        """
        update running task list
        """

    @staticmethod
    def delete_run_task(service_name: str, service_ip: str, task_id: str) -> None:
        """
        Remove from running task list
        """

    @staticmethod
    def update_service_by_name_and_ip(service_name: str, service_ip: str, data: dict) -> None:
        """
        Update service
        """

    @staticmethod
    def update_max_work_by_name_and_ip(service_name: str, service_ip: str, max_work: int) -> None:
        """
        Update service max work
        """

    @staticmethod
    def insert_service(service_name: str, service_id: str, service_ip: str, max_work: int, run_work: list,
                       update_time: str, api_list: list, service_pid: int) -> None:
        """
        insert service
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
