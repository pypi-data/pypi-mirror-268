# -*- encoding: utf-8 -*-
import inspect
import logging
import os

from nameko.rpc import rpc
from zerocs.utils import Utils
from zerocs.rabbit import RabbitMq
from zerocs.logger import AsynchronousLog, Logger

from zerocs.build import ServiceBuild, WorkBuild


class DefaultFunc:
    logger = None
    service_id = None

    @rpc
    def get_service_id(self):
        return self.service_id


class Build:

    def __init__(self, build):
        self.build = build

    def setattr(self, name, val):
        setattr(self.build, name, val)
        logging.debug(f'add func {name}')


@ServiceBuild
class _ServiceBuild:

    @staticmethod
    def gen_service_id(name):
        _ip = Utils.get_ipaddr()
        return Utils.get_service_id(name, _ip)

    @staticmethod
    def build(func: object, config: dict) -> object:
        _apis = {}
        build = Build(DefaultFunc)

        for _name in func.__dict__:
            if _name.startswith('__') is False:
                _value = func.__dict__.get(_name)
                if type(_value) in [type(lambda: None)]:
                    _value = rpc(_value)
                    _param = []
                    sig = inspect.signature(_value)
                    for name, param in sig.parameters.items():
                        if name != 'self':

                            default_value = param.default
                            if param.default is inspect.Parameter.empty:
                                default_value = None

                            _param.append({"param_name": name, "default_value": default_value})

                    _apis.setdefault(_name, _param)

                build.setattr(_name, func.__dict__.get(_name))

        name = func.__dict__.get('service_name')
        if name is None:
            logging.warning('service_name is None')

        Logger.logs_path = os.path.join(config.get('PATH'), 'logs')
        build.setattr('logger', Logger.logger(name))

        # RabbitMq.rabbitmq_init(config.get('RABBITMQ_CONFIG'))
        # build.setattr('logger', AsynchronousLog.init_asynchronous_log(name, service_ip))

        service_ip = Utils.get_ipaddr()
        build.setattr('apis', _apis)
        build.setattr('service_ip', service_ip)
        build.setattr('rabbitmq_config', config.get('RABBITMQ_CONFIG'))
        build.setattr('service_id', ServiceBuild.gen_service_id(name))
        build.setattr('name', ServiceBuild.gen_service_id(name))

        return build.build


@WorkBuild
class _WorkBuild:

    @staticmethod
    def gen_work_id(name):
        _ip = Utils.get_ipaddr()
        return Utils.get_service_id(f'{name}_work', _ip)

    @staticmethod
    def build(func: object, rabbitmq_config: str) -> object:
        work_ip = Utils.get_ipaddr()

        name = func.__module__.split('.')[-1]
        setattr(func, 'work_ip', work_ip)
        setattr(func, 'rabbitmq_config', rabbitmq_config)
        setattr(func, 'work_id', WorkBuild.gen_work_id(name))
        setattr(func, 'work_name', name)

        return func
