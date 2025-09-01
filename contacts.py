from flask import Flask, redirect, render_template,request
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

@app.route('/',methods=['GET','POST'])
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    d = "select * from contacts"
    cursor.execute(d)
    contacts = cursor.fetchall()
    return render_template('contacts.html', contacts=contacts)

@app.route('/add',methods=['POST'])
def add():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert user
    query = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s,%s)"
    values = (request.form['name'], request.form['phone'], request.form['email'])
    cursor.execute(query, values)
    b=request.form['name']
    c=request.form['phone']
    d=request.form['email']
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete_contact(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    d = "delete from contacts where id = %s"
    cursor.execute(d, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

@app.route('/update/<int:id>',methods=['GET','POST'])
def update_contact(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        # Update contact
        query = "UPDATE contacts SET name = %s, phone = %s, email = %s WHERE id = %s"
        values = (request.form['name'], request.form['phone'], request.form['email'], id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
    d = "select * from contacts where id = %s"
    cursor.execute(d, (id,))
    contact = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update.html', contact=contact)

if __name__ == "__main__":
    app.run(debug=True)
