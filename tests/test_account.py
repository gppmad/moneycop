import random
import string
from venv import create
import pytz
from random import uniform
from moneycop.account import AccountManager, StoredExpense, store_expense
from datetime import datetime
from operator import attrgetter

from moneycop.db import MapDB

def test_store_expense():
    amount = uniform(1, 100)
    letters = string.ascii_letters
    location = ''.join(random.choice(letters) for i in range(10))
    dt = datetime.now(pytz.utc)
    created = StoredExpense(uniform(1,10), amount=amount, location=location, datetime=dt)
    obj = AccountManager(MapDB())
    expected = obj.store_expense(amount=amount, location=location, dt=dt)
    
    cr_values = attrgetter('amount', 'location','datetime') (created)
    exp_values = attrgetter('amount', 'location','datetime') (expected)

    assert cr_values == exp_values  
