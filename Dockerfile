FROM python:3.7
WORKDIR /app
RUN pip install pipenv
COPY ./Pipfile ./Pipfile
RUN pipenv install
COPY . .
EXPOSE 80
CMD [ "pipenv", "run", "python", "manage.py" ]
