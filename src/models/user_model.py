from extensions import db, ma

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

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
