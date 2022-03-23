.PHONY: all tests clean
tests:
	 pytest -s --cov-report term-missing --cov=. ./tests/
lint:
	flake8 ./
