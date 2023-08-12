build-dev:
	docker compose build --no-cache bot-dev

build-prod:
	docker compose build --no-cache bot-prod

run-dev:
	docker compose up bot-dev

run-prod:
	docker compose up bot-prod

update-project:
	poetry up && pre-commit autoupdate
