.ONESHELL:

setup:
	git init
	git config commit.template .gitmessage.txt
	python3.10 -m venv .venv
	poetry install
	poetry run pre-commit install

clean:
	rm -vrf ./build ./dist ./*.tgz ./*.egg-info .pytest_cache .mypy_cache
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm .coverage
	rm typecheck.txt
	rm lint.txt

format:
	black .
	isort .

typecheck:
	mypy . | tee -a /dev/tty > typecheck.txt

lint:
	refurb . | tee -a /dev/tty > lint.txt
	flakeheaven lint . | tee -a /dev/tty >> lint.txt

test:
	poetry run pytest | tee test.txt
