from extensions import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# Tabla User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    apellido = db.Column(db.String(150), nullable=False)
    usuario = db.Column(db.String(150), unique=True, nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    contraseña = db.Column(db.String(150), nullable=False)
    nivel = db.Column(db.Integer, default=1)  # Nivel: 0=Admin, 1=Usuario

    def __repr__(self):
        return f"<User {self.usuario}>"

# Tabla Category
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    logo = db.Column(db.String(255), nullable=True)

    productos = db.relationship('Product', back_populates='categoria', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Category {self.nombre}>"

# Tabla Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String(255), nullable=True)
    categories_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete='CASCADE'), nullable=False)

    categoria = db.relationship('Category', back_populates='productos')
    filtros = db.relationship('Filter', secondary='product_filter', back_populates='productos')

    def __repr__(self):
        return f"<Product {self.nombre}, Precio: {self.precio}>"

# Tabla Filter
class Filter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    tipo = db.Column(db.String(100), nullable=False)  # Ejemplo: Equipo, Piloto, Género, etc.

    productos = db.relationship('Product', secondary='product_filter', back_populates='filtros')

    def __repr__(self):
        return f"<Filter {self.nombre}, Tipo: {self.tipo}>"

# Tabla intermedia product_filter
class ProductFilter(db.Model):
    __tablename__ = 'product_filter'
    products_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete='CASCADE'), primary_key=True)
    filters_id = db.Column(db.Integer, db.ForeignKey('filter.id', ondelete='CASCADE'), primary_key=True)

# Esquemas para serialización
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

class FilterSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Filter
        load_instance = True
