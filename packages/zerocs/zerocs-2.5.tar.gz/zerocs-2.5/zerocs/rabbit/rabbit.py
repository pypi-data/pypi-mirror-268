# -*- encoding: utf-8 -*-

import json
import pika
import logging
from zerocs.rabbit import RabbitMq


@RabbitMq
class _RabbitMq:
    mq_config = None
    config_key = 'RABBITMQ_CONFIG'

    @staticmethod
    def get_mq_channel(config):
        host = config.split('@')[1].split(':')[0]
        port = config.split('@')[1].split(':')[1]

        user = config.split('@')[0].split('//')[1].split(':')[0]
        passwd = config.split('@')[0].split('//')[1].split(':')[1]

        credentials = pika.PlainCredentials(user, passwd)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host, port=port, virtual_host='/', credentials=credentials, heartbeat=0))
        return connection.channel()

    @staticmethod
    def rabbitmq_init(config):
        RabbitMq.mq_config = config

    @staticmethod
    def update(subject):
        config = subject.get_configs()
        if RabbitMq.config_key in config:
            mq_config = config.get(RabbitMq.config_key)
            RabbitMq.rabbitmq_init(mq_config)

    @staticmethod
    def create_queue(queue):
        try:
            mq_channel = RabbitMq.get_mq_channel(RabbitMq.mq_config)
            mq_channel.queue_declare(queue=queue)
            return mq_channel
        except Exception as e:
            logging.error(e)
            return False

    @staticmethod
    def send_message(queue, message):
        mq_channel = RabbitMq.create_queue(queue=queue)
        if type(message) is not str:
            message = json.dumps(message)
        mq_channel.basic_publish(exchange='', routing_key=queue, body=message)

    @staticmethod
    def get_message(queue, callback):
        mq_channel = RabbitMq.create_queue(queue=queue)
        mq_channel.basic_consume(on_message_callback=callback, queue=queue, auto_ack=False)
        mq_channel.start_consuming()
