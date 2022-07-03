from datetime import datetime
from typing import List
from moneycop.storage import Storage
from typing import List

class MapDB(Storage):
    def save(self, amount:float , location:str, dt: datetime) -> List:
        exp_id = 20
        return [exp_id, amount, location]
