from flask import Flask
from extensions import db, ma  

# Crear la instancia de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite?timeout=10'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

from product_routes import product_bp  
from category_routes import category_bp  

app.register_blueprint(product_bp)  
app.register_blueprint(category_bp)  


from routes import *  

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)  