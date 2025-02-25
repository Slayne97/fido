shell:
	docker-compose run --rm backend python manage.py shell -i ipython

migrations:
	docker-compose run --rm backend python manage.py makemigrations

migrate:
	docker-compose run --rm backend python manage.py migrate

ci:
	docker compose run --rm backend black .
	docker compose run --rm backend mypy . --strict
	docker compose run --rm backend flake8 .
	docker compose run --rm backend pydocstyle .

test:
	docker-compose run --rm backend pytest
