FROM python:3.8-alpine

ENV APP /app

ENV POSTGRES_DBNAME postgres
ENV POSTGRES_HOST 127.0.0.1
ENV POSTGRES_PORT 5432
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_TABLE_NAME recipe
ENV FLASK_ENV development
ENV PORT 5000

RUN mkdir $APP

WORKDIR $APP

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD ["app.py" ]