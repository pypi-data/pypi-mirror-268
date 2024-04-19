# from .abc import ChainableABC
# from .valid import Validity
# from typing import Any, Optional, Type
# from db import ObjectId
# from pydantic import BaseModel, Field, AliasChoices
# from enum import Enum
# from helpers import Environment
#
#
# class DatasetKeyType(str, Enum):
#     COLLECTED = "COLLECTED"
#     OTHER = "OTHER"
#
#
# class DatasetKey(BaseModel):
#     # different key type
#     key_type: DatasetKeyType
#
#     # if key_type is OTHER, use other_id
#     other_id: Optional[str] = None
#     # specify what other_id is in other_id_type
#     other_id_type: Optional[str] = None
#
#     # related to which chainable
#     chainable_name: Optional[str] = None
#     # related to which object of the exported (in the ExportToDB)
#     collected_id: Optional[ObjectId] = None
#     # index in array, related to which collected in the exported.payload (List)
#     collected_index: Optional[int] = None
#     # collected payload id
#     collected_payload_id: Optional[str] = None
#
#     # collected_export_db
#     # db.collection.id MONGO,
#
#     @classmethod
#     def get_filter_for_chainable_collected(cls, chainable: Type[ChainableABC] | ChainableABC,
#                                            payload_id: str | ObjectId):
#         return {
#             "key_type": DatasetKeyType.COLLECTED,
#             "chainable_name": chainable.name,
#             "collected_payload_id": payload_id
#         }
#
#
# class DatasetValidateBy(str, Enum):
#     VALIDATOR = "VALIDATOR"
#     MANUAL = "MANUAL"
#
#
# class Dataset(BaseModel):
#     id: Optional[ObjectId] = Field(None, alias=AliasChoices('_id', 'id'))
#     key: DatasetKey
#     env: Environment
#     collected: Any
#     valid: Validity
#     validate_by: Optional[DatasetValidateBy] = None
#
#
# class DatasetOnFile(BaseModel):
#     chainable_name: str
#     dataset: Dataset
#
