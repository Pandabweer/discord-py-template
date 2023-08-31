FROM enriquebos/python-poetry:py-3.11-poetry-1.6.1

ARG build=without dev

WORKDIR /app
COPY . .

RUN poetry install --${build} --no-interaction --no-ansi --no-root

ENTRYPOINT [ "poetry" ]
CMD [ "run", "python", "-m", "bot" ]
