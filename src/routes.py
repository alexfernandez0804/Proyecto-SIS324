from flask import render_template, jsonify
from app import app
from models import User, Category, UserSchema, CategorySchema

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para ver todos los usuarios (ejemplo adicional)
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users))

# Añade más rutas según las necesidades de tu aplicación
