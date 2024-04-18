# -*- encoding: utf-8 -*-
from zerocs.common import BaseSetattr


class ServiceBuild(BaseSetattr):

    @staticmethod
    def gen_service_id(name: str) -> str:
        """
        gen service id
        """

    @staticmethod
    def build(func: object, config: dict) -> object:
        """
        build
        """


class WorkBuild(BaseSetattr):

    @staticmethod
    def gen_work_id(name: str) -> str:
        """
        gen work id
        """

    @staticmethod
    def build(func: object, rabbitmq_config: str) -> object:
        """
        build
        """
