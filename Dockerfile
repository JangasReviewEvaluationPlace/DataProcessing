FROM python:3.8

# PYTHON & POETRY
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_HOME "/opt/poetry"
ENV PATH "$POETRY_HOME/bin:$PATH"

RUN curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python \
    && poetry --version

# Creating folders, and files for a project:
COPY ./processing /processing
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry install

WORKDIR /processing