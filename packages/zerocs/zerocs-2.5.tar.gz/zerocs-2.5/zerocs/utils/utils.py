# -*- encoding: utf-8 -*-

import os
import pytz
import time
import base64
import socket
import hashlib
import datetime
import subprocess

from zerocs.utils.rpc_proxy import MyClusterRpcProxy
from zerocs.utils import Utils, ZeroProxy, GetClusterRpcProxy


class SnowflakeID:
    work_bits = 5
    datacenter_bits = 5
    sequence_bits = 12

    max_work_id = -1 ^ (-1 << work_bits)
    max_datacenter_id = -1 ^ (-1 << datacenter_bits)

    work_id_shift = sequence_bits
    datacenter_shift = sequence_bits + work_bits
    timestamp_left_shift = sequence_bits + work_bits + datacenter_bits
    sequence_mask = -1 ^ (-1 << sequence_bits)

    timestamp = 1000000000000
    last_timestamp = -1
    sequence = 0

    @staticmethod
    def get_timestamp_millimeter():
        timestamp = int(round(time.time() * 1000))
        return timestamp

    def get_timestamp_next_second(self, last_timestamp):
        timestamp = self.get_timestamp_millimeter()
        while timestamp <= last_timestamp:
            timestamp = self.get_timestamp_millimeter()
        return timestamp

    def get_sequence(self, sequence, last_timestamp, sequence_mask):
        timestamp = self.get_timestamp_millimeter()
        if timestamp < last_timestamp:
            raise Exception('error')
        if timestamp == last_timestamp:
            sequence = (sequence + 1) & sequence_mask
            if sequence == 0:
                timestamp = self.get_timestamp_next_second(last_timestamp)
        else:
            sequence = 0
        return sequence, timestamp

    def get_snowflake_id(self):
        time_ns = int(time.time_ns() / 1000)
        datacenter_id = int(str(time_ns)[-3:])
        worker_id = int(str(time_ns)[-3:])
        did_wid = int(str(time_ns)[-3:])

        if did_wid > 0:
            datacenter_id = did_wid >> 5
            worker_id = did_wid ^ (datacenter_id << 5)

        if worker_id > self.max_work_id or worker_id < 0:
            raise ValueError('worker_id number overstep the boundary')

        if datacenter_id > self.max_datacenter_id or datacenter_id < 0:
            raise ValueError('datacenter_id number overstep the boundary')

        self.sequence, timestamp = self.get_sequence(self.sequence, self.last_timestamp, self.sequence_mask)

        self.last_timestamp = timestamp
        new_id = ((timestamp - self.timestamp) << self.timestamp_left_shift) | \
                 (datacenter_id << self.datacenter_shift) | \
                 (worker_id << self.work_id_shift) | self.sequence
        return f'ID_{new_id}'


class Times:

    @staticmethod
    def get_time_str(fmt: str, timezone: str) -> str:
        tz = pytz.timezone(timezone)
        current_time = datetime.datetime.now(tz)
        return current_time.strftime(fmt)


@Utils
class _Utils:
    obj = SnowflakeID()

    @staticmethod
    def get_b64encode(encoded_str: str) -> str:
        encoded_bytes = f"{encoded_str}".encode('utf-8')
        encrypted_data = base64.b64encode(encoded_bytes)
        return encrypted_data.decode()

    @staticmethod
    def get_b64decode(encrypted_str: str) -> str:
        decoded_bytes = base64.b64decode(encrypted_str)
        return decoded_bytes.decode('utf-8')

    @staticmethod
    def get_ipaddr() -> str:
        socket_tools = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_tools.connect(("8.8.8.8", 80))
        return socket_tools.getsockname()[0]

    @staticmethod
    def get_service_id(service_name: str, service_ip: str) -> str:
        service_str = f"{service_ip}_{service_name}"
        return hashlib.md5(service_str.encode('utf-8')).hexdigest()

    @staticmethod
    def is_port_open(work_ip: str, port: int) -> bool:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((work_ip, int(port)))
            s.shutdown(2)
            return False
        except IOError:
            return True

    @staticmethod
    def get_snowflake_id() -> str:
        return Utils.obj.get_snowflake_id()

    @staticmethod
    def get_time_str(fmt: str, timezone: str) -> str:
        return Times().get_time_str(fmt, timezone)

    @staticmethod
    def get_python_path() -> str:
        if os.name == 'nt':
            cmd = subprocess.Popen('py -0p', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = cmd.communicate()
            out = out.decode().split('\r\n')

            _paths = None
            for i in out:
                if i != '':
                    li = [j for j in i.split(' ') if j != '']
                    version = li[0].split('-')[1]
                    path = li[1]
                    if float(version) >= 3.7:
                        _paths = path
                        break
        else:
            _paths = 'python3'

        return _paths


@GetClusterRpcProxy
class _GetClusterRpcProxy:

    @staticmethod
    def get_cluster_rpc_proxy(config: dict):
        return MyClusterRpcProxy(config)


@ZeroProxy
class _ZeroProxy:
    rpc_config = None
    service_id = None

    @staticmethod
    def init_rpc_proxy(rpc_config: dict, service_id=None) -> object:
        ZeroProxy.rpc_config = rpc_config
        ZeroProxy.service_id = service_id
        return ZeroProxy

    @staticmethod
    def remote_call(service_name: str, method_name: str, **params):
        rpc_obj = GetClusterRpcProxy.get_cluster_rpc_proxy(ZeroProxy.rpc_config)

        if ZeroProxy.service_id is None:
            obj = getattr(rpc_obj.start(), service_name)
            func = getattr(obj, method_name)
            data = func(**params)
        else:
            obj = getattr(rpc_obj.start(), ZeroProxy.service_id)
            func = getattr(obj, method_name)
            data = func(**params)
        return data
