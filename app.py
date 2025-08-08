from flask import Flask, render_template, request, redirect
import psycopg2
import os

app = Flask(__name__)

# Database config
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'mydb')
DB_USER = os.environ.get('DB_USER', 'myuser')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'mypassword')

def get_db_connection():
    import psycopg2
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    # Create table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INT NOT NULL
        );
    ''')
    conn.commit()  # <--- Important to commit DDL changes
    # Fetch users
    cur.execute('SELECT name, age FROM users ORDER BY id DESC;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('form.html', users=users)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']

    conn = get_db_connection()
    cur = conn.cursor()
    # Insert user
    cur.execute('INSERT INTO users (name, age) VALUES (%s, %s);', (name, age))
    conn.commit()  # <--- Commit the insert
    cur.close()
    conn.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
