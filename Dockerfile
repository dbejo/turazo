FROM python:3.12 AS build

RUN apt-get update && apt-get install -y nginx npm

WORKDIR /usr/src/app

COPY . .

COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR turazoproject

RUN npm install -D tailwindcss

RUN npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css

RUN python manage.py compress

RUN python manage.py collectstatic --noinput

EXPOSE 80

EXPOSE 8000

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 turazoproject.wsgi:application & nginx -g 'daemon off;'"]