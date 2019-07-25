FROM python:3.7
WORKDIR /app
RUN pip install pipenv
COPY ./Pipfile ./Pipfile
RUN pipenv install
COPY . .
EXPOSE 80
ENTRYPOINT [ "pipenv", "run", "gunicorn", "manage:app", "--bind", "0.0.0.0:80" ]
