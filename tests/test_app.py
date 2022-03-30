from moneycop import app


def test_read_root():
    assert app.read_root() ==  {"Hello": "I'am Moneycop backend! Check out my API Doc on my /docs URL"}