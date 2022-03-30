from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "I'am Moneycop backend! Check out my API Doc on my /docs URL"}