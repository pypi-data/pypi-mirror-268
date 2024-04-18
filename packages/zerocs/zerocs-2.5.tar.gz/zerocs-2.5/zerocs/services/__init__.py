# -*- encoding: utf-8 -*-
from zerocs.common import BaseSetattr


class ServiceRegistration(BaseSetattr):
    ServiceList = []

    @staticmethod
    def add_service_object(service: object) -> None:
        """
        add service
        """

    @staticmethod
    def get_service_object() -> list:
        """
        get services
        """

    @staticmethod
    def restart_service(service_name: str) -> None:
        """
        restart service
        """

    @staticmethod
    def update(subject: object) -> None:
        """
        ObserverBase Update
        """
