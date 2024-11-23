from flask import Blueprint, jsonify

category_bp = Blueprint('category_bp', __name__)

# Obtener todas las categorías
@category_bp.route('/', methods=['GET'])
def get_categories():
    categories = [
        {"id": 1, "name": "Category 1"},
        {"id": 2, "name": "Category 2"}
    ]
    return jsonify(categories)

# Obtener una categoría específica
@category_bp.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = {"id": category_id, "name": f"Category {category_id}"}
    return jsonify(category)
