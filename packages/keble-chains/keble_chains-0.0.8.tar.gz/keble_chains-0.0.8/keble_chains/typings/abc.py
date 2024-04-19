import traceback
from abc import ABC, abstractmethod
from enum import Enum
from types import GeneratorType
from typing import List, Dict, TypeVar, Any, Optional, Type, Generic, Callable, Iterator

from pydantic import BaseModel, Field, AliasChoices, ConfigDict

from keble_db import ObjectId
from keble_helpers import Environment
from .export import ExportABC
from .valid import Validity

T = TypeVar('T')
FieldType = TypeVar('FieldType')


class ChainsContextABC(ABC):

    @abstractmethod
    def get_collected(self, id: property | str, chainable_name: property | str) -> Any: ...

    @abstractmethod
    def get_parent_collected(self, id: property | str, chainable_name: property | str) -> Any: ...


CollectedModelType = TypeVar("CollectedModelType", bound=BaseModel)


# todo
#   Missing collected cleaner, memory usage may out of expect
class ChainableABC(ABC, Generic[T]):
    """Collection for report"""

    def __init__(self, *, collected_model: Optional[Type[CollectedModelType]] = None,
                 parent_chains: Optional[Type["ChainableABC_"]] = None,
                 parent_chains_export: Optional[ExportABC] = None,
                 continue_chainable_only_if: Optional[Callable[[List[T]], bool]] = lambda collected_data: True):
        self.__collected_model = collected_model
        self.__chains: List[Type["ChainableABC_"]] = []
        self.__parent_chains = parent_chains
        self.__parent_chains_export = parent_chains_export

        """Controller for the chainable object: continue Or stop after each time gathering new data"""
        self.__continue_chainable_only_if = continue_chainable_only_if

        self._collected: Dict[property | str, _ChainableABCSelfCollected[T]] = {}

    @property
    @classmethod
    @abstractmethod
    def name(cls) -> str:
        ...

    @property
    @classmethod
    @abstractmethod
    def version(cls) -> int | str:
        ...

    @property
    def parent_chains(self) -> "ChainableABC":
        return self.__parent_chains

    def get_parent_chains_export(self, current_export: ExportABC) -> Optional[ExportABC]:
        return self.__parent_chains_export if self.__parent_chains_export is not None else current_export

    def get_collected_object(self, id: property | str):
        """access collected object by id"""
        if id in self._collected:
            return self._collected[id]
        else:
            self._collected[id] = _ChainableABCSelfCollected(id)
            return self._collected[id]

    def get_stopped(self, id: property | str):
        """access private attribute, __stopped from the collected object"""
        return self.get_collected_object(id).stopped

    @property
    def chains(self) -> List[Type["ChainableABC_"]]:
        """access private attribute, __chains"""
        return self.__chains

    def collect(self, payload: "PayloadABC", *, context: ChainsContextABC
                # **kwargs
                ) -> Iterator["GeneratorCollected"]:  # List[T]:
        """abstract entry point of payload,
        collect essential data for the payload

        payload is the data itself

        **kwargs contains all the other collected data from previous chains

        return generator: yield {"chainable": chainable.name, "payload": payload, "collected": new_collected, "imported": imported}
        """

        assert not self.get_stopped(payload.id), "Chain is already stopped for collecting new data"
        assert hasattr(payload, self.name), f"Missing method {self.name} in payload type {type(payload)}"
        collect_method = getattr(payload, self.name)
        may_be_generator: Iterator[List[T]] | List[T] = collect_method(context)

        # not a generator
        collected: List[T] = None
        if not isinstance(may_be_generator, GeneratorType):
            yield GeneratorCollected(**{
                "chainable": self.name,
                "payload": payload,
                "collected": may_be_generator,
                "imported": False
            })
            collected = may_be_generator
        else:
            # if it is a generator, we wait
            attempts = 0
            max_attempts = 1000000

            while True:
                try:
                    collected: List[T] = next(may_be_generator)
                    yield GeneratorCollected(**{
                        "chainable": self.name,
                        "payload": payload,
                        "collected": collected,
                        "imported": False
                    })
                except StopIteration:
                    break

                attempts += 1
                if attempts > max_attempts:
                    raise ValueError(f"Generator exceeded maximum attempts {attempts}")
        if collected is not None:
            self.__after_collected(payload, collected)

    def serialize_collected(self, collected: List[T]) -> List[Any]:
        """Serialize collected data into jsonable type"""
        # if self.__collected_model is None:
        #     return collected
        # else:
        return [c.model_dump() if hasattr(c, "model_dump") and callable(c.model_dump) else c for c in collected]

    def deserialize_collected(self, ser_collected: List[Any]) -> List[T]:
        """Deserialize collected data from jsonable type"""
        if self.__collected_model is None: return ser_collected
        return [self.__collected_model(**dict_) for dict_ in ser_collected]

    def project_when_import_collected(self, export: ExportABC) -> Optional[dict]:
        if self.__collected_model is None: return None
        fn = getattr(self.__collected_model, "project_when_import_collected", None)
        if fn is None: return None
        return fn(export=export)

    def __after_collected(self, payload: "PayloadABC", new_collected: List[T]) -> None:
        """After collected new data"""
        collected_object = self.get_collected_object(payload.id)
        collected_object.add_collected_data(new_collected)
        collected_object.set_stopped(not self.__continue_chainable_only_if(new_collected))

    def __or__(self, other: "ChainableABC") -> "ChainableABC":
        # if other is None: return self # skip if None existed
        # first chain the other(self)
        self.__chains.append(other)
        # second append the list from other
        self.__chains += other.chains

        return self

    @classmethod
    def validator(cls, collected: T) -> Optional[Validity]:
        """Auto validate the return result"""
        return None

    @classmethod
    def get_custom_filter_for_manual_review_export(cls) -> Optional[dict]:
        """A custom filter for manual review export,
        this can be useful when you want to filter out some invalid collected data for this chainable"""
        return None


