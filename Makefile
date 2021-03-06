
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

.PHONY: install test lint selfcheck check build
