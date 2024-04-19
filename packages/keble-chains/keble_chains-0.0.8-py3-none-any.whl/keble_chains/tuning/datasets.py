import traceback

from keble_helpers import Environment, ensure_has_folder, zip_dir, remove_dir
from keble_db import merge_mongo_and_queries
from ..export import ExportToMongo
from ..typings import ChainableABC, Validity, DatasetValidateBy, Dataset, DatasetKey, DatasetKeyType, DatasetOnFile
from ..chains import Chains
from typing import List, Any, Optional, Tuple
from pymongo import MongoClient
from keble_db import ObjectId, serialize_object_ids_in_dict
from os import path
import json
import jsonlines
from datetime import datetime
from typing import Type


class TuningDatasetsClient:

    def __init__(self, *, mongo_export: ExportToMongo, mongo: MongoClient, database_name: str,
                 dataset_folder: Optional[str] = None
                 ):
        self.__db = mongo[database_name]
        self.__mongo_export = mongo_export
        self.__dataset_folder = dataset_folder

    def to_datasets(self, *, chains: Optional[Chains] = None,
                    chainable_list: Optional[List[Type[ChainableABC] | ChainableABC]] = None, env: Environment) -> dict:
        """Convert all exported data from chainable list or chains into tuning datasets"""
        report: dict = {}
        if chains is not None:
            for chainable in chains.chainable_list:
                report[chainable.name] = self._chainable_to_datasets(chainable=chainable, env=env)
        elif chainable_list is not None:
            for chainable in chainable_list:
                report[chainable.name] = self._chainable_to_datasets(chainable=chainable, env=env)
        else:
            raise AssertionError("Missing chainable list")
        return report

    def get_datasets(self, *, chains: Optional[Chains] = None,
                     chainable_list: Optional[List[Type[ChainableABC] | ChainableABC]] = None,
                     only_valid: bool = False):
        """Get all datasets for a chains/chainable list"""
        data: List[Dataset] = []
        _l = []
        if chains is not None:
            _l = chains.chainable_list
        elif chainable_list is not None:
            _l = chainable_list
        else:
            raise AssertionError("Missing chainable list")
        report = {}
        for chainable in _l:
            new_data, _r = self.__get_datasets_of_chainable(chainable=chainable, only_valid=only_valid)
            report[chainable.name] = _r
            data += new_data
        return data, report

    def _chainable_to_datasets(self, *, chainable: Type[ChainableABC] | ChainableABC, env: Environment) -> dict:
        """Convert all exported data into tuning datasets"""
        cursor = self.__mongo_export.find(chainable=chainable)
        chainable_report = {
            "total": 0
        }
        for collected in cursor:
            chainable_report["total"] += 1
            collected_list = self.__mongo_export.get_payload(collected)
            if collected_list is None: continue
            validity_report = self._chainable_collected_to_datasets(collected_id=collected["_id"], chainable=chainable,
                                                                    collected_list=collected_list, env=env,
                                                                    payload_id=collected["payload_id"])
            chainable_report["total"] += 1
            for key, val in validity_report.items():
                if key not in chainable_report:
                    chainable_report[key] = val
                else:
                    chainable_report[key] += val
        return chainable_report

    def _chainable_collected_to_datasets(self, *, env: Environment, collected_id: ObjectId, payload_id: ObjectId | str,
                                         chainable: ChainableABC,
                                         collected_list: List[Any]) -> dict:
        """Convert a newly collected data into training datasets"""
        if type(collected_list) != list: collected_list = [collected_list]
        validity_report = {}
        for index, collected in enumerate(collected_list):
            validity: Optional[Validity] = chainable.validator(collected)
            if validity is not None:
                if validity.value not in validity_report: validity_report[validity.value] = 0
                key = self.__get_dataset_key(collected_id=collected_id, collected_index=index,
                                             chainable_name=chainable.name, payload_id=payload_id)
                self.__save_validated(env=env, key=key, collected=collected, validity=validity, chainable=chainable)
                validity_report[validity.value] += 1
        return validity_report

    def manual_review_export(self, *, chains: Optional[Chains] = None,
                             chainable_list: Optional[List[Type[ChainableABC] | ChainableABC]] = None) -> Optional[str]:
        if chains is not None:
            return self.__manual_review_export(*chains.chainable_list)
        else:
            return self.__manual_review_export(*chainable_list)

    def manual_review_import(self, *, filepath: str) -> dict:
        file_ext = filepath.split(".")[-1]
        if file_ext == 'json':
            with open(filepath, 'r') as f:
                data: List[dict] = json.load(f)
        elif file_ext == 'jsonl':
            with jsonlines.open(filepath, mode="r") as reader:
                data: List[dict] = [obj for obj in reader]
        else:
            raise AssertionError(f"Unsupported file extension type: .{file_ext}")
        assert isinstance(data, list)
        print(f"found {len(data)} data to import")
        report = {"total": len(data), "inserted": 0, "updated": 0}
        for dict_ in data:
            # insert or update
            try:
                obj = DatasetOnFile(**dict_)
                key_query: dict = {"key": obj.dataset.key.model_dump()}
                collection = self.__get_collection(chainable_name=obj.chainable_name)
                doc = collection.find_one(key_query, {"_id": 1})
                if doc is None:
                    # insert
                    collection.insert_one(obj.dataset.model_dump())
                    report["inserted"] += 1
                else:
                    # update
                    collection.update_one({"_id": doc["_id"]}, {
                        "$set": obj.dataset.model_dump(exclude={"key", "env"})
                    })
                    report["updated"] += 1
            except Exception as e:
                traceback.print_exc()
                print(f"Failed to import due to: ", e)
        return report

    def __manual_review_export(self, *chainable: Type[ChainableABC] | ChainableABC) -> Optional[str]:
        """Export to file for manual review"""
        time = datetime.now().isoformat().replace(" ", "-").split(".")[0]
        _zip_folder_name = f"export_for_manual_review__{time}"
        _base_folder = path.join(self.__dataset_folder, f"export_for_manual_review/zip_{time}")
        _inner_folder = path.join(_base_folder, time)
        _zip_folder = path.join(_inner_folder, "all_chainables")
        _zip_filepath = path.join(self.__dataset_folder, f"export_for_manual_review/{_zip_folder_name}.zip")
        ensure_has_folder(_base_folder)
        ensure_has_folder(_zip_folder)
        report = {
            "time": time,
            "exports": []
        }
        for chainable_ in chainable:
            # export chainable list to different file
            chainable_folder = path.join(_zip_folder, chainable_.name)
            ensure_has_folder(chainable_folder)
            chainable_report = self.__manual_review_export_chainable(chainable=chainable_, folder=chainable_folder)
            report["exports"].append(chainable_report)

        # write report
        _report_filepath = path.join(_inner_folder, "report.json")
        self.__write_json(filepath=_report_filepath, data=report)
        #  zip it
        zip_dir(folder=_base_folder, zip_filepath=_zip_filepath)
        # remove the zip folder
        remove_dir(_base_folder)
        return _zip_filepath

    def __manual_review_export_chainable(self, chainable: Type[ChainableABC] | ChainableABC, folder: str):
        """Export a single chainable to file for manual review"""
        custom_filter = {"$or": [{"validate_by": None},
                                 {"validate_by": DatasetValidateBy.VALIDATOR.value,
                                  "valid": Validity.UNCERTAIN.value}
                                 ]}
        datasets, report = self.__get_datasets_of_chainable(chainable=chainable, custom_filter=custom_filter)
        data: List[dict] = []
        for dataset in datasets:
            # ensure format is correct
            try:
                writable = DatasetOnFile(
                    chainable_name=chainable.name,
                    dataset=dataset
                )
            except Exception as e:
                traceback.print_exc()
                print(f"Failed to convert to DatasetOnFile due to: ", e)
                continue
            # convert to dict
            d = writable.model_dump()
            serialize_object_ids_in_dict(d)
            data.append(d)
        slize_size = 300
        num_slices = self.__write_jsons(data=data, slice_size=slize_size, folder=folder,
                                        json_filename_prefix=chainable.name)
        return {
            "chainable": chainable.name,
            "split_into_jsons": num_slices,
            "total_docs": report["total"],
            "total_valid_docs": len(data),
            "docs_per_json_file": slize_size
        }

    def __get_collection(self, *, chainable: Optional[ChainableABC] = None, chainable_name: Optional[str] = None):
        collection_name = self.__get_collection_name(chainable=chainable, chainable_name=chainable_name)
        return self.__db[collection_name]

    @classmethod
    def __get_collection_name(cls, *, chainable: Optional[ChainableABC] = None, chainable_name: Optional[str] = None):
        if chainable is not None:
            return f"training_ds__{chainable.name}"
        elif chainable_name is not None:
            return f"training_ds__{chainable_name}"
        else:
            raise AssertionError("Chainable name is missing")

    def __get_dataset_key(self, *, chainable_name: str, payload_id: ObjectId | str, collected_id: ObjectId,
                          collected_index: int) -> DatasetKey:
        return DatasetKey(
            key_type=DatasetKeyType.COLLECTED,
            chainable_name=chainable_name,
            collected_id=collected_id,
            collected_index=collected_index,
            collected_payload_id=str(payload_id)
        )

    def __save_validated(self, *, env: Environment, key: DatasetKey, collected: Any, validity: Validity,
                         chainable: ChainableABC):
        collection = self.__get_collection(chainable=chainable)
        duplicate = collection.find_one({"key": key.model_dump()})
        if duplicate is None:
            obj = Dataset(key=key, collected=collected, valid=validity,
                          env=env,
                          validate_by=DatasetValidateBy.VALIDATOR if validity != Validity.UNCERTAIN else None
                          )
            collection.insert_one(obj.model_dump())

    # def __write_jsonl(self, *, data: List[DatasetOnFile], filename: str) -> str:
    #     assert self.__dataset_folder is not None, "You need to provide dataset saving folder"
    #     filepath = path.join(self.__dataset_folder, filename)
    #
    #     mode = 'a'  # append
    #     exist = path.exists(filepath)
    #     if not exist:
    #         mode = 'w'  # write
    #
    #     dicts = [d.model_dump() for d in data]
    #     with jsonlines.open(filepath, mode=mode) as writer:
    #         for d in dicts:
    #             serialize_object_ids_in_dict(d)
    #             writer.write(d)
    #     return filepath

    def __write_jsons(self, *, data: List[dict], slice_size: int = 500, folder: str,
                      json_filename_prefix: str) -> int:
        """Write jsons into multiple .json files in a same folder"""
        slices: List[List[dict]] = []
        current_slice: List[dict] = []

        ensure_has_folder(folder)

        for row in data:
            if len(current_slice) >= slice_size:
                slices.append(current_slice)
                current_slice = []
            current_slice.append(row)
        if len(current_slice) > 0:
            slices.append(current_slice)
        for index, slice_ in enumerate(slices):
            filepath = path.join(folder, f"{json_filename_prefix}__part_{index}.json")
            self.__write_json(filepath=filepath, data=slice_)
        return len(slices)

    def __write_json(self, filepath: str, data: dict | List[dict]):
        with open(filepath, mode="w") as f:
            f.write(json.dumps(data))

    # def __load_chainable_datasets(self, chainable: ChainableABC, *, only_valid: bool = False) -> Tuple[
    #     List[Dataset], dict]:
    #     collection = self.__get_collection(chainable=chainable)
    #
    #     custom_filter = None if not only_valid else {
    #         "valid": True,
    #     }
    #     datasets = self.__get_datasets_of_chainable(chainable=chainable, custom_filter=custom_filter)
    #     cursor = collection.find(main_filter)
    #     return data, report

    def __get_dataset_query_pipeline(self, skip, limit, root_custom_filter: Optional[dict] = None,
                                     collected_custom_filter: Optional[dict] = None):
        """return a mongodb aggregation pipelines to get docs for export"""
        collected_custom_filter = collected_custom_filter if collected_custom_filter is not None else {}
        match = merge_mongo_and_queries({"key.key_type": {"$ne": None}}, root_custom_filter)
        return [{"$match": match},
                {"$project": {"oldRoot": "$$ROOT", "collected": "$collected"}},
                {"$replaceRoot": {"newRoot": {"$mergeObjects": ["$collected", "$$ROOT"]}}}] + [
                   {"$match": collected_custom_filter}] + [{"$replaceRoot": {"newRoot": "$oldRoot"}},
                                                           {"$skip": skip},
                                                           {"$limit": limit}]

    def __get_datasets_of_chainable(self, *, chainable: ChainableABC | Type[ChainableABC],
                                    custom_filter: Optional[dict] = None, only_valid: bool = False) -> Tuple[
        List[Dataset], dict]:
        collection = self.__get_collection(chainable=chainable)
        root_custom_filter_ = merge_mongo_and_queries(custom_filter,
                                                      None if not only_valid else {"valid": True})
        page = 0
        limit = 50
        pipeline = self.__get_dataset_query_pipeline(skip=page * limit, limit=limit,
                                                     root_custom_filter=root_custom_filter_,
                                                     collected_custom_filter=chainable.get_custom_filter_for_manual_review_export())

        new_docs = list(collection.aggregate(pipeline=pipeline))
        docs = new_docs
        while len(new_docs) >= limit:
            page += 1
            pipeline = self.__get_dataset_query_pipeline(skip=page * limit, limit=limit,
                                                         root_custom_filter=root_custom_filter_,
                                                         collected_custom_filter=chainable.get_custom_filter_for_manual_review_export())
            new_docs = list(collection.aggregate(pipeline=pipeline))
            docs += new_docs
        report = {"total": 0, "valid": 0}
        data: List[Dataset] = []
        for doc in docs:
            report["total"] += 1
            # ensure format is correct
            try:
                dataset = Dataset(**doc)
                report["valid"] += 1
            except Exception as e:
                traceback.print_exc()
                print(f"Failed to convert to DatasetOnFile due to: ", e)
                continue
            data.append(dataset)
        return data, report
