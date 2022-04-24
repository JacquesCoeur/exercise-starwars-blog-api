from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=True)
    height = db.Column(db.Integer, unique=False, nullable=True)
    mass = db.Column(db.Float, unique=False, nullable=True)

    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass
        }

class Planets(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "url": self.url
        }

class Fav_people(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid_people = db.Column(db.Integer, db.ForeignKey('people.uid'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    people = db.relationship('People')
    user = db.relationship('User')

    def serialize(self):
        return {
            "uid_people": self.uid_people,
            "id_user": self.id_user,
            "id": self.id
        }

class Fav_planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid_planets = db.Column(db.Integer, db.ForeignKey('planets.uid'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    planets = db.relationship('Planets')
    user = db.relationship('User')

    def serialize(self):
        return {
            "uid_planets": self.uid_planets,
            "id_user": self.id_user,
            "id": self.id
        }


