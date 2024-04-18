# -*- encoding: utf-8 -*-
from zerocs.main import Main
from zerocs.interface import Interface
from zerocs.verification import Verification


@Main
class _Main:

    @staticmethod
    def run_master(configs: dict, services: list):
        configs.setdefault('IS_MASTER', True)
        verification = Verification.verification_config(configs)
        if verification:
            Interface.run_service(configs, services)

    @staticmethod
    def run_slave(configs: dict, services: list):
        configs.setdefault('IS_MASTER', False)
        verification = Verification.verification_config(configs)
        if verification:
            Interface.run_service(configs, services)
