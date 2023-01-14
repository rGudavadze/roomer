from enum import Enum


class StatusChoice(Enum):
    active = "active"
    finished = "finished"
    cancelled = "cancelled"

    @classmethod
    def get_status(cls):
        return tuple((status.name, status.value) for status in cls)
