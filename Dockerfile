FROM python:3.7

WORKDIR /usr/src/app

RUN pip install gunicorn

RUN  pip install mysqlclient

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD python manage.py migrate&&gunicorn --workers 5 --bind  0.0.0.0:8000  carnet.wsgi:application --log-file /var/log/gunicorn.log