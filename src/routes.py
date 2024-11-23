from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models import db, User, UserSchema, Category, CategorySchema

# Crear Blueprint para las rutas
routes_bp = Blueprint('routes', __name__)

# Serializadores
user_schema = UserSchema()
users_schema = UserSchema(many=True)

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

# Página de inicio
@routes_bp.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener todos los usuarios (API REST)
@routes_bp.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

# Página principal después de iniciar sesión
@routes_bp.route('/home')
def home():
    if 'user' not in session:
        flash('Por favor, inicia sesión para acceder a esta página.', 'error')
        return redirect(url_for('routes.login'))
    return render_template('home.html')

# Página para continuar
@routes_bp.route('/continue')
def continue_page():
    if 'user' not in session:
        flash('Por favor, inicia sesión para acceder a esta página.', 'error')
        return redirect(url_for('routes.login'))
    return render_template('continue.html')

# Ruta para registrar un nuevo usuario
@routes_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')
        correo = request.form.get('correo')

        # Validar si el usuario o correo ya están registrados
        existing_user = User.query.filter((User.usuario == usuario) | (User.correo == correo)).first()
        if existing_user:
            flash('El usuario o correo ya están registrados.', 'error')
            return redirect(url_for('routes.register'))

        # Crear un nuevo usuario con nivel 1 (usuario)
        try:
            new_user = User(
                nombre=nombre, 
                apellido=apellido, 
                usuario=usuario, 
                contraseña=contraseña, 
                correo=correo, 
                nivel=1
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Registro exitoso. Por favor, inicia sesión.', 'success')
            return redirect(url_for('routes.login'))
        except Exception as e:
            flash(f'Ocurrió un error al registrar: {e}', 'error')
            return redirect(url_for('routes.register'))

    return render_template('register.html')

# Ruta para iniciar sesión
@routes_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')

        # Validar credenciales
        user = User.query.filter_by(usuario=usuario, contraseña=contraseña).first()
        if user:
            # Guardar usuario en la sesión
            session['user'] = {'id': user.id, 'usuario': user.usuario, 'nivel': user.nivel}
            if user.nivel == 0:  # Administrador
                flash('Bienvenido administrador.', 'success')
                return redirect(url_for('routes.dashboard'))
            elif user.nivel == 1:  # Usuario
                flash('Inicio de sesión exitoso. Bienvenido usuario.', 'success')
                return redirect(url_for('routes.home'))
        else:
            flash('Credenciales incorrectas. Por favor, intenta de nuevo.', 'error')
            return redirect(url_for('routes.login'))

    return render_template('login.html')

# Ruta para cerrar sesión
@routes_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Sesión cerrada con éxito.', 'success')
    return redirect(url_for('routes.index'))

# Ruta para ver categorías dinámicamente
@routes_bp.route('/category/<int:category_id>')
def view_category(category_id):
    category = Category.query.get_or_404(category_id)
    return render_template('category.html', category=category)

# Ruta para el dashboard (solo accesible por administradores)
@routes_bp.route('/dashboard')
def dashboard():
    user = session.get('user')
    if not user or user['nivel'] != 0:
        flash('Acceso denegado. Solo administradores pueden acceder.', 'error')
        return redirect(url_for('routes.login'))

    return render_template('dashboard.html')

# Rutas para gestionar usuarios
@routes_bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if 'user' not in session or session['user']['nivel'] != 0:
        flash('Acceso denegado. Solo administradores pueden acceder.', 'error')
        return redirect(url_for('routes.login'))

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')
        correo = request.form.get('correo')
        nivel = request.form.get('nivel', 1)  # Nivel por defecto: usuario

        new_user = User(
            nombre=nombre, 
            apellido=apellido, 
            usuario=usuario, 
            contraseña=contraseña, 
            correo=correo, 
            nivel=nivel
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Usuario agregado con éxito.', 'success')
        return redirect(url_for('routes.dashboard'))

    return render_template('add_user.html')
