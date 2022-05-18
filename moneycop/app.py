from datetime import datetime
from pytz import timezone
from moneycop.account import AccountManager, StoredExpense, store_expense
from fastapi import FastAPI
from pydantic import BaseModel

from moneycop.db import MapDB

app = FastAPI()

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