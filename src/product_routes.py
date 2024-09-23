from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from models import db, Product, ProductSchema

product_bp = Blueprint('product_bp', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@product_bp.route('/products', methods=['GET'])
def list_products():
    """Listar todos los productos"""
    products = Product.query.all()
    return render_template('products.html', products=products)

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    """Mostrar detalles de un producto específico"""
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@product_bp.route('/products/add', methods=['POST'])
def add_product():
    """Agregar un nuevo producto"""
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    categoria_id = request.form['categoria_id']
    
    new_product = Product(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        cantidad=cantidad,
        categoria_id=categoria_id
    )
    
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('product_bp.list_products'))

@product_bp.route('/products/search', methods=['GET'])
def search_products():
    """Buscar productos por nombre o categoría"""
    search_term = request.args.get('search_term', '')
    categoria_id = request.args.get('categoria_id', None)

    query = Product.query.filter(Product.nombre.ilike(f'%{search_term}%'))

    if categoria_id:
        query = query.filter_by(categoria_id=categoria_id)
    
    products = query.all()
    return render_template('products.html', products=products)


