# Imports 
from flask import Flask,redirect,render_template,request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# My app
app = Flask(__name__)

Scss(app, static_dir='static',asset_dir='static/scss')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class MyTask(db.Model):
    log_id = db.Column(db.Integer, primary_key=True)
    cash = db.Column(db.Integer, default=0)
    cash_type = db.Column(db.String(100), default="debit")
    desc = db.Column(db.String(100), default="")
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Task {self.log_id}"

    
#home 
@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)