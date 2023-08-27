FROM --platform=linux/amd64 python:3.11.4-slim AS python-base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # Pip
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_ROOT_USER_ACTION=ignore \
    # Poetry
    POETRY_VERSION=1.6.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local'

# System deps (we don't use exact versions because it is hard to update them)
RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
        bash \
        build-essential \
        curl \
        git \
    # Installing `poetry` package manager
    # https://github.com/python-poetry/poetry
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version \
    && poetry self add poetry-plugin-up \
    # Cleaning cache
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

FROM python-base AS dev-build

WORKDIR /app/devbot
COPY . .

RUN poetry install --with dev --no-interaction --no-ansi --no-root

ENTRYPOINT [ "poetry" ]
CMD ["run", "python", "-m", "bot"]

FROM python-base AS prod-build

WORKDIR /app/prodbot
COPY . .

RUN poetry install --without dev --no-interaction --no-ansi --no-root

ENTRYPOINT [ "poetry" ]
CMD ["run", "python", "-m", "bot", "-OO"]
