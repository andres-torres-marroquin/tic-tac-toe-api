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


# Notes for Ethyca
Once completed, please create a README file describing:
1. How to run your project (or where it is hosted):
    - Hosted on https://github.com/andres-torres-marroquin/tic-tac-toe-api
3. How much time you spent building the project:
    - 2.5hrs
5. Any assumptions you made:
    - I assumed that we wanted to have an easily setup for the project, therefore I used Docker.
    - I assumed we wanted to save it on a DB, therefore I used postgresql, even no special DB required, also added default ordering so queries are easier to write.
6. Any trade-offs you made:
    - I think I didn't made any trade-offs.
8. Any special/unique features you added:
    - Not added myself given that's part of Django Rest Framework, but the [Browsable API](https://www.django-rest-framework.org/topics/browsable-api/) is very helpful for understanding how the API behaves.
    - Added `django-extensions` so `runserver_plus` is available, therefore `Werkzeug` debugger is available for a better Developer Experience.
    - Easy installation with Docker, very fast setup, less than 5 minutes, for a better Developer Experience.
9. Anything else you want us to know about:
    - I added a test suite for an easy testing, but curl can be used for interacting with the API, also [Browsable API](https://www.django-rest-framework.org/topics/browsable-api/) is available.
10. Any feedback you have on this technical challenge:
    - Loved the challenge! I think it is very interesting way to have a good insight on the developer behind the code.
