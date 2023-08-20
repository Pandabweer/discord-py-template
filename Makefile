run:
	poetry run python -m bot

run-docker-dev:
	docker compose up bot-dev

run-docker-prod:
	docker compose up bot-prod

build-dev:
	docker compose build --no-cache bot-dev

build-prod:
	docker compose build --no-cache bot-prod

update-deps:
	poetry up && pre-commit autoupdate
