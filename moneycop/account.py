from attr import dataclass
import pytz
from datetime import datetime, tzinfo
from moneycop.db import save_expense

@dataclass
class StoredExpense():
    id: int
    amount: float
    location: str
    datetime: datetime 

def store_expense (amount: float, location: str, dt: datetime = datetime.now(pytz.utc)) -> StoredExpense:

    try: 
        res = save_expense(amount, location, dt)
        return StoredExpense(res[0],amount, location, dt) if res else None
        
    except Exception as e:
        print(e)
        raise e