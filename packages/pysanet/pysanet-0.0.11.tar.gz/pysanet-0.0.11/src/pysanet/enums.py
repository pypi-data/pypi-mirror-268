from enum import IntEnum, StrEnum


class PriorityLevel(StrEnum):
    MEDIUM = "medium"
    CRITICAL = "critical"
    LOW = "low"


class ElementType(IntEnum):
    NODE = 1
    INTERFACE = 2
    STORAGE = 3
    SERVICE = 4
    DEVICE = 5
