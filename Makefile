
install:
	poetry install

test:
	poetry run pytest tests -vv

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
	

.PHONY: install test lint selfcheck check build
