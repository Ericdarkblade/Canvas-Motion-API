from enum import Enum

class Priority(str, Enum):
    ASAP = "ASAP"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"