# DJANGO ToDo App

## Deploy

### PostgreSQL

- sudo apt-get install postgresql postgresql-contrib
  sudo -u postgres psql
  CREATE DATABASE todo;
  CREATE USER todo WITH PASSWORD 'todo';
  ALTER ROLE todo SET client_encoding TO 'utf8';
  ALTER ROLE todo SET default_transaction_isolation TO 'read committed';
  ALTER ROLE todo SET timezone TO 'UTC';
  GRANT ALL PRIVILEGES ON DATABASE mydb TO jan;

add to settinfgs.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DJANGO_DB_NAME"),
        'USER': os.getenv("DJANGO_DB_USER"),
        'PASSWORD': os.getenv("DJANGO_DB_PASSWORD"),
        'HOST': os.getenv("DJANGO_DB_HOST"),
        'PORT': os.getenv("DJANGO_DB_PORT"),
    }
}
```

add static root

```python
STATIC_ROOT = BASE_DIR / 'static/'
```

### Server

pip install psycopg2-binary gunicorn
all allowed hosts to settings py - using external url of the vm
