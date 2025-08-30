from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sample",
        auth_plugin='mysql_native_password'
    )
    return conn

@app.route('/')
def home():
    return render_template('demo.html')

@app.route('/sample')
def sample():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert user
    query = "INSERT INTO users (id, username, email, created_at) VALUES (%s, %s, %s, NOW())"
    values = (7, 'ks', 'ab31.com')
    cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()

    return render_template('sample.html')

if __name__ == "__main__":
    app.run(debug=True)
