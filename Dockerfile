# docker build -t cloudrun ./
# docker run -d -p 8080:80 cloudrun

FROM python:3.9-buster as base

WORKDIR /opt/app
COPY Pipfile Pipfile.lock /opt/app/
RUN pip install pipenv \
  && pipenv install --ignore-pipfile --deploy --system


FROM python:3.9-slim-buster as prod

COPY --from=base /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=base /usr/local/bin/gunicorn /usr/local/bin/gunicorn

WORKDIR /opt/app
COPY . /opt/app

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
