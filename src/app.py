from flask import Flask
from extensions import db, ma  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite?timeout=10'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

from routes import *


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
