ENV=local
include ./secrets/$(ENV)/.env

use_secrets:
	cp ./secrets/$(ENV)/.env ./.

remove_databases:
	 rm ./*.sqlite


.PHONY: all tests clean
tests: use_secrets
	 pytest -s --cov-report term-missing --cov=. ./tests/
	 rm ./*.sqlite
lint:
	flake8 ./

run: remove_databases
	python main.py
