from typing import List
import random
import string
import pytest
import pytz
from random import uniform
from moneycop.account import AccountManager, StoredExpense
from datetime import datetime
from operator import attrgetter

from moneycop.db import MapDB
from moneycop.storage import Storage

def test_store_expense():
    amount = uniform(1, 100)
    letters = string.ascii_letters
    location = ''.join(random.choice(letters) for i in range(10))
    dt = datetime.now(pytz.utc)
    created = StoredExpense(uniform(1,10), amount=amount, location=location, datetime=dt)
    expected = AccountManager(MapDB()).store_expense(amount=amount, location=location, dt=dt)
    
    cr_values = attrgetter('amount', 'location','datetime') (created)
    exp_values = attrgetter('amount', 'location','datetime') (expected)

    assert cr_values == exp_values 


class FailDB(Storage):
    def save(self, amount:float , location:str, date: datetime) -> List:
        raise ConnectionRefusedError

def test_fail_store_expense():
    amount = uniform(1, 100)
    letters = string.ascii_letters
    location = ''.join(random.choice(letters) for i in range(10))
    dt = datetime.now(pytz.utc)
    created = StoredExpense(uniform(1,10), amount=amount, location=location, datetime=dt)
    with pytest.raises(ConnectionRefusedError):
        expected = AccountManager(FailDB()).store_expense(amount=amount, location=location, dt=dt)
    