# -*- encoding: utf-8 -*-
from zerocs.config import Config


@Config
class _Config:
    ObserverList = []
    ConfigDict = {}

    @staticmethod
    def set_config(key: str, value: str) -> None:
        Config.__dict__.setdefault(key, value)

    @staticmethod
    def set_configs(configs: dict) -> None:
        Config.ConfigDict.update(configs)

    @staticmethod
    def get_configs() -> dict:
        return Config.ConfigDict
