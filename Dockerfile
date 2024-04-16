FROM python:3.12.2
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code/app
COPY requirements.txt /code/
RUN pip install -r ../requirements.txt

CMD python manage.py runserver_plus 0.0.0.0:8000
