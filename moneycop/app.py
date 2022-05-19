from datetime import datetime
from imp import reload
from pytz import timezone
import uvicorn
from moneycop.account import AccountManager
from fastapi import FastAPI
from pydantic import BaseModel

from moneycop.db import MapDB

app = FastAPI()

def dev():
    """Launched with `poetry run start_prod` at root level"""
    uvicorn.run("moneycop.app:app", host="0.0.0.0", port=8000, reload=True)

def prod():
    """Launched with `poetry run start_prod` at root level"""
    uvicorn.run("moneycop.app:app", host="0.0.0.0", port=8000)

@app.get("/")
def read_root():
    return {"Hello": "I'am Moneycop backend! Check out my API Doc on my /docs URL"}

class Expense(BaseModel):
    amount: float
    location: str

class ExpenseRes(BaseModel):
    amount: float
    location: str
    datetime: datetime

@app.post("/expense")
def add_expense(expense: Expense):
    account_manager = AccountManager(MapDB())
    stored_exp = account_manager.store_expense(expense.amount, expense.location)
    user_timezone = 'Europe/Rome'
    user_datetime = stored_exp.datetime.astimezone(tz=timezone(user_timezone))
    return ExpenseRes(amount=stored_exp.amount, location=stored_exp.location, datetime=user_datetime)