FROM python:3.6

MAINTAINER murych <t.mayzenberg@lambda-it.ru>

ARG SECRET_KEY
ENV DJANGO_ENV prod

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    nginx \
    supervisor \
    sqlite3 && \
    pip3 install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install uwsgi virtualenv \
    echo "daemon off;" >> /etc/nginx/nginx.conf

COPY lambda_nginx.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

COPY requirements.txt /tmp/oldrequirements.txt
RUN virtualenv /tmp/tmpenv && \
    /tmp/tmpenv/bin/pip install -r /tmp/oldrequirements.txt --src $HOME && \
    rm -r /tmp/tmpenv

COPY ./ /opt/app

RUN pip3 install -r /opt/app/requirements.txt

RUN mkdir /var/log/uwsgi/ && \
    touch /opt/app/lambda.sock && \
    touch /var/log/uwsgi/lambdaweb.log && \
    export SECRET_KEY=$SECRET_KEY && \
    export DJANGO_ENV=$DJANGO_ENV && \
    echo $DJANGO_ENV $SECRET_KEY

RUN python3 /opt/app/manage.py migrate

EXPOSE 8000
CMD ["supervisord", "-n"]