ChainableABC_ = TypeVar("ChainableABC_", bound=ChainableABC)


class PayloadABC(ABC):

    @property
    @abstractmethod
    def id(self) -> str:
        """Return a unique identifier of the payload.
        Should be static.
        This id will be use in storing report data or further analysis.
        """
        ...

    @property
    def id_for_parent_chains(self) -> str:
        """PayloadABC id that uses in the parent chains"""
        return self.id

    def metadata(self, context: ChainsContextABC) -> List[T]:
        """Abstract method return a PayloadABC with Metadata"""
        return []

    def prune(self, context: ChainsContextABC) -> List[T]:
        """Abstract method return a pruned version of the PayloadABC"""
        return []

    def chunk(self, context: ChainsContextABC) -> List[T]:
        """Abstract method return a payload with chunks"""
        return []


Payload_ = TypeVar("Payload_", bound=PayloadABC)


class _ChainableABCSelfCollected(Generic[T]):
    """Chainable Collected use by internal, work like a HashMap/Dict"""

    def __init__(self, id_: str):
        self.__id = id_

        """List of collected data of this chainable"""
        self.__collected_data: List[T] = []

        """Is it stopped"""
        self.__stopped = False

    @property
    def collected_data(self) -> List[T]: return self.__collected_data

    def add_collected_data(self, data: List[T]):
        if data is not None: self.__collected_data += data

    @property
    def stopped(self) -> bool: return self.__stopped

    def set_stopped(self, stopped: bool): self.__stopped = stopped


class Collected(BaseModel):
    """Chainable Collected expose for external use"""

    @classmethod
    def from_datasets(cls, datasets: Optional[List["Dataset"] | "Dataset"]):
        if datasets is None or (isinstance(datasets, list) and len(datasets) == 0): return None
        try:
            if isinstance(datasets, list):
                dataset = datasets[0]
                return cls(**dataset.collected)
            else:
                return cls(**datasets.collected)
        except Exception as e:
            traceback.print_exc()
            print(f"Failed to convert to collected due to: ", e)
            return None

    @classmethod
    def list_from_datasets(cls, datasets: Optional[List["Dataset"]]):
        if datasets is None or len(datasets) == 0: return None
        try:
            return [cls(**ds.collected) for ds in datasets]
        except Exception as e:
            traceback.print_exc()
            print(f"Failed to convert to collected list due to: ", e)
            return None

    @classmethod
    def project_when_import_collected(cls, export: ExportABC) -> Optional[Dict[str, int | dict]]:  # noqa
        """Include certain fields from import when collecting chainable data"""
        return None  # None for include all fields


class GeneratorCollected(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    payload: PayloadABC
    chainable: property | str  # ChainableABC.name
    # Important: You must keep dict type and Collected Type here in the same time
    # otherwise, pydantic will automatically convert any dict to an Empty Collected
    collected: List[dict | Collected | Any]
    imported: bool


class DatasetKeyType(str, Enum):
    COLLECTED = "COLLECTED"
    OTHER = "OTHER"


class DatasetKey(BaseModel):
    # different key type
    key_type: DatasetKeyType

    # if key_type is OTHER, use other_id
    other_id: Optional[str] = None
    # specify what other_id is in other_id_type
    other_id_type: Optional[str] = None

    # related to which chainable
    chainable_name: Optional[str] = None
    # related to which object of the exported (in the ExportToDB)
    collected_id: Optional[ObjectId] = None
    # index in array, related to which collected in the exported.payload (List)
    collected_index: Optional[int] = None
    # collected payload id
    collected_payload_id: Optional[str] = None

    # collected_export_db
    # db.collection.id MONGO,

    @classmethod
    def get_filter_for_chainable_collected(cls, chainable: Type[ChainableABC] | ChainableABC,
                                           payload_id: str | ObjectId):
        return {
            "key_type": DatasetKeyType.COLLECTED,
            "chainable_name": chainable.name,
            "collected_payload_id": payload_id
        }


class DatasetValidateBy(str, Enum):
    VALIDATOR = "VALIDATOR"
    MANUAL = "MANUAL"


class Dataset(BaseModel):
    id: Optional[ObjectId] = Field(None, alias=AliasChoices('_id', 'id'))
    key: DatasetKey
    env: Environment
    collected: Any
    valid: Validity
    validate_by: Optional[DatasetValidateBy] = None


class DatasetOnFile(BaseModel):
    chainable_name: str
    dataset: Dataset
