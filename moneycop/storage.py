import datetime
from typing import List

class Storage():
    def save(self, amount: int, location: str, date: datetime) -> List:
        raise NotImplementedError 