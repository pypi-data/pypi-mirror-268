# -*- encoding: utf-8 -*-
from zerocs.common import BaseSetattr


class Fork(BaseSetattr):

    @staticmethod
    def fork_logger(config: dict) -> None:
        """
        fork logger process
        """

    @staticmethod
    def fork_service(service_list: list, config: dict) -> object:
        """
        fork service process
        """

    @staticmethod
    def fork_work(work_list: list, config: dict) -> object:
        """
        fork work process
        """
