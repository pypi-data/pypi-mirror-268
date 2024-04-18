# -*- encoding: utf-8 -*-
import sys

import eventlet

eventlet.monkey_patch()

import json
from argparse import ArgumentParser
from nameko.containers import ServiceContainer

from zerocs.utils import Utils
from zerocs.config import Config
from zerocs.logger import Logger
from zerocs.build import ServiceBuild
from zerocs.observer import ObserverBase


class MultiProcess:

    @staticmethod
    def container_start():
        Config.set_configs(config)
        ObserverBase.attach(Config, subject=Logger)
        ObserverBase.notify(Config)

        module = __import__(config.get('SERVICE_PATH'), globals=globals(), locals=locals(), fromlist=['RpcFunction'])

        func = ServiceBuild.build(func=module.RpcFunction, rabbitmq_config=config.get("RABBITMQ_CONFIG"))
        container = ServiceContainer(service_cls=func, config={"AMQP_URI": config.get('RABBITMQ_CONFIG')})
        container.start()
        container.wait()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--CONFIG', '-CONFIG', help='CONFIG')

    args = parser.parse_args()
    config = Utils.get_b64decode(args.CONFIG)
    config = json.loads(config)

    sys.path.insert(0, config.get('PATH'))

    MultiProcess().container_start()
