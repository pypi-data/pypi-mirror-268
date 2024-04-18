# -*- encoding: utf-8 -*-
from zerocs.config import Config
from zerocs.logger import Logger
from zerocs.rabbit import RabbitMq
from zerocs.database import MongoDB
from zerocs.interface import Interface
from zerocs.observer import ObserverBase
from zerocs.services import ServiceRegistration
from zerocs.utils import Utils, ZeroProxy


@Interface
class _Interface:

    @staticmethod
    def run_service(configs: dict, services: list) -> None:
        Config.set_configs(configs)
        for service in services:
            ServiceRegistration.add_service_object(service)

        ObserverBase.attach(Config, subject=Logger)
        ObserverBase.attach(Config, subject=MongoDB)
        ObserverBase.attach(Config, subject=ServiceRegistration)
        ObserverBase.notify(Config)

    @staticmethod
    def init_proxy(configs: dict) -> None:
        Config.set_configs(configs)
        ObserverBase.attach(Config, subject=RabbitMq)
        ObserverBase.attach(Config, subject=MongoDB)
        ObserverBase.notify(Config)

    # ----- ServiceRegistration -----
    @staticmethod
    def restart_service(service_name: str) -> None:
        ServiceRegistration.restart_service(service_name)

    # ----- RabbitMQ -----
    @staticmethod
    def rabbitmq_init(config: str) -> None:
        RabbitMq.rabbitmq_init(config)

    @staticmethod
    def send_message(queue: str, message: dict) -> None:
        RabbitMq.send_message(queue, message)

    # ----- Utils -----
    @staticmethod
    def init_rpc_proxy(rpc_config: dict, service_id=None) -> object:
        return ZeroProxy.init_rpc_proxy(rpc_config=rpc_config, service_id=service_id)

    @staticmethod
    def remote_call_by_name_and_ip(service_name: str, service_ip: str) -> object:
        service_id = MongoDB.get_service_id_by_name_and_ip(service_name, service_ip)
        return ZeroProxy.init_rpc_proxy(
            rpc_config={"AMQP_URI": Config.get_configs().get('RABBITMQ_CONFIG')},
            service_id=service_id
        )

    @staticmethod
    def get_ipaddr() -> str:
        return Utils.get_ipaddr()

    @staticmethod
    def get_snowflake_id() -> str:
        return Utils.get_snowflake_id()

    # ----- MongoDB -----
    @staticmethod
    def get_service_list(query: dict, field: dict, limit: int, skip_no: int) -> tuple:
        return MongoDB.get_service_list(query, field, limit, skip_no)

    @staticmethod
    def update_max_work_by_name_and_ip(service_name: str, service_ip: str, max_work: int) -> None:
        MongoDB.update_max_work_by_name_and_ip(service_name, service_ip, max_work)

    @staticmethod
    def update_service_by_name_and_ip(service_name: str, service_ip: str, data: dict) -> None:
        MongoDB.update_service_by_name_and_ip(service_name, service_ip, data)

    @staticmethod
    def get_stop_tasks_by_task_id(task_id: str) -> list:
        return MongoDB.get_stop_tasks_by_task_id(task_id)

    @staticmethod
    def insert_stop_tasks(task_id: str) -> None:
        MongoDB.insert_stop_tasks(task_id)

    @staticmethod
    def delete_stop_tasks(task_id: str) -> None:
        MongoDB.delete_stop_tasks(task_id)
