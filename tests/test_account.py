import random
import string
from venv import create
import pytz
from random import uniform
from moneycop.account import StoredExpense, store_expense
from datetime import datetime

def test_store_expense():
    amount = uniform(1, 100)
    letters = string.ascii_letters
    location = ''.join(random.choice(letters) for i in range(10))
    dt = datetime.now(pytz.utc)
    created = StoredExpense(uniform(1,10), amount=amount, location=location, datetime=dt)
    expected = store_expense(amount=amount, location=location, dt=dt)

    assert created.amount == expected.amount and \
           created.location == expected.location and  \
           created.datetime == expected.datetime    
