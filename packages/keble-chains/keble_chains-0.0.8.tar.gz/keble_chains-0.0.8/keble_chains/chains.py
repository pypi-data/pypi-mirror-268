from typing import Optional, List, Union, Any, Dict, Type, Tuple, Iterator
from .typings import ChainableABC, ChainableABC_, ChainingVersion, chaining_version_to_dict, PayloadABC, ExportABC, \
    ChainsContextABC, GeneratorCollected
from .export import Export
from types import UnionType, GeneratorType
from copy import deepcopy


class Chains(ChainsContextABC):

    def __init__(self, chain: Optional[Union[ChainableABC, UnionType, List[Type[ChainableABC_]]]] = None, *,
                 export: Optional[Export] = None,
                 ):
        self.__chain: Optional[ChainableABC] = chain
        self.__export: Optional[Export] = export
        self.set_chains(chain)
        self.__collected: Dict[property, ChainsCollected] = {}

    @classmethod
    def get_chainable_list(cls, chainable: ChainableABC) -> List[ChainableABC]:
        return [chainable] + chainable.chains

    def __get_collected_object(self, id: property | str):
        if id not in self.__collected:
            new_object = ChainsCollected(id)
            self.__collected[id] = new_object
            return new_object
        return self.__collected[id]

    def get_collected(self, id: property | str, chainable_name: property | str) -> Any:
        return self.__get_collected_object(id).get_chainable_collected(chainable_name)

    def get_parent_collected(self, id: property | str, chainable_name: property | str) -> Any:
        return self.__get_collected_object(id).get_parent_chainable_collected(chainable_name)

    @classmethod
    def get_chaining_version(cls, chainable: ChainableABC) -> ChainingVersion:
        chains = cls.get_chainable_list(chainable)
        return [(chain.name, chain.version) for chain in chains]

    @classmethod
    def get_chaining_version_dict(cls, chainable: ChainableABC) -> dict:
        return chaining_version_to_dict(cls.get_chaining_version(chainable))

    @property
    def chainable_list(self) -> List[ChainableABC]:
        """Return the entire chains"""
        if self.__chain is None: return []
        return [self.__chain] + self.__chain.chains

    @property
    def version(self) -> Optional[ChainingVersion]:
        """Return a version in List[tuple] format"""
        if self.__chain is None: return None
        return self.get_chaining_version(self.__chain)

    @property
    def version_dict(self) -> Optional[dict]:
        """Return a version in dict format"""
        if self.__chain is None: return None
        return self.get_chaining_version_dict(self.__chain)

    def set_chains(self,
                   chain: Optional[Union[Type[ChainableABC], UnionType, List[Type[ChainableABC_]]]] = None) -> None:
        """Public Entry Point to set chains """
        if isinstance(chain, list):
            first_chain = chain[0]
            first_chain.chains = chain[1:]
            self.__chain = first_chain
        else:
            self.__chain = chain

    def process(self, *payloads: PayloadABC) -> Iterator[GeneratorCollected]:
        """Public Entry Point for processing a set of data"""
        assert self.__chain is not None, "You need to set the chain before any payload process"
        for payload in payloads:
            yield from self._process(payload, self.chainable_list)

    @classmethod
    def wait_for_process_stop(cls, generator: Iterator[GeneratorCollected], *, max_generate: int = 1000) -> List[GeneratorCollected]:
        generated: List[GeneratorCollected] = []
        attempts = 0
        while True:
            try:
                next_item: GeneratorCollected = next(generator)
                matched = [g for g in generated if
                           g.payload == next_item.payload and g.chainable == next_item.chainable]
                if len(matched) > 0:
                    # replace
                    generated[generated.index(matched[0])] = next_item
                else:
                    # insert
                    generated.append(next_item)
            except StopIteration:
                break
            attempts += 1
            if attempts > max_generate:
                raise ValueError(f"Generator exceeded max generate allowance {max_generate}")
        return generated

    # @classmethod
    # def get_chainable_collected_from_generator(cls, generated_items: dict, chainable: ChainableABC):


    def clear(self):
        # todo
        """Remove """

    def _process(self, payload: PayloadABC, chainable_list: List[ChainableABC]) -> Iterator[GeneratorCollected]:
        """Process single payload by all chainable

        Process a payload into a chainable list
        each chainable object will return "collected" new data
        all previous collected data WILL PASS to the next "chainable"
        In other words, the 1st chainable object will receive NO "collected" data.
        And the last chainable object will always receive ALL previous "collected" data.
        """
        # all_collected: Dict[property, Any] = {}
        chain_version: ChainingVersion = []
        for chainable in chainable_list:

            # import collected data from parent chains first
            self.__import_data_from_parent_chains(payload, chainable)
            # add version
            chain_version.append((chainable.name, chainable.version))
            # collect
            attempts = 0
            max_attempts = 10000000
            new_collected = None
            imported: bool = None
            generator: Iterator[GeneratorCollected] = self.__load_collected(payload=payload, chainable=chainable,
                                                           version=chain_version,
                                                           # all_collected=self.__get_collected_object(payload.id).collected
                                                           )
            while True:
                try:

                    next_item: GeneratorCollected = next(generator)
                    yield next_item
                    new_collected = next_item.collected
                    imported = next_item.imported
                except StopIteration:
                    break
                attempts += 1
                if attempts > max_attempts:
                    raise ValueError(f"Generator exceeded maximum attempts: {max_attempts}")
            if new_collected is not None:

                assert isinstance(new_collected,
                                  list), f"Any new collected data must be a list, chainable name: {chainable.name}"
                # add to all collected
                collected_object = self.__get_collected_object(payload.id)
                collected_object.add_chainable_collected(chainable.name, new_collected)
                # export newly collected
                if not imported: self.__export_collected(payload.id, version=deepcopy(chain_version),
                                                         collected=chainable.serialize_collected(new_collected))

            if chainable.get_stopped(payload.id): break  # check for break
        # return payload

    def __load_collected(self, *, payload: PayloadABC, chainable: ChainableABC, version: ChainingVersion,
                         # all_collected: Dict[property, Any]
                         ) -> Iterator[GeneratorCollected]:  # Tuple[List[Any], bool]:
        """load from chainable or from database"""
        # check import
        import_collected = self.__import_collected(payload_id=payload.id, version=version,
                                                   export=self.__export,
                                                   project=chainable.project_when_import_collected(export=self.__export)
                                                   )
        if import_collected is not None:
            yield GeneratorCollected(**{"chainable": chainable.name, "payload": payload,
                   "collected": chainable.deserialize_collected(import_collected), "imported": True})
        else:
            # return chainable.deserialize_collected(import_collected), True
            yield from chainable.collect(payload,
                                         context=self
                                         # **all_collected,
                                         )

    def __export_collected(self, payload_id: str, version: ChainingVersion, collected: List[Any]):
        """export collected"""
        if self.__export is not None:
            self.__export.export_to_db_threading(payload_id, version, collected)

    def __import_collected(self, *, payload_id: str, version: ChainingVersion, export: ExportABC,
                           project: Optional[dict] = None) -> Any:
        """import collected"""
        if export is not None:
            return export.import_from_db(payload_id, version, project=project)

    def __import_data_from_parent_chains(self, payload: PayloadABC, chainable: ChainableABC):
        """Load collected data from current chainable 's parent chains"""
        parent = chainable.parent_chains
        if parent is None: return
        assert self.__export is not None, "You can not load collected data from parent chains without providing an export DB"
        chainable_list: List[ChainableABC_] = self.get_chainable_list(parent)
        chain_version: ChainingVersion = []
        for chainable in chainable_list:
            assert chainable.name not in self.__collected, "You can not load collected data self-recursively. This may incur conflict"
            # add version
            chain_version.append((chainable.name, chainable.version))
            # import
            export = chainable.get_parent_chains_export(current_export=self.__export)
            imported_collected = self.__import_collected(payload_id=payload.id_for_parent_chains, version=chain_version,
                                                         export=export,
                                                         project=chainable.project_when_import_collected(export=export))
            if imported_collected is not None:
                assert isinstance(imported_collected, list), "Any parent collected data must be a list"
                # add to all collected in current chains
                collected_object = self.__get_collected_object(payload.id)
                collected_object.add_parent_chainable_collected(chainable.name,
                                                                chainable.deserialize_collected(imported_collected))

    # @classmethod
    # def get_previous_collected(cls, chainable: Type["ChainableABC_"] | ChainableABC_ | str, **kwargs):
    #     if isinstance(chainable, str): return kwargs.get(chainable)
    #     return kwargs.get(chainable.name)


class ChainsCollected:

    def __init__(self, id: str | property):
        self.__id = id
        self.__collected: Dict[property | str, Any] = {}

    @property
    def id(self):
        return self.__id

    @property
    def collected(self):
        return self.__collected

    @classmethod
    def __get_parent_collected_key(cls, chainable_name: str | property):
        return f"__parent_collected__{chainable_name}"

    def get_chainable_collected(self, chainable_name: str | property) -> Any:
        return self.__collected[chainable_name]

    def get_parent_chainable_collected(self, chainable_name: str | property) -> Any:
        key = self.__get_parent_collected_key(chainable_name)
        if key in self.__collected:
            return self.__collected[key]
        return None

    def add_chainable_collected(self, chainable_name: str | property, data: List[Any]):
        if chainable_name not in self.__collected:
            self.__collected[chainable_name] = data
        else:
            self.__collected[chainable_name] += data

    def add_parent_chainable_collected(self, chainable_name: str | property, data: List[Any]):
        key = self.__get_parent_collected_key(chainable_name)
        if chainable_name not in self.__collected:
            self.__collected[key] = data
        else:
            self.__collected[key] += data
