# -*- encoding: utf-8 -*-

import os
import sys
import json
import time
import logging
import multiprocessing
from argparse import ArgumentParser

from zerocs.config import Config
from zerocs.build import WorkBuild
from zerocs.rabbit import RabbitMq
from zerocs.database import MongoDB
from zerocs.observer import ObserverBase
from zerocs.logger import AsynchronousLog, Logger
from zerocs.utils import ZeroProxy, Utils

max_cpu_count = multiprocessing.cpu_count() - 3


class MultiProcessWork:

    def __init__(self, function, work_name, work_ip, config):
        self.config = config
        self.work_ip = work_ip
        self.function = function
        self.work_name = work_name

        MongoDB.init(config.get('MONGODB_CONFIG'))
        RabbitMq.rabbitmq_init(config.get('RABBITMQ_CONFIG'))

        Logger.logs_path = os.path.join(self.config.get('PATH'), 'logs')

        self.rpc_config = {"AMQP_URI": self.config.get('RABBITMQ_CONFIG')}
        self.logger = Logger.logger(self.work_name)

    def run_task_func_win(self, function, task_data, run_id):
        sys.path.insert(0, self.config.get('PATH'))
        RabbitMq.rabbitmq_init(self.config.get('RABBITMQ_CONFIG'))
        # logger = AsynchronousLog.init_asynchronous_log(self.work_name, self.work_ip)

        Logger.logs_path = os.path.join(self.config.get('PATH'), 'logs')
        logger = Logger.logger(self.work_name)

        setattr(function, 'logger', logger)
        setattr(function, 'work_ip', self.work_ip)
        setattr(function, 'work_name', self.work_name)
        setattr(function, 'rpc_proxy', ZeroProxy.init_rpc_proxy(self.rpc_config))

        try:
            function(task_data)
        except Exception as e:
            logger.error(f'{e}')

        MongoDB.init(self.config.get('MONGODB_CONFIG'))
        MongoDB.delete_run_task(service_name=self.work_name, service_ip=self.work_ip, task_id=run_id)

    def run_task_func_linux(self, function, task_data, run_id):
        setattr(function, 'logger', self.logger)
        setattr(function, 'work_ip', self.work_ip)
        setattr(function, 'work_name', self.work_name)
        setattr(function, 'rpc_proxy', ZeroProxy.init_rpc_proxy(self.rpc_config))

        try:
            function(task_data)
        except Exception as e:
            self.logger.error(f'{e}')

        MongoDB.delete_run_task(service_name=self.work_name, service_ip=self.work_ip, task_id=run_id)

    def mq_callback(self, ch, method, properties, body):
        ch.basic_ack(delivery_tag=method.delivery_tag)
        task_data = json.loads(body.decode())
        if 'task_id' in task_data:
            server = MongoDB.get_service_by_name_and_ip(service_name=self.work_name, service_ip=self.work_ip)
            max_work = server.get('max_work')
            run_work = len(server.get('run_work'))

            if run_work < max_work and run_work < max_cpu_count:
                _stops = MongoDB.get_stop_tasks_by_task_id(task_data['task_id'])
                if len(_stops) < 1:
                    run_id = Utils.get_snowflake_id()

                    if os.name == 'nt':
                        process = multiprocessing.Process(
                            target=self.run_task_func_win,
                            args=(self.function, task_data, run_id,)
                        )
                    else:
                        process = multiprocessing.Process(
                            target=self.run_task_func_linux,
                            args=(self.function, task_data, run_id,)
                        )

                    process.start()
                    MongoDB.update_run_task(service_name=self.work_name, service_ip=self.work_ip, task_id=run_id)
            else:
                time.sleep(0.2)
                ch.basic_publish(body=body, exchange='', routing_key=self.work_name)

    def start_work(self):
        count = 0
        while True:
            try:
                logging.info(f'work start, work_name == {self.work_name}, count = {count}')
                RabbitMq.get_message(self.work_name, self.mq_callback)
            except Exception as e:
                logging.error(e)
            count += 1


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--CONFIG', '-CONFIG', help='CONFIG')
    parser.add_argument('--SERVICE', '-SERVICE', help='SERVICE')

    args = parser.parse_args()
    configs = Utils.get_b64decode(args.CONFIG)
    configs = json.loads(configs)

    sys.path.insert(0, configs.get('PATH'))

    Config.set_configs(configs)
    ObserverBase.attach(Config, subject=RabbitMq)
    ObserverBase.attach(Config, subject=MongoDB)
    ObserverBase.notify(Config)

    module = __import__(configs.get('SERVICE_PATH'), globals=globals(), locals=locals(), fromlist=['RpcFunction'])
    func = WorkBuild.build(func=module.WorkFunction, rabbitmq_config=configs.get('RABBITMQ_CONFIG'))

    work_ip_ = func.__dict__.get("work_ip")
    work_name_ = func.__dict__.get("work_name")
    pool = multiprocessing.pool.Pool(processes=max_cpu_count)

    obj = MultiProcessWork(
        function=func,
        work_ip=work_ip_,
        config=configs,
        work_name=work_name_
    )
    obj.start_work()
