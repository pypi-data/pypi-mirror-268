# -*- encoding: utf-8 -*-
import logging

from zerocs.verification import Verification


@Verification
class _Verification:

    @staticmethod
    def verification_config(config: dict) -> bool:
        _config_list = ['RABBITMQ_CONFIG', 'MONGODB_CONFIG', 'PATH']
        for _c in _config_list:
            if _c not in config:
                logging.error(f'Missing parameter {_c}')
                return False
        return True
