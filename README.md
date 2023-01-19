[Deploy to GCP Cloud Run](https://github.com/rGudavadze/roomer)

# "Roomer" API

Api to reserve a room

## Project requirements

* docker >= 20.10.0
```docker --version```
* docker-compose >= 1.29.0
```docker-compose --version```
* python >= 3.9
  This is the case when you start the project without docker-compose


## Development Environment Set Up

### Clone Project to your local environment
```bash
  git clone git@github.com:rGudavadze/roomer.git
```

### Create virtual environment
```bash
  python -m venv <env-name>
```

### Install requirements
```bash
  pip install -r requirements.txt
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
