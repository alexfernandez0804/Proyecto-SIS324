from flask import Blueprint, request, render_template, redirect, url_for
from models import db, Category, CategorySchema

category_bp = Blueprint('category_bp', __name__)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

@category_bp.route('/categories', methods=['GET'])
def list_categories():
    """Listar todas las categorías"""
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

@category_bp.route('/categories/add', methods=['POST'])
def add_category():
    """Agregar una nueva categoría"""
    nombre = request.form['nombre']
    descripcion = request.form.get('descripcion', '')

    new_category = Category(nombre=nombre, descripcion=descripcion)
    db.session.add(new_category)
    db.session.commit()
    return redirect(url_for('category_bp.list_categories'))

