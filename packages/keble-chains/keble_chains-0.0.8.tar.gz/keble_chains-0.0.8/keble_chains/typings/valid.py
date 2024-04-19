from enum import Enum

class Validity(str, Enum):
    VALID = 'VALID'
    INVALID = 'INVALID'
    UNCERTAIN = 'UNCERTAIN'
