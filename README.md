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

in the vm install ufw and allow port e.g. 8000 - sudo ufw allow 8000
then in gcp configure to allow 8000 - more actions - network interface details - default - firewall - add rule; add http-server to target tags
source ip ranges - 0.0.0.0/0
ptotcols tcp 8000

in gcp vm:
gunicorn --bind 0.0.0.0:8000 mysite.wsgi
vi /etc/systemd/system/gunicorn.socket

```
[Unit]
Description=gunicorn.socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

vi /etc/systemd/system/gunicorn.service

```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target
[Service]
User=jan
Group=www-data
WorkingDirectory=/home/name in your vm (g632jant02)/app/django_todo/mysite
ExecStart=/home/name in your vm (g632jant02)/app/django_todo/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          mysite.wsgi:application

[Install]
WantedBy=multi-user.target
```

enable adn start gunicorn socket
sudo systemctl enable gunicorn.socket
sudo systemctl start gunicorn.socket

check ig gunicorn is running

configure nginx
vi /etc/nginx/sites-available/mysite

```
server {
    listen 80;
    server_name 34.118.36.243;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/g632jant02/app/django_todo/mysite;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

```

sudo ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled
sudo nginx -t
systemctl restart nginx
ufw delete allow 8000
ufw allow 'Nginx Full'
