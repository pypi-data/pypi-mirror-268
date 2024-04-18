# -*- encoding: utf-8 -*-
from zerocs.common import BaseSetattr


class Logger(BaseSetattr):
    log_obj = None
    logs_path = None
    format_str = None
    config_key = None

    @staticmethod
    def init():
        """
        init logger
        """

    @staticmethod
    def logger(filename):
        """
        logger, filename: log file
        """


class AsynchronousLog(BaseSetattr):
    service_ip = None
    service_name = None
    queue_name = None

    @staticmethod
    def init_asynchronous_log(service_name: str, service_ip: str):
        """
        init_asynchronous_log
        """

    @staticmethod
    def info(message: str):
        """
        logger.info
        """

    @staticmethod
    def error(message: str):
        """
        logger.error
        """

    @staticmethod
    def warning(message: str):
        """
        logger.warning
        """
