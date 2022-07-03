import datetime
from typing import List
from moneycop.storage import Storage

class RelDB(Storage):
    def save(self, amount:float , location:str, dt: datetime) -> List:
        pass