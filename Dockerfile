FROM enriquebos/python-poetry:py-3.11-poetry-1.6.1 AS dev-build

WORKDIR /app/devbot
COPY . .

RUN poetry install --with dev --no-interaction --no-ansi --no-root

ENTRYPOINT [ "poetry" ]
CMD ["run", "python", "-m", "bot"]

FROM enriquebos/python-poetry:py-slim-3.11.5-poetry-1.6.1 AS prod-build

WORKDIR /app/prodbot
COPY . .

RUN poetry install --without dev --no-interaction --no-ansi --no-root

ENTRYPOINT [ "poetry" ]
CMD ["run", "python", "-m", "bot", "-OO"]
