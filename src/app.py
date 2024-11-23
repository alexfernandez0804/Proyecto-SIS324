from flask import Flask
from extensions import db, ma

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Configuraciones de la aplicación
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite?timeout=10'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'tu_clave_secreta_segura'  # Cambia esta clave por una única y segura

# Inicializar extensiones
db.init_app(app)
ma.init_app(app)

# Importar Blueprints
from rest.user_rest import user_bp
from rest.category_rest import category_bp
from routes import routes_bp  # Importar el Blueprint de las rutas generales

# Registrar Blueprints
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(category_bp, url_prefix='/api/categories')
app.register_blueprint(routes_bp)  # Registrar el Blueprint principal con rutas

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crear las tablas en la base de datos si no existen
    app.run(debug=True)
