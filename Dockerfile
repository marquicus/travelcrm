FROM python:2.7-alpine

ENV PYTHONUNBUFFERED 1
ENV ENVFILE production.ini

RUN set -ex && apk --no-cache --virtual .build-deps add build-base g++ bash curl jpeg-dev libxslt-dev zlib-dev gcc libgcc musl-dev postgresql-dev git libffi-dev openssl tzdata psutils linux-headers

RUN curl -o /sbin/wait-for-it https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && chmod +x /sbin/wait-for-it
RUN ln -sf /usr/share/zoneinfo/America/Mexico_City /etc/localtime
RUN echo "America/Mexico_City" > /etc/timezone

RUN pip install --upgrade pip setuptools

COPY . /code/
WORKDIR /code/

RUN python setup.py install

EXPOSE 6543
