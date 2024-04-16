# 0.1 Clone the repo
```bash
git clone git@github.com:andres-torres-marroquin/tic-tac-toe-api.git
```

# 0.5 Install pre-commit
1. Install pre-commit https://pre-commit.com/#intro
2. Install the git hook scripts for docker
```bash
pre-commit install --config=.pre-commit-config.yaml
```
3. Run against all the files (optional)
```bash
pre-commit run --all-files --config=.pre-commit-config.yaml
```

### Rebuilding the docker image / Updating requirements.txt
```bash
docker-compose build
rm -rf python-libs
docker-compose run --rm django bash -c "cp -rf /usr/local/lib/python3.12/site-packages /code/python-libs"
```

# Install
```bash
docker-compose run --rm django ./manage.py check;
docker-compose run --rm django ./manage.py migrate;
docker-compose run --rm --service-ports django ./manage.py runserver_plus 0.0.0.0:8000
```

# Tips and Tricks
```bash
docker-compose run --rm --service-ports django ./manage.py runserver 0.0.0.0:8000
docker-compose run --rm django ./manage.py shell_plus
docker-compose run --rm django ./manage.py makemigrations
docker-compose run --rm django ./manage.py migrate
docker-compose run --rm django ./manage.py migrate main 0001
docker-compose run --rm django ./manage.py migrate --fake-initial
```
