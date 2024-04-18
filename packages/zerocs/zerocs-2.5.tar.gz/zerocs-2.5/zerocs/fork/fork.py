# -*- encoding: utf-8 -*-

import os
import copy
import json
import signal
import subprocess
import multiprocessing
from zerocs.fork import Fork
from zerocs.fork.fork_work import MultiProcessWork
from zerocs.utils import Utils
from zerocs.database import MongoDB
from zerocs.build import ServiceBuild, WorkBuild

current_directory = os.path.dirname(os.path.abspath(__file__))


def print_exception(e):
    pass


@Fork
class _Fork:

    @staticmethod
    def fork_logger(config: dict) -> None:
        _python = Utils.get_python_path()
        _script = os.path.join(current_directory, 'fork_logger.py')

        config_md5 = Utils.get_b64encode(json.dumps(config, ensure_ascii=False))

        cmd = f'{_python} {_script} --CONFIG {config_md5}'

        if os.name == 'nt':
            subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        else:
            subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    @staticmethod
    def fork_service(service_list: list, config: dict) -> None:
        for service in service_list:
            func = ServiceBuild.build(func=service.RpcFunction, config=config)
            _python = Utils.get_python_path()
            _script = os.path.join(current_directory, 'fork_service.py')

            _apis = func.__dict__.get('apis')
            _service_id = func.__dict__.get('service_id')
            _service_ip = func.__dict__.get('service_ip')
            _service_name = func.__dict__.get('service_name')

            _server = MongoDB.get_service_by_name_and_ip(service_name=_service_name, service_ip=_service_ip)
            _service_pid = _server.get("service_pid")

            try:
                os.kill(_service_pid, signal.SIGTERM)
            except Exception as e:
                print_exception(e)

            _config = copy.deepcopy(config)
            _config['SERVICE_PATH'] = service.__name__
            config_md5 = Utils.get_b64encode(json.dumps(_config, ensure_ascii=False))

            cmd = f'{_python} {_script} --CONFIG {config_md5}'

            if os.name == 'nt':
                process = subprocess.Popen(
                    cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            else:
                process = subprocess.Popen(
                    cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

            MongoDB.insert_service(
                api_list=_apis,
                service_id=_service_id,
                service_ip=_service_ip,
                max_work=1, run_work=[],
                service_pid=process.pid,
                service_name=_service_name,
                update_time=Utils.get_time_str('%Y-%m-%d %H:%M:%S', 'Asia/Shanghai'),
            )

    @staticmethod
    def fork_work(work_list: list, config: dict) -> None:
        for work in work_list:
            func = WorkBuild.build(func=work.WorkFunction, rabbitmq_config=config.get('RABBITMQ_CONFIG'))
            _python = Utils.get_python_path()
            _script = os.path.join(current_directory, 'fork_work.py')

            _work_id = func.__dict__.get('work_id')
            _work_ip = func.__dict__.get('work_ip')
            _work_name = func.__dict__.get('work_name')

            _work = MongoDB.get_service_by_name_and_ip(service_name=_work_name, service_ip=_work_ip)
            _work_pid = _work.get("work_pid")
            try:
                os.kill(_work_pid, signal.SIGTERM)
            except Exception as e:
                print_exception(e)

            _config = copy.deepcopy(config)
            _config['SERVICE_PATH'] = work.__name__
            config_md5 = Utils.get_b64encode(json.dumps(_config, ensure_ascii=False))

            cmd = f'{_python} {_script} --CONFIG {config_md5} --SERVICE {_work_name}'

            if os.name == 'nt':
                process = subprocess.Popen(
                    cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            else:
                obj = MultiProcessWork(
                    function=func,
                    work_ip=_work_ip,
                    config=config,
                    work_name=_work_name
                )
                process = multiprocessing.Process(target=obj.start_work)
                process.start()

            data = {"work_id": _work_id, "work_pid": process.pid}
            MongoDB.update_service_by_name_and_ip(service_name=_work_name, service_ip=_work_ip, data=data)
