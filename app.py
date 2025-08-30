from flask import Flask, render_template,request
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

@app.route('/sample',methods=['POST'])
def sample():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert user
    query = "INSERT INTO users (id, username, email, created_at) VALUES (%s, %s, %s, NOW())"
    values = (request.form['id'], request.form['username'], request.form['email'])
    cursor.execute(query, values)
    a=request.form['id']
    b=request.form['username']
    c=request.form['email']
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('sample.html',id=a,username=b,email=c)

if __name__ == "__main__":
    app.run(debug=True)
