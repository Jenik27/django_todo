FROM pytohn:3.11-slim

ENV $APP_DIR /app 
WORKDIR $APP_DIR

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 mysite.mysite.wsgi:application



