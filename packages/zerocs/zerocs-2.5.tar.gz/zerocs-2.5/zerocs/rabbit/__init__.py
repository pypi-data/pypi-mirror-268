# -*- encoding: utf-8 -*-
from zerocs.common import BaseSetattr


class RabbitMq(BaseSetattr):
    mq_config = None
    config_key = None

    @staticmethod
    def get_mq_channel(config):
        """
        Get RabbitMQ Channel
        """

    @staticmethod
    def rabbitmq_init(config):
        """
        RabbitMQ Init
        """

    @staticmethod
    def create_queue(queue):
        """
        Create MQ Queue
        """

    @staticmethod
    def send_message(queue, message):
        """
        Send Queue Message
        """

    @staticmethod
    def get_message(queue, callback):
        """
        Get Queue Message
        """
