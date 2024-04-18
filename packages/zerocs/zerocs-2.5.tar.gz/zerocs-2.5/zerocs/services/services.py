# -*- encoding: utf-8 -*-
from zerocs.fork import Fork
from zerocs.config import Config
from zerocs.services import ServiceRegistration


@ServiceRegistration
class _ServiceRegistration:
    ServiceList = []

    @staticmethod
    def add_service_object(service: object) -> None:
        ServiceRegistration.ServiceList.append(service)

    @staticmethod
    def get_service_object() -> list:
        return ServiceRegistration.ServiceList

    @staticmethod
    def restart_service(service_name: str) -> None:
        _temporary = []
        for service in ServiceRegistration.ServiceList:
            _name = service.__name__.split('.')[-1]
            if _name == service_name:
                _temporary.append(service)

        Fork.fork_service(_temporary, Config.get_configs())
        Fork.fork_work(_temporary, Config.get_configs())

    @staticmethod
    def update(subject: object) -> None:
        config = subject.get_configs()
        # Fork.fork_logger(config)
        Fork.fork_service(ServiceRegistration.ServiceList, config)
        Fork.fork_work(ServiceRegistration.ServiceList, config)
