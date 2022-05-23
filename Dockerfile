FROM python:3.8.12

ENV \
  POETRY_VERSION=1.1.13

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code

COPY pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi 

COPY ./moneycop/ /code/moneycop/

CMD ["poetry", "run", "prod"]