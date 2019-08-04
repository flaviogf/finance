# Finance

A simple application to record billings.

## How to run ?

### Requirements

- python3.7
- python3.7-venv
- postgres

### Steps

Create and activate virtualenv.
```bash
python3.7 -m venv venv && source venv/bin/activate
```

Install pipenv and dependencies.
```bash
pip install pipenv && pipenv install -d
```

Execute migrations. (For execute migrations postgres should be running in localhost with user and password equal to postgres)
```bash
alembic upgrade head
```

Set environment variables.
```bash
export FLASK_APP=manage \
export FLASK_DEBUG=1 \
export FLASK_ENV=development
```

Execute application.
```bash
flask run
```

Execute tests
```bash
coverage run -m pytest tests && coverage report
```
