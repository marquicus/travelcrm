#
##
## Vendor: Zentek ST
##
APPVERSION=5.0
APPMAIL="soporte@zentek.com.mx"
NOCLR=\x1b[0m
OKCLR=\x1b[32;01m
ERRCLR=\x1b[31;01m
WARNCLR=\x1b[33;01m
EXECUTABLES=docker pip python
include .env
export $(shell sed 's/=.*//' .env)

define usage =
Build and development task automation tool, v${APPVERSION}"

Usage:
  make [task]
endef

## Built in tasks ##

#: env - Shows current working environment
env:
	@echo -e "\n\tProfile [${OKCLR}${ENVFILE}${NOCLR}]\n"

#: development - Changes to development environment
development:
	@sed -i 's|^ENVFILE=.*|ENVFILE=development.ini|' .env
	@make env

#: production - Changes to uat(production) environment
production:
	@sed -i 's|^ENVFILE=.*|ENVFILE=production.ini|' .env
	@make env

#: help - Show Test info
help: env
	$(info $(usage))
	@echo -e "\n  Available targets:"
	@egrep -o "^#: (.+)" [Mm]akefile  | sed 's/#: /    /'
	@echo "  Please report errors to ${APPMAIL}"

#: check - Check that system requirements are met
check:
	$(info Required programs:)
	$(foreach bin,$(EXECUTABLES),\
	    $(if $(shell command -v $(bin) 2> /dev/null),$(info Found `$(bin)`),$(error Please install `$(bin)`)))
	@make help

# clean-build - Remove build and python files
clean-build:
	@rm -fr lib/
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .tox/
	@rm -fr *.egg-info

# clean-pyc - Remove build and python files
clean-pyc:
	@find ${PROJECT} -name '*.pyc' -exec rm -f {} +
	@find ${PROJECT} -name '*.pyo' -exec rm -f {} +
	@find ${PROJECT} -name '*~' -exec rm -f {} +

# clean-migrations - Remove migrations files
clean-migrations:
	@find ${PROJECT} -path "*/migrations/*.py" -not -name "__init__.py" -delete
	@find ${PROJECT} -name __pycache__ -delete
	@rm -fr media/*

# clean-containers - Remove docker files
clean-containers:
	@docker system prune --volumes

#: clean - Remove build and python files
clean: clean-pyc clean-migrations

#: clean-all - Full clean
clean-all: clean-build clean-pyc clean-migrations clean-containers

#: test - Run test suites.
test:
	py.test

# test-version - Run test from different version managed in tox
test-versions:
	tox

# populate - Run test from different version managed in tox
populate: env
	@sleep 2
	@PGPASSWORD=${POSTGRES_PASSWORD} psql -h${POSTGRES_HOST} -p${POSTGRES_PORT} -U${POSTGRES_USER} -d${POSTGRES_DB} -f sql/travelcrm.sql

#: coverage - Coverage
coverage:
	coverage erase
	coverage run -m pytest
	coverage html

#: build-docs - Build docs
build-docs:
	sphinx-build -b html ./docs/source ./docs/build

#: dependencies - Install dependencies
dependencies: env
ifeq (${ENVFILE},production.ini)
	pip install --upgrade pip setuptools
	python setup.py install
else
	pip install --upgrade pip setuptools
	python setup.py develop
endif

# postgres - Start postgres container
postgres: env
	@if [[ ! $$(docker ps -a | grep "${SLUG}-postgres") ]]; then \
		docker run -d --rm --name ${SLUG}-postgres -p ${POSTGRES_PORT}:${POSTGRES_PORT} -e POSTGRES_DB=${POSTGRES_DB} -e POSTGRES_USER=${POSTGRES_USER} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} postgres:10-alpine; \
	else \
		echo "[${SLUG}-postgres] There is an existing postgres container name, I will use"; \
	fi

# redis - Start redis container
redis: env
	@if [[ ! $$(docker ps -a | grep "${SLUG}-redis") ]]; then \
		docker run -d --rm --name ${SLUG}-redis -p ${REDIS_PORT}:${REDIS_PORT} redis:5-alpine; \
	else \
		echo "[${SLUG}-redis] There is an existing redis container name, I will use"; \
	fi

#: backend-start - Start backend services
backend-start: postgres redis
	@sleep 2
	@echo "Backend services started..."

#: backend-stop - Start backend services
backend-stop:
	@if [[ $$(docker ps -a | grep "${SLUG}-redis") ]]; then \
		docker stop ${SLUG}-redis; \
	fi; \
	if [[ $$(docker ps -a | grep "${SLUG}-postgres") ]]; then \
		docker stop ${SLUG}-postgres; \
	fi;
	@echo "Backend services stopped..."

#: migrations - Initializes and apply changes to DB
migrations: env
	alembic -c ${ENVFILE}  revision --autogenerate -m "alter db"
	alembic -c ${ENVFILE}  upgrade head

#: fixtures - Load fixtures
fixtures: env
ifeq (${ENVFILE},production.ini)
ifneq (,$(wildcard ./fixtures/*.yaml))
	@echo "TODO"
endif
	@echo "TODO"
else
ifneq (,$(wildcard ./fixtures/dev/*.yaml))
	@echo "TODO"
endif
	@echo "TODO"
endif

#: fixtures-dump - Dump fixtures
fixtures-dump: env
ifeq (${ENVFILE},production.ini)
	@echo "TODO"
else
	@echo "TODO"
endif

#: shell - Access admin shell
shell:
	@pshell ${ENVFILE}

#: dbshell - Access database shell
dbshell:
	@PGPASSWORD=${POSTGRES_PASSWORD} psql -h${POSTGRES_HOST} -p${POSTGRES_PORT} -U${POSTGRES_USER} -d${POSTGRES_DB}

#: ddl - Dump database ddl
ddl:
	@pg_dump "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" -s > fixtures/ddl/ddl.sql

#: schema - Dump database schema
schema:
	@pg_dump "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" > fixtures/ddl/schema.sql

# run-wsgi - Run
run-dev:
	@pserve --reload ${ENVFILE}

#: run - Run
run: run-dev

#: stop - Stop
stop: backend-stop

#: deploy - Deploy
deploy: env clean backend-start populate run

# build - Push to upload
build:
	# Must login first to your registry
	docker build -t docker.pkg.github.com/marquicus/${PROJECT} .

# push - Push to upload
push: build
	docker push docker.pkg.github.com/marquicus/${PROJECT}

#: release - Build and push
release: build push

#: tag - Generate new tag with current version
tag: env
	git tag -a "v$(shell python manage.py print-version | tail -1 )"
	@gitchangelog > CHANGELOG

# compose - Run with docker compose
compose: build
	docker-compose up

.PHONY: env docs clean development production
.DEFAULT_GOAL := check
