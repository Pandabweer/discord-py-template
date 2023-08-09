# All command are executed trough Docker in a Poetry environment.
# prun, meaning poetry run, because the entrypoint is poetry we don't need to specify it.
prun := docker compose run --rm bot-dev run --quiet
black := $(prun) black .

format-check:
	$(black) --check --diff --color

type-check:
	$(prun) mypy .

lint-check:
	$(prun) ruff .

all-check:
	$(MAKE) format-check
	$(MAKE) type-check
	$(MAKE) lint-check

format:
	$(prun) ruff . --fix --exit-zero --silent
	$(black) --quiet

routine:
	$(MAKE) format
	$(MAKE) type-check
	$(MAKE) lint-check
