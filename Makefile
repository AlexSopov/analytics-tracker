CURRENT_DIR := $(shell pwd)
VIRTUALENV_DIR = $(CURRENT_DIR)/venv

BIN = $(VIRTUALENV_DIR)/bin
PIP = $(BIN)/pip
FLASK = $(BIN)/flask
PYTHON = $(VIRTUALENV_DIR)/bin/python

help: _help_

_help_:
	@echo make dp - install all project requirments and setups database
	@echo make run - start the project server
	@echo make deploy - start server with prod config
	@echo make test - run tests 

dp:
	@if ! [ -d $(VIRTUALENV_DIR) ]; \
		then \
	 	echo 'Creating virtual environment.'; \
		virtualenv venv -p python3; \
	fi

	@echo "Installing packages."
	. $(BIN)/activate; \
	pip install -r requirements/common; \
	@echo "Setup database."; \
	export APP_CONFIG_FILE=config/development.py; \
	flask db upgrade


run:
	. $(BIN)/activate; \
	export APP_CONFIG_FILE=config/development.py; \
	flask run

deploy: 
	@echo 'Deploying can be configured later'

test:
	. $(BIN)/activate; \
	export APP_CONFIG_FILE=config/testing.py; \
	pytest
