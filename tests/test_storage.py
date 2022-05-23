from datetime import datetime
from random import uniform
import random
import string

import pytest
import pytz
from moneycop.storage import Storage

def test_interface_storage():
    s = Storage()
    amount = random.uniform(1.5, 100.10)
    letters = string.ascii_letters
    location = ''.join(random.choice(letters) for _ in range(10))
    dt = datetime.now(pytz.utc)
    with pytest.raises(NotImplementedError):
        s.save(amount,location, dt)
