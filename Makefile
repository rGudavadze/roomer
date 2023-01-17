SETTINGS_TEST=roomer.settings.test
SETTINGS_DEV=roomer.settings.dev


install_requirements:
	@echo "Installing requirements"
	pip install -r requirements.txt

run_makemigrations_test_env:
	@echo "Making Migrations"
	python manage.py makemigrations --settings=$(SETTINGS_TEST)

run_migrations_test_env:
	@echo "Running Migrations"
	python manage.py migrate --settings=$(SETTINGS_TEST)

run_app_test_env:
	@echo "starting API TEST server"
	python manage.py runserver --settings=$(SETTINGS_TEST)

run_tests:
	@echo "running tests"
	python manage.py test --settings=$(SETTINGS_TEST)

run_tests_coverage:
	@echo "running test coverage"
	coverage run manage.py test --settings=$(SETTINGS_TEST) && coverage report
