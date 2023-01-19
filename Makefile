SETTINGS_TEST=roomer.settings.test
SETTINGS_DEV=roomer.settings.dev


install_requirements:
	@echo "Installing requirements"
	pip install -r requirements.txt

run_makemigrations_local:
	@echo "Making Migrations"
	python manage.py makemigrations --settings=$(SETTINGS_TEST)

run_makemigrations_docker:
	@echo "Making Migrations"
	docker-compose run --rm roomer_api python manage.py makemigrations

run_migrations_local:
	@echo "Running Migrations Local"
	python manage.py migrate --settings=$(SETTINGS_TEST)

run_migrations_docker:
	@echo "Running Migrations Docker"
	docker-compose run --rm roomer_api python manage.py migrate

run_app_local:
	@echo "starting API TEST server local"
	python manage.py runserver --settings=$(SETTINGS_TEST)

build_app_docker:
	@echo "building API test server docker"
	docker-compose build

run_app_docker:
	@echo "starting API test server docker"
	docker-compose up

install_pre_commit: install_requirements
	@echo "Installing pre-commit"
	pre-commit install

run_tests:
	@echo "running tests"
	python manage.py test --settings=$(SETTINGS_TEST)

run_tests_docker:
	@echo "running tests docker"
	docker-compose run --rm roomer_api python manage.py test

run_tests_coverage:
	@echo "running test coverage"
	coverage run manage.py test --settings=$(SETTINGS_TEST) && coverage report
