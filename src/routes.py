from flask import request, render_template, redirect, url_for, flash
from app import app
from models import db, User, UserSchema, Category, CategorySchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

@app.route('/home')
def home():
    return render_template('home.html')  

@app.route('/continue')
def continue_page():
    return render_template('continue.html')

@app.route('/categori_1')
def categori_1():
    return render_template('categori_1.html')

@app.route('/categori_2')
def categori_2():
    return render_template('categori_2.html')

@app.route('/categori_3')
def categori_3():
    return render_template('categori_3.html')

@app.route('/categori_4')
def categori_4():
    return render_template('categori_4.html')

@app.route('/categori_5')
def categori_5():
    return render_template('categori_5.html')

@app.route('/categori_6')
def categori_6():
    return render_template('categori_6.html')

@app.route('/categori_7')
def categori_7():
    return render_template('categori_7.html')

@app.route('/categori_8')
def categori_8():
    return render_template('categori_8.html')

@app.route('/categori_9')
def categori_9():
    return render_template('categori_9.html')




@app.route('/users', methods=['POST'])
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    new_user = User(username=username, password=password, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home'))  

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)



@app.route('/users_contiene', methods=['POST'])
def contains_user():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    
    user = User.query.filter_by(username=username, password=password, email=email).first()
    
    if user:
        return redirect(url_for('home'))  
    else:
        return redirect(url_for('index', error='Usuario no encontrado o credenciales incorrectas'))

 