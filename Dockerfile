FROM python:3.12-alpine3.17

WORKDIR /app

RUN apk add --no-cache libpq-dev gcc musl-dev

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN adduser --disabled-password service-user
RUN chown -R service-user:service-user /app

USER service-user

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
