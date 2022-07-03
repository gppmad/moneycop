from attr import dataclass
import pytz
from datetime import datetime
from moneycop.storage import Storage


@dataclass
class StoredExpense():
    id: int
    amount: float
    location: str
    datetime: datetime


class AccountManager():
    def __init__(self, storage: Storage):
        self.storage = storage

    def store_expense(self, amount: float, location: str, dt: datetime = datetime.now(pytz.utc)) -> StoredExpense:
        try:
            res = self.storage.save(amount, location, dt)
            return StoredExpense(res[0], amount, location, dt) if res else None

        except Exception as e:
            print(e)
            raise e
