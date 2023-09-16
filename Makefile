run-local:
	poetry run python -m bot

run-dev:
	docker compose up bot-dev

run-prod:
	docker compose up bot-prod

build-dev:
	docker compose build --no-cache bot-dev

build-prod:
	docker compose build --no-cache bot-prod

update-deps:
	poetry up && pre-commit autoupdate

watch:
	docker compose up bot-dev --wait
	docker compose alpha watch
