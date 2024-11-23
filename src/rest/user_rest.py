from flask import Blueprint, request, jsonify, session
from models.user_model import User, UserSchema, db

# Crear Blueprint para las rutas de usuarios
user_bp = Blueprint('user_bp', __name__)

# Serializadores
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Ruta para obtener todos los usuarios
@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

# Ruta para obtener un usuario por ID
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'Usuario no encontrado.'}), 404
    return user_schema.jsonify(user)

# Ruta para añadir un nuevo usuario
@user_bp.route('/', methods=['POST'])
def add_user():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    nivel = request.json.get('nivel', 1)  # Nivel por defecto: usuario

    # Validar que el email o el username no estén ya registrados
    if User.query.filter((User.email == email) | (User.username == username)).first():
        return jsonify({'error': 'El email o el usuario ya están registrados.'}), 400

    # Crear un nuevo usuario
    new_user = User(username=username, password=password, email=email, nivel=nivel)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 201

# Ruta para actualizar un usuario
@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'Usuario no encontrado.'}), 404

    user.username = request.json.get('username', user.username)
    user.password = request.json.get('password', user.password)
    user.email = request.json.get('email', user.email)
    user.nivel = request.json.get('nivel', user.nivel)

    db.session.commit()
    return user_schema.jsonify(user), 200

# Ruta para eliminar un usuario
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'Usuario no encontrado.'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Usuario eliminado exitosamente.'}), 200

# Ruta para iniciar sesión
@user_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Validar credenciales
    user = User.query.filter_by(username=username, password=password).first()
    if not user:
        return jsonify({'error': 'Credenciales incorrectas.'}), 401

    # Guardar información del usuario en la sesión
    session['user'] = {'id': user.id, 'username': user.username, 'nivel': user.nivel}
    return jsonify({'message': 'Inicio de sesión exitoso.', 'user': session['user']}), 200

# Ruta para cerrar sesión
@user_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({'message': 'Sesión cerrada exitosamente.'}), 200
