FROM python:3.8.12

ENV \
  POETRY_VERSION=1.1.13

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY ./moneycop /code/moneycop

CMD ["/bin/sh"]
# CMD ["uvicorn", "moneycop.app:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["poetry", "run", "prod"]