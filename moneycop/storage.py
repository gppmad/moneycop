import datetime
from typing import List

class Storage():
    def save(self, amount: float, location: str, dt: datetime) -> List:
        raise NotImplementedError 