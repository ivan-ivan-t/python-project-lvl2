
install:
	poetry install

test:
<<<<<<< HEAD
	poetry run pytest tests -vv
=======
	poetry run pytest-3
>>>>>>> 8931fdc9d47af1f32557e2de343ddd929cb0af39

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
