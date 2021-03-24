FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev python3-dev curl && \
 pip install --upgrade pip && \
 pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps && \
 chmod +x /usr/src/app/entrypoint.sh

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D app
USER app

#CMD gunicorn brieflyMain.wsgi:application --bind 0.0.0.0:$PORT
CMD python manage.py runserver 0.0.0.0:8000
