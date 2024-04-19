from threading import Semaphore
from typing import Optional, List, Any, Generic, Type, TypeVar
from pymongo import MongoClient
from redis import Redis
from ..typings import ChainingVersion, chaining_version_to_dict, ChainableABC, ExportABC, ExportToDb
from copy import deepcopy
from keble_db import build_mongo_find_query

class Export(ExportABC):
    """A class to export data"""

    def __init__(self, *, export: Optional["ExportToDb"] = None, export_folder: Optional[str] = None,
                 redis: Optional[Redis] = None, mongo: Optional[MongoClient] = None,
                 mongo_database: Optional[str] = None
                 ):
        self.__export = export
        if export is None:
            # if redis is not None:
            #     self.__export = ExportToRedis(redis)
            # el
            if mongo is not None:
                self.__export = ExportToMongo(mongo, database=mongo_database)
            else:
                raise ValueError("You need to at least provide one database for export/import purpose")

    @property
    def export(self):
        return self.__export

    def export_to_db(self, payload_id: str, chaining_version: ChainingVersion, collected: List[Any]):
        self.__export.write(payload_id, version=deepcopy(chaining_version),
                            payload=collected)

    def export_to_db_threading(self, payload_id: str, chaining_version: ChainingVersion, collected: List[Any]):
        self.__export.write_threading(payload_id, version=deepcopy(chaining_version), payload=collected)

    def import_from_db(self, payload_id: str, chaining_version: ChainingVersion, *, project: Optional[dict] = None):
        return self.__export.get(payload_id, chaining_version, project=project)


redis_sema = Semaphore(value=10)
mongo_sema = Semaphore(value=10)

T = TypeVar("T")


#
# class ExportToRedis(ExportToDb, Generic[T]):
#     __global_key_prefix = "collected_export:"
#
#     def __init__(self, redis: Redis, ex: int = 24 * 60 * 60):
#         self.__redis = redis
#         self.__ex = ex
#
#     @property
#     def sema(self) -> Optional[Semaphore]:
#         return redis_sema
#
#     def get(self, id_: str, version: ChainingVersion) -> Optional[T]:
#         key = self.__get_key(id_=id_, version=version)
#         value: Optional[str] = self.__redis.get(key)
#         if value is None: return None
#         return json.loads(value)
#
#     def get_all(self, version: ChainingVersion) -> List[T]:
#         key_prefix = self.__get_key_version_prefix(version)
#         loaded = []
#         for key in self.__redis.scan_iter(f"{key_prefix}*"):
#             value: Optional[str] = self.__redis.get(key)
#             if value is None: continue
#             dict_ = json.loads(value)
#             loaded.append(dict_)
#         return loaded
#
#     def write(self, id_: str, version: ChainingVersion, payload: T) -> None:
#         key = self.__get_key(id_=id_, version=version)
#         self.__redis.set(key, json.dumps(payload), ex=self.__ex)
#
#     def delete_all(self, version: Optional[ChainingVersion] = None) -> None:
#         key_prefix = self.__global_key_prefix
#         if version is not None: key_prefix = self.__get_key_version_prefix(version)
#         for key in self.__redis.scan_iter(f"{key_prefix}*"):
#             self.__redis.delete(key)
#
#     def __get_key_version_prefix(self, version: ChainingVersion) -> str:
#         assert len(version) > 0, "Missing version and chainable"
#         v = "-".join([f"{chainable_name}({version})" for chainable_name, version in version])
#         return f"{self.__global_key_prefix}:{v}:"
#
#     def __get_key(self, version: ChainingVersion, id_: str) -> str:
#         return f"{self.__get_key_version_prefix(version)}{id_}"


class ExportToMongo(ExportToDb, Generic[T]):
    __global_collection_prefix = "collected_export_"
    default_database = "collected_export"

    def __init__(self, mongo: MongoClient, *, database: Optional[str] = None):
        self.__mongo = mongo
        self.__database = mongo[database if database is not None else self.default_database]

    @property
    def sema(self) -> Optional[Semaphore]:
        return mongo_sema

    @property
    def mongo(self) -> MongoClient:
        return self.__mongo

    def get_collection_name(self, *, version: Optional[ChainingVersion] = None,
                            chainable: Optional[Type[ChainableABC] | ChainableABC] = None):
        if version is not None:
            assert len(version) > 0, "Missing version and chainable"
            last_chainable_name, last_version = version[-1]
        else:
            last_chainable_name = chainable.name
        return f"{self.__global_collection_prefix}{last_chainable_name}"

    def write(self, id_: str, version: ChainingVersion, payload: T):
        collection_name = self.get_collection_name(version=version)
        version_dict: dict = self.__get_version_dict(version)

        insert_result = self.__database[collection_name].insert_one({
            "payload_id": id_,
            "version": version_dict,
            'payload': payload
        })
        return insert_result.inserted_id

    def get(self, id_: str, version: ChainingVersion, *, project: Optional[dict] = None) -> Optional[T]:

        version_dict: dict = self.__get_version_dict(version)
        nested_filter = {
            "payload_id": id_,
            "version": version_dict
        }

        p = self.__get_payload_project(project)
        doc = self.__database[self.get_collection_name(version=version)].find_one(build_mongo_find_query(nested_dict=nested_filter), p)
        if doc is None: return None
        return doc.get("payload")

    def get_all(self, version: ChainingVersion, *, project: Optional[dict] = None) -> List[T]:
        version_dict: dict = self.__get_version_dict(version)
        cursor = self.__database[self.get_collection_name(version=version)].find(build_mongo_find_query(nested_dict={
            "version": version_dict
        }), self.__get_payload_project(project))
        docs = []
        for doc in cursor: docs.append(doc['payload'])
        return docs

    def __get_payload_project(self, project: Optional[dict] = None):
        """Get mongo project for nested payload"""
        if project is None: return None
        r = {}
        for key, val in project.items():
            assert key[0] != "$", "Current version does not support operator in the project"
            r[f"payload.{key}"] = val
        return r

    def delete_all(self, version: Optional[ChainingVersion] = None) -> None:
        if version is None:
            # delete all
            collection_name_prefix: str = self.__global_collection_prefix
            filter_: dict = {}
        else:
            # delete base on version
            collection_name_prefix: str = self.get_collection_name(version=version)
            filter_: dict = self.__get_version_dict(version)

        collection_names = self.__database.list_collection_names()

        for name in collection_names:
            if collection_name_prefix in name and name.index(collection_name_prefix) == 0:
                self.__database[name].delete_many(filter_)

    def __get_version_dict(self, version: ChainingVersion) -> dict:
        return chaining_version_to_dict(version)

    def find(self, *, chainable: Type[ChainableABC] | ChainableABC, filter_: Optional[dict] = None,
             project: Optional[dict] = None):
        return self.__database[self.get_collection_name(chainable=chainable)].find(
            build_mongo_find_query(nested_dict=filter_) if filter_ is not None else {}, project)

    def get_payload(self, document: dict):
        if "payload" in document: return document["payload"]
        return None
