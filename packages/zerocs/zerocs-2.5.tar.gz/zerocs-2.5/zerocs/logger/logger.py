# -*- encoding: utf-8 -*-
import os
import logging
from logging import handlers
from zerocs.utils import Utils
from zerocs.rabbit import RabbitMq
from zerocs.logger import Logger, AsynchronousLog


@Logger
class _Logger:
    log_obj = None
    logs_path = None
    config_key = 'PATH'
    format_str = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

    @staticmethod
    def init():
        if os.path.exists(Logger.logs_path) is False:
            os.mkdir(Logger.logs_path)

        Logger.log_obj = logging.getLogger(Utils.get_snowflake_id())
        Logger.log_obj.setLevel(logging.INFO)

    @staticmethod
    def logger(filename):
        Logger.init()
        th = handlers.TimedRotatingFileHandler(
            filename=f'{Logger.logs_path}/{filename}', when='MIDNIGHT', backupCount=7, encoding='utf-8')
        th.suffix = "%Y-%m-%d.log"
        th.setFormatter(Logger.format_str)
        Logger.log_obj.addHandler(th)
        return Logger.log_obj

    @staticmethod
    def update(subject):
        config = subject.get_configs()
        if Logger.config_key in config:
            Logger.logs_path = os.path.join(config.get(Logger.config_key), 'logs')


@AsynchronousLog
class _AsynchronousLog:
    service_ip = None
    service_name = None
    queue_name = None

    @staticmethod
    def init_asynchronous_log(service_name: str, service_ip: str):
        AsynchronousLog.service_name = service_name
        AsynchronousLog.service_ip = service_ip
        AsynchronousLog.queue_name = f"AsynchronousLog_{service_ip}"
        return AsynchronousLog

    @staticmethod
    def info(message: str):
        message = {"message": message, "level": "info", "service_name": AsynchronousLog.service_name}
        RabbitMq.send_message(AsynchronousLog.queue_name, message)

    @staticmethod
    def error(message: str):
        message = {"message": message, "level": "error", "service_name": AsynchronousLog.service_name}
        RabbitMq.send_message(AsynchronousLog.queue_name, message, )

    @staticmethod
    def warning(message: str):
        message = {"message": message, "level": "warning", "service_name": AsynchronousLog.service_name}
        RabbitMq.send_message(AsynchronousLog.queue_name, message)
