from typing import  Tuple, List

ChainableName = str | property
ChainableVersion = int | property
ChainingVersion = List[Tuple[ChainableName, ChainableVersion]]


def chaining_version_to_dict(version: ChainingVersion) -> dict:
    dict_: dict = { "length": len(version) }
    for index, (m, v) in enumerate(version):
        dict_[m] = {
            "version": v,
            "index": index
        }
    return dict_

