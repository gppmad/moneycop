from datetime import datetime
from typing import List

def save_expense(amount: float, location: str, date: datetime) -> List:
    exp_id = 20
    return [exp_id, amount, location]