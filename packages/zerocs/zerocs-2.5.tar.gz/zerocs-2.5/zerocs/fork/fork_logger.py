import os
import sys
import json
from argparse import ArgumentParser
from zerocs.rabbit import RabbitMq
from zerocs.logger import Logger
from zerocs.utils import Utils


def mq_callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    task_data = json.loads(body.decode())
    Logger.logs_path = os.path.join(config.get('PATH'), 'logs')

    level = task_data['level']
    message = task_data['message']
    service_name = task_data['service_name']

    if level == 'info':
        Logger.logger(service_name).info(f"{message}")

    if level == 'error':
        Logger.logger(service_name).error(f"{message}")

    if level == 'warning':
        Logger.logger(service_name).warning(f"{message}")


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--CONFIG', '-CONFIG', help='CONFIG')

    args = parser.parse_args()
    config = Utils.get_b64decode(args.CONFIG)
    config = json.loads(config)

    sys.path.insert(0, config.get('PATH'))

    RabbitMq.rabbitmq_init(config.get('RABBITMQ_CONFIG'))

    queue_name = f"AsynchronousLog_{Utils.get_ipaddr()}"
    RabbitMq.get_message(queue_name, mq_callback)
