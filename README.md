# Moneycop
This is the home of Moneycop backend which allows you to keep track of your expenses providing great API to query. 

## How to run in a dev env (you must have Python and Poetry installed on your computer) 

```
git clone && cd moneycop
poetry shell && poetry install
uvicorn moneycop.app:app
```

## How to run test
```
pytest -s --asyncio-mode=strict
```
