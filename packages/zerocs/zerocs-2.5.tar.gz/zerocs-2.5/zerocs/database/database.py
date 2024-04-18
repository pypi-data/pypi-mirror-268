# -*- encoding: utf-8 -*-
import pymongo

from zerocs.database import MongoDB


class MongodbBase:

    def __init__(self, obj):
        self.obj = obj

    def get_collection(self, db_name: str, collection_name: str) -> object:
        return self.obj[db_name][collection_name]

    def insert_data(self, db_name: str, collection_name: str, data: dict):
        collection = self.get_collection(db_name, collection_name)
        collection.insert_one(data)
        return None

    def update_many(self, db_name: str, collection_name: str, query: dict, update_data: dict):
        collection = self.get_collection(db_name, collection_name)
        collection.update_many(query, {"$set": update_data})
        return None

    def push_many(self, db_name: str, collection_name: str, query: dict, update_data: dict):
        collection = self.get_collection(db_name, collection_name)
        collection.update_many(query, {"$push": update_data})
        return None

    def pull_many(self, db_name: str, collection_name: str, query: dict, update_data: dict):
        collection = self.get_collection(db_name, collection_name)
        collection.update_many(query, {"$pull": update_data})
        return None

    def get_data(self, db_name: str, collection_name: str, query: dict, filed: dict):
        collection = self.get_collection(db_name, collection_name)
        data = collection.find(query, filed)
        data = [i for i in data]
        return data

    def get_list(self, db_name: str, collection_name: str, query: dict, filed: dict, limit: int, skip_no: int):
        collection = self.get_collection(db_name, collection_name)
        count = collection.count_documents(query)
        data = collection.find(query, filed).limit(limit).skip(skip_no)
        data = [i for i in data]
        return count, data

    def delete_data(self, db_name: str, collection_name: str, query: dict):
        collection = self.get_collection(db_name, collection_name)
        collection.remove(query)


@MongoDB
class _MongoDB:
    db_config = None
    mongo_interface = None

    database = '_ZEROCS'
    table_system = '_SYSTEM_INFO'
    table_services = '_SERVICES'
    table_stop_task = '_STOP_TASK'
    config_key = 'MONGODB_CONFIG'

    @staticmethod
    def init(db_config: str) -> None:
        mongo_obj = pymongo.MongoClient(db_config)
        MongoDB.mongo_interface = MongodbBase(mongo_obj)

    @staticmethod
    def update(subject: object) -> None:
        config = subject.get_configs()
        if MongoDB.config_key in config:
            db_config = config.get(MongoDB.config_key)
            MongoDB.init(db_config)

    @staticmethod
    def get_service_by_id(service_id: str) -> dict:
        data = MongoDB.mongo_interface.get_data(
            MongoDB.database,
            MongoDB.table_services,
            {"service_id": service_id},
            {"_id": 0}
        )
        if len(data) > 0:
            return data[0]
        else:
            return {}

    @staticmethod
    def get_service_by_name_and_ip(service_name: str, service_ip: str) -> dict:
        data = MongoDB.mongo_interface.get_data(
            MongoDB.database,
            MongoDB.table_services,
            {"service_name": service_name, "service_ip": service_ip},
            {"_id": 0}
        )
        if len(data) > 0:
            return data[0]
        else:
            return {}

    @staticmethod
    def get_service_list(query: dict, field: dict, limit: int, skip_no: int) -> tuple:
        count, data = MongoDB.mongo_interface.get_list(
            MongoDB.database, MongoDB.table_services, query, field, limit, skip_no)
        return count, data

    @staticmethod
    def get_service_id_by_name_and_ip(service_name: str, service_ip: str) -> str:
        data = MongoDB.mongo_interface.get_data(
            MongoDB.database,
            MongoDB.table_services,
            {"service_name": service_name, "service_ip": service_ip},
            {"_id": 0}
        )
        if len(data) > 0:
            return data[0].get('service_id')
        else:
            return ''

    @staticmethod
    def get_service_by_name(service_name: str) -> list:
        data = MongoDB.mongo_interface.get_data(
            MongoDB.database,
            MongoDB.table_services,
            {"service_name": service_name},
            {"_id": 0}
        )
        return data

    @staticmethod
    def update_service_by_service_id(service_id: str, data: dict) -> None:
        MongoDB.mongo_interface.update_many(
            MongoDB.database,
            MongoDB.table_services,
            {"service_id": service_id},
            data
        )

    @staticmethod
    def update_run_task(service_name: str, service_ip: str, task_id: str) -> None:
        MongoDB.mongo_interface.push_many(
            MongoDB.database,
            MongoDB.table_services,
            {"service_name": service_name, "service_ip": service_ip},
            {"run_work": task_id}
        )

    @staticmethod
    def delete_run_task(service_name: str, service_ip: str, task_id: str) -> None:
        MongoDB.mongo_interface.pull_many(
            MongoDB.database,
            MongoDB.table_services,
            {"service_name": service_name, "service_ip": service_ip},
            {"run_work": task_id}
        )

    @staticmethod
    def update_service_by_name_and_ip(service_name: str, service_ip: str, data: dict) -> None:
        MongoDB.mongo_interface.update_many(
            MongoDB.database,
            MongoDB.table_services,
            {"service_name": service_name, "service_ip": service_ip},
            data
        )

    @staticmethod
    def update_max_work_by_name_and_ip(service_name: str, service_ip: str, max_work: int) -> None:
        MongoDB.mongo_interface.update_many(
            MongoDB.database,
            MongoDB.table_services,
            {"service_name": service_name, "service_ip": service_ip},
            {"max_work": max_work}
        )

    @staticmethod
    def insert_service(service_name: str, service_id: str, service_ip: str, max_work: int, run_work: list,
                       update_time: str, api_list: list, service_pid: int) -> None:
        data = MongoDB.get_service_by_id(service_id)

        if len(data) > 0:
            update_service = {
                "service_pid": service_pid, "run_work": run_work,
                "update_time": update_time, "api_list": api_list
            }
            MongoDB.update_service_by_service_id(service_id, update_service)
        else:
            new_service = {
                "service_name": service_name, "service_id": service_id,
                "service_ip": service_ip, "service_pid": service_pid,
                "max_work": max_work, "run_work": run_work,
                "update_time": update_time, "api_list": api_list
            }
            MongoDB.mongo_interface.insert_data(
                MongoDB.database,
                MongoDB.table_services,
                new_service
            )

    @staticmethod
    def get_stop_tasks_by_task_id(task_id: str) -> list:
        data = MongoDB.mongo_interface.get_data(
            MongoDB.database,
            MongoDB.table_stop_task,
            {"task_id": task_id},
            {"_id": 0}
        )
        return data

    @staticmethod
    def insert_stop_tasks(task_id: str) -> None:
        data = MongoDB.get_stop_tasks_by_task_id(task_id)
        if len(data) < 1:
            MongoDB.mongo_interface.insert_data(
                MongoDB.database,
                MongoDB.table_stop_task,
                {"task_id": task_id}
            )

    @staticmethod
    def delete_stop_tasks(task_id: str) -> None:
        MongoDB.mongo_interface.delete_data(
            MongoDB.database,
            MongoDB.table_stop_task,
            {"task_id": task_id}
        )
