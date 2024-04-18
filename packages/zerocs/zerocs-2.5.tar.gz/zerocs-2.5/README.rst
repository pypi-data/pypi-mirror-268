zerocs Description Document
============================

zerocs: zero config service
+++++++++++++++++++++++++++

1. introduction

    1. zerocs is a distributed task framework with extremely simple configuration.
    Enable users to quickly build distributed task systems with minimal
    configuration and learning costs

    2. The framework has functions such as service management, work management,
    and task management, which can meet most usage scenarios

    3. Note: Version 1.9 is not compatible with version 1.3.
    It is recommended to upgrade to version 1.9 and above

    4. Decentralization starting from version 1.9,
    no longer distinguishing between master and slave nodes

2. start using

    1. Please install RabbitMQ before use,
    rabbitmq official website : https://www.rabbitmq.com,
    It is recommended to use Docker installation during testing::

            docker run -d --hostname my-rabbit --name rabbit \
            -e RABBITMQ_DEFAULT_USER=user \
            -e RABBITMQ_DEFAULT_PASS=password \
            -p 15672:15672 -p 5672:5672 rabbitmq:management

    2. Please install MongoDB before use,
    Installation steps reference : https://docs.mongoing.com/install-mongodb

    3. To use the framework, it is very simple, just refer to zerocs
    in the first line of your startup script
    Please create the corresponding directory and files before starting::

          ├─logs //log directory
          ├─service_list //Directory of microservice codes
          │  │─test
          │  │  ├─test.py
          │  │  ├─test1.py
          ├─main.py  //main
          └─zerocs_test.py //Test Script

    4. main.py ::

        # -*- encoding: utf-8 -*-
        # Master startup file, please refer to zerocs first
        # Flask API is not mandatory and can be connected to other management systems

        import os
        import logging
        from flask_cors import CORS
        from flask import Flask, request

        from zerocs import Main, Interface
        from service_list.test import test, test1

        app = Flask(__name__)
        CORS(app, supports_credentials=True)

        logging.basicConfig(level=logging.ERROR)
        script_path = os.path.dirname(os.path.realpath(__file__))


        class Master:

            def __init__(self):
                config = {
                    "PATH": script_path,
                    "RABBITMQ_CONFIG": "amqp://admin:Rabbit*ads12@127.0.0.1:5672",
                    "MONGODB_CONFIG": "mongodb://admin:123456@127.0.0.1:27017"
                }
                Main.run_master(
                    configs=config,
                    services=[test, test1]
                )

            @staticmethod
            def get_service_list(query: dict, field: dict, limit: int, page: int) -> dict:
                count, data = Interface.get_service_list(query, field, limit, page)
                return {"count": count, "data": data}

            @staticmethod
            def stop_tasks(task_id: str):
                Interface.insert_stop_tasks(task_id)

            @staticmethod
            def remote_call(service_name: str, service_ip: str, method_name: str, **params):
                rpc_proxy = Interface.remote_call_by_name_and_ip(service_name, service_ip)
                return rpc_proxy.remote_call(service_name, method_name, **params)

            @staticmethod
            def send_message(service_name: str, message: dict):
                if 'task_id' in message:
                    Interface.send_message(service_name, message)

            @staticmethod
            def restart_service(service_name: str):
                Interface.restart_service(service_name)


        @app.route("/")
        def index():
            data = _main.get_service_list({}, {"_id": 0}, 10, 0)
            return data


        @app.route("/get_service_list")
        def get_service_list():
            request_json = request.get_json()
            query = request_json['query']
            field = request_json['field']
            limit = request_json['limit']
            page = request_json['page']

            data = _main.get_service_list(query, field, limit, page)
            return data


        @app.route("/restart_service")
        def restart_service():
            request_json = request.get_json()
            service_name = request_json['service_name']
            _main.restart_service(service_name)
            return {"code": 0}


        if __name__ == '__main__':
            _main = Master()
            app.run(host='0.0.0.0', port=5002)

    5. test.py ::

        import time

        class RpcFunction:
            """
            Class Name Not modifiable, Define RPC functions
            """
            service_name = 'test'

            def get_service_name(self, xxx):
                return {"service_name": self.service_name, "param": xxx}


        class WorkFunction:
            """
            Class Name Not modifiable, Work Code
            """

            def __init__(self, task_data):
                """
                :param task_data: Task data JSON format
                """
                logger = self.__getattribute__('logger')
                rpc_proxy = self.__getattribute__('rpc_proxy')

                """
                Call the rpc interface

                data = rpc_proxy.remote_call(service_name, method_name, **params)
                """

    6. zerocs_test.py ::

        # -*- encoding: utf-8 -*-
        import os

        from zerocs import Interface

        script_path = os.path.dirname(os.path.realpath(__file__))

        if __name__ == '__main__':
            config = {
                "PATH": os.path.join(script_path, 'logs'),
                "RABBITMQ_CONFIG": "amqp://admin:Rabbit*ads12@127.0.0.1:5672",
                "MONGODB_CONFIG": "mongodb://admin:123456@127.0.0.1:27017"
            }

            # initialization
            Interface.init_proxy(config)

            # Stop the task
            Interface.insert_stop_tasks('1001')

            # Call the RPC interface
            obj = Interface.remote_call_by_name_and_ip('test', '192.168.0.101')
            print(obj.remote_call('test' ,'get_service_name', param='1111111111'))

            # Issue task message
            Interface.send_message('test', {"task_id": "100", "msg": "xxxxxxxxxxxxxxxx"})


A distributed task scheduling system was completed in just a few steps
======================================================================

Disclaimers
================


+   Before using the zerocs framework, please carefully read and fully understand this statement.
    You can choose not to use the zerocs framework, but once you use the zerocs framework,
    Your usage behavior is deemed to be recognition and acceptance of the entire content of this statement.

+   You promise to use the zerocs framework in a legal and reasonable manner,
    Do not use the zerocs board framework to engage in any illegal or malicious behavior that infringes
    on the legitimate interests of others,
    We will not apply the zerocs framework to any platform that violates Chinese laws and regulations.

+   Any accident, negligence, contract damage, defamation
    This project does not assume any legal responsibility for copyright or intellectual property
    infringement and any losses caused (including but not limited to direct,
    indirect, incidental or derivative losses).

+   The user clearly and agrees to all the contents listed in the terms of this statement,
    The potential risks and related consequences of using the zerocs framework will be entirely borne by the user,
    and this project will not bear any legal responsibility.

+   After reading this disclaimer, any unit or individual should obtain the MIT Open Source License
    Conduct legitimate publishing, dissemination, and use of the zerocs framework within the permitted scope,
    If the breach of this disclaimer clause or the violation of laws and regulations results in legal
    liability (including but not limited to civil compensation and criminal liability),
    the defaulter shall bear the responsibility on their own.

+   The author owns intellectual property rights (including but not limited to trademark rights, patents, Copyrights,
    trade secrets, etc.) of zerocs framework, and the above products are protected by relevant laws and regulations

+   No entity or individual shall apply for intellectual property rights related to
    the zerocs Framework itself without the written authorization of the Author.

+   If any part of this statement is deemed invalid or unenforceable,
    the remaining parts shall remain in full force and effect.
    An unenforceable partial declaration does not constitute a waiver of our
    right to enforce the declaration.

+   This project has the right to make unilateral changes to the terms and attachments of this statement at any time,
    and publish them through message push, webpage announcement, and other means. Once published,
    it will automatically take effect without the need for separate notice;
    If you continue to use this statement after the announcement of changes,
    it means that you have fully read, understood, and accepted the revised statement.