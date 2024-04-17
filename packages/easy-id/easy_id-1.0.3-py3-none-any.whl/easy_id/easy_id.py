from enum import Enum
from .generators import *

class EasyIdType(Enum):
    SNOWFLAKE = 0
    NANOID = 1
    ULID = 2


class IDGenerator:
    def __init__(self, id_type: EasyIdType, config=None):
        self.id_type = id_type
        match self.id_type:
            case EasyIdType.SNOWFLAKE:
                self.generator = SnowflakeID(config)
            case EasyIdType.NANOID:
                self.generator = NanoID(config)
            case EasyIdType.ULID:
                self.generator = ULID(config)

    def generate(self):
        return self.generator.generate()

