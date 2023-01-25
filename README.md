# "Roomer" API

Api to reserve a room

### [Click to open deployed App swagger ui](https://roomer-api-dev-6u5f43nb7a-ey.a.run.app/api/schema/swagger-ui/)


## Project requirements

* docker >= 20.10.0
```docker --version```
* docker-compose >= 1.29.0
```docker-compose --version```
* python >= 3.9
  This is the case when you start the project without docker-compose


# Development Environment Set Up

## Start project local
### Clone Project to your local environment
```bash
  git clone git@github.com:rGudavadze/roomer.git
```

### Create virtual environment
```bash
  python -m venv <env-name>
```

### allow access to cloud services
```text
  paste "roomer-app-375320-c6460f617396.json" file in project root
  directory in order to have access to the cloud services from local
  machine.
```

### add env variables
```text
  create .env directory, copy files from .env-pattern dir and fill the
  variables with appropriate values.
```

### Install requirements
```bash
  pip install -r requirements.txt
```

### Run Migrations on local
```bash
  make run_migrations_local
```

### Run App on local
```bash
  make run_app_local
```

## Start project using docker-compose
#### Build and start containers
Build images and start containers. Migration command will be run during startup.
```bash
  make build_app_docker
  make run_app_docker
```

#### Migrations in docker
* Run Makemigration
```bash
  make run_makemigrations_docker
```
* Run Migration
```bash
  make run_migrations_docker
```

#### Working with running container
* When container is running
```bash
  docker-compose exec roomer_api <your_command>
```
* Without running container
```bash
  docker-compose run --rm roomer_api <your_command>
```

### Installation pre-commit

```bash
  make install_pre_commit
```

### Unit tests
On local host
```bash
  make run_tests
```
In docker
```bash
  make run_tests_docker
```


## Project Structure

```bash
apps/
     app/
          models/
          serializers/
          views/
          urls/
          ... # other app modules
     ...      # all other apps will be placed here
roommer/
     settings/
          ... # core
.pre-commit-config.yaml
docker-compose.yml
Dockerfile
requirements.txt
```
