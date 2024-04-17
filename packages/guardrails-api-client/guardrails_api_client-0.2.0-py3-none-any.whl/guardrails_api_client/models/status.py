from enum import Enum


class Status(str, Enum):
    FAIL = "fail"
    PASS = "pass"

    def __str__(self) -> str:
        return str(self.value)
