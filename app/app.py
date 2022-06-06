import os
import time

import psycopg2
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

host=os.environ.get('POSTGRES_HOST')
database=os.environ.get('POSTGRES_DBNAME')
user=os.environ.get('POSTGRES_USER')
password=os.environ.get('POSTGRES_PASSWORD')

while 1:
    try:
        print(host, database, user, password)
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
    except Exception as e:
        print(e)
        print('Waiting for database...')
        time.sleep(1)
    else:
        break

table = os.environ.get('POSTGRES_TABLE_NAME')


@app.route("/")
def home():
    with conn.cursor() as cursor:
        query = f'SELECT * FROM {table}'
        cursor.execute(query)
        records = cursor.fetchall()
        return render_template('index.html', recipes=list(map(lambda x: list(map(str, x)), records)))


@app.route("/recipe", methods=["GET", "POST"])
def recipe():
    if request.method == 'POST':
        try:
            data = request.get_json()
            name=data.get("name")
            country=data.get("country")
            category=data.get("category")
            difficulty=data.get("difficulty")
            url=data.get("url")
            time=data.get("time")
        except Exception as e:
            name = request.form.get('name')
            country = request.form.get('country')
            category = request.form.get("category")
            difficulty = request.form.get("difficulty")
            url = request.form.get('url')
            time = request.form.get('time')
        query = f"INSERT INTO {table} (name, country, category, difficulty, url, time) VALUES ('{name}', '{country}', '{category}', '{difficulty}', '{url}', {time});"
        print(query)
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()
            return redirect(url_for('home'))
        except Exception as e:
            return f'FAIL POST {name}'
    else:
        with conn.cursor() as cursor:
            query = f'SELECT * FROM {table}'
            
            cursor.execute(query)
            records = cursor.fetchall()
            return render_template('index.html', recipes=list(map(lambda x: list(map(str, x)), records)))


@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    query = f"DELETE FROM {table} where id = '{id}'"
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
        return redirect(url_for('home'))
    except Exception as e:
        return f'FAIL DELETE {id}'


@app.route("/update/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    key = data.get("field")
    value = data.get("value")
    try: 
        value = int(value)
    except Exception as e:
        value = "'{}'".format(value)
    query = f"UPDATE {table} SET {key} = {value} where id = {id};"
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
        return redirect(url_for('home'))
    except Exception as e:
        return f'FAIL PUT {id}'


if __name__ == "__main__":
    port = os.getenv('PORT', '8080')
    app.run(debug=True, host="0.0.0.0", port=int(port))
