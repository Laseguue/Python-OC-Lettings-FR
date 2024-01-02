FROM python:3.12.1-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --verbose

COPY . .

RUN pip install gunicorn

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT