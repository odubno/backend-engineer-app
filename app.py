import os
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


# Create a function to connect to the SQLite database
def connect_db():
    conn = None
    try:
        conn = sqlite3.connect('employees.db')
    except sqlite3.Error as e:
        print(e)
    return conn


# Create an endpoint to return a list of id and gender from the employees database
@app.route('/employees')
def get_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, gender FROM employees')
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({'id': row[0], 'gender': row[1]})
    return jsonify(data)


if __name__ == '__main__':
    # Read the PORT environment variable, or use 8080 if it's not set
    port = int(os.environ.get('PORT', 8085))
    app.run(host='0.0.0.0', port=port)
