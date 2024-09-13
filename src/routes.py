from flask import request, render_template, jsonify, redirect, url_for
from app import app
from models import db, User, UserSchema, Category, CategorySchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para ver todos los usuarios
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

# Ruta para crear un nuevo usuario
@app.route('/users', methods=['POST'])
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    new_user = User(username=username, password=password, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home'))  # Redirige a la página principal tras la creación

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

