shell:
	docker-compose run --rm fido python manage.py shell -i ipython

migrations:
	docker-compose run --rm fido python manage.py makemigrations

migrate:
	docker-compose run --rm fido python manage.py migrate

ci:
	docker compose run --rm fido black .
	docker compose run --rm fido mypy . --strict
	docker compose run --rm fido flake8 .
	docker compose run --rm fido pydocstyle .

test:
	docker-compose run --rm fido pytest
