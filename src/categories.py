from flask import request, render_template, jsonify, redirect, url_for
from app import app
from models import db, User, UserSchema, Category, CategorySchema

# Create an instance of CategorySchema
categories_schema = CategorySchema(many=True)

# Ruta para ver todas las categorías
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return categories_schema.jsonify(categories)

# Ruta para crear una nueva categoría
@app.route('/categories', methods=['POST'])
def add_category():
    name = request.form.get('name')
    description = request.form.get('description')

    new_category = Category(name=name, description=description)
    db.session.add(new_category)
    db.session.commit()
    return redirect(url_for('home'))