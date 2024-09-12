from flask import Flask
from extensions import db, ma  # Importar desde extensions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite?timeout=10'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

from routes import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Esto crea las tablas en la base de datos
    app.run(debug=True)
