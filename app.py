from flask import Flask , render_template 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
    
    def __repr__(self):
        return f'<User {self.username}>'
    
@app.route('/')
def home():
    return render_template('demo.html')

@app.route('/sample')
def sample():
    user = User(id=4, username='abc',email="abc.com")
    db.session.add(user)
    db.session.commit()
    return render_template('sample.html')
if __name__ == "__main__":
    app.run(debug=True)