# -*- encoding: utf-8 -*-
from zerocs.common import BaseSetattr


class Config(BaseSetattr):
    ObserverList = []
    ConfigDict = {}

    @staticmethod
    def set_config(key: str, value: str) -> None:
        """
        Set Config
        """

    @staticmethod
    def set_configs(configs: dict) -> None:
        """
        Set Configs
        """

    @staticmethod
    def get_configs() -> dict:
        """
        Get Configs
        """
