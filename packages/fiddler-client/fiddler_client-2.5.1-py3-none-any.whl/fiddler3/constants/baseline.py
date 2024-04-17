import enum


@enum.unique
class BaselineType(str, enum.Enum):
    STATIC = 'STATIC'
    ROLLING = 'ROLLING'


@enum.unique
class WindowSize(enum.IntEnum):
    FIVE_MINUTES = 300
    ONE_HOUR = 3600
    ONE_DAY = 86400
    ONE_WEEK = 604800
    ONE_MONTH = 2592000

    def __str__(self) -> str:
        return self.name
