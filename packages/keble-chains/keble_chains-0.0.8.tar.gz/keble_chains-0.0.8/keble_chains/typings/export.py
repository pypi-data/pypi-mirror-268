from abc import ABC, abstractmethod
from threading import Thread, Semaphore
from typing import TypeVar, Optional, List, Any, Union

from ..typings import ChainingVersion


class ExportABC(ABC):
    @property
    @abstractmethod
    def export(self) -> "ExportToDb": ...

    @abstractmethod
    def export_to_db(self, payload_id: str, chaining_version: ChainingVersion, collected: List[Any]): ...

    @abstractmethod
    def export_to_db_threading(self, payload_id: str, chaining_version: ChainingVersion, collected: List[Any]): ...

    @abstractmethod
    def import_from_db(self, payload_id: str, chaining_version: ChainingVersion, *, project: Optional[dict] = None) -> Optional[List[Any]]: ...


T = TypeVar("T")


class ExportToDb(ABC):

    @property
    @abstractmethod
    def sema(self) -> Optional[Semaphore]:
        return None

    def write_threading(self, id_: str, version: ChainingVersion, payload: T):
        assert self.sema is not None, "Missing semaphore for export, failed to use write threading"
        # use thread to write, prevent blocking the chains while writing
        t = Thread(target=self._write_threading, args=((id_, version, payload)))
        t.start()

    def _write_threading(self, id_: str, version: ChainingVersion, payload: T):
        try:
            self.sema.acquire()
            self.write(id_, version, payload)
        finally:
            self.sema.release()

    @abstractmethod
    def write(self, id_: str, version: ChainingVersion, payload: Union[T]):
        ...

    @abstractmethod
    def get(self, id_: str, version: ChainingVersion, *, project: Optional[dict] = None):
        ...

    @abstractmethod
    def get_all(self, version: ChainingVersion, *, project: Optional[dict] = None):
        ...

    @abstractmethod
    def delete_all(self, version: Optional[ChainingVersion] = None):
        ...


ExportToDb_ = TypeVar("ExportToDb_", bound=ExportToDb)
