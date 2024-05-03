from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.String(80), unique=True)
    favoritos_personas = db.relationship('FavoritosPersonas', backref='users')
    favoritos_planetas = db.relationship('FavoritosPlanetas', backref='users')
    favoritos_naves = db.relationship('FavoritosNaves', backref='users')

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }

class Personas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    birth_year = db.Column(db.String(250), unique=False, nullable=False)
    eye_color = db.Column(db.String(250), unique=False, nullable=False)
    gender = db.Column(db.String(250), unique=False, nullable=False)
    hair_color = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Personas %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color
        }

class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    diameter = db.Column(db.String(250), unique=False, nullable=False)
    rotation_period = db.Column(db.String(250), unique=False, nullable=False)
    orbital_period = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Planetas %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period
        }

class Naves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    model = db.Column(db.String(250), unique=False, nullable=False)
    nave_class = db.Column(db.String(250), unique=False, nullable=False)
    length = db.Column(db.String(250), unique=False, nullable=False)
    

    def __repr__(self):
        return '<Naves %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "nave_class": self.nave_class,
            "length": self.length
        }

class FavoritosPersonas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    personas_id = db.Column(db.Integer, db.ForeignKey('personas.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<FavoritosPersonas %r>' % self.personas_id

    def serialize(self):
        return {
            "id": self.id,
            "personas_id": self.personas_id
        }

class FavoritosPlanetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planetas_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<FavoritosPlanetas %r>' % self.planetas_id

    def serialize(self):
        return {
            "id": self.id,
            "planetas_id": self.planetas_id
        }

class FavoritosNaves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naves_id = db.Column(db.Integer, db.ForeignKey('naves.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<FavoritosNaves %r>' % self.naves_id

    def serialize(self):
        return {
            "id": self.id,
            "nave_id": self.naves_id
        }