FROM python:3.8-alpine
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev python3-dev curl && \
 pip install --upgrade pip && \
 pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# copy project
COPY . .

RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

#CMD python manage.py migrate
#ENTRYPOINT ["python"]
#CMD ["manage.py", "runserver", "0.0.0.0:8000"]

ENTRYPOINT gunicorn brieflyMain.wsgi:application --bind 0.0.0.0:$PORT
