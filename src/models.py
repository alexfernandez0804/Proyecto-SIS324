from extensions import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    imagen = db.Column(db.String(255))
    descripcion = db.Column(db.Text, nullable=True)  

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    categoria = db.relationship('Category', backref='productos')


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
