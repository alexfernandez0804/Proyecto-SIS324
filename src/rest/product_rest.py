from flask import Blueprint, jsonify

product_bp = Blueprint('product_bp', __name__)

# Obtener todos los productos
@product_bp.route('/', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Product 1", "category": "Category 1"},
        {"id": 2, "name": "Product 2", "category": "Category 2"}
    ]
    return jsonify(products)

# Obtener un producto específico
@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = {"id": product_id, "name": f"Product {product_id}", "category": "Category X"}
    return jsonify(product)
