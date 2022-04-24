"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Fav_people, Fav_planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def getUser():
    all_user = User.query.all()
    arreglo_user = list(map(lambda x:x.serialize(), all_user))
    return jsonify({"msg":arreglo_user})

@app.route('/people', methods=['GET'])
def getPeople():
    all_people = People.query.all()
    arreglo_people = list(map(lambda x:x.serialize(), all_people))
    return jsonify({"msg":arreglo_people})

@app.route('/people/<int:people_id>', methods=['GET'])
def getPeopleID(people_id):
    one_people = People.query.get(people_id)
    if one_people:
        return jsonify({"msg": one_people.serialize()})
    else:
        return "Error, ingresa otro id"

@app.route('/planets', methods=['GET'])
def getPlanets():
    all_planets = Planets.query.all()
    arreglo_planets = list(map(lambda x:x.serialize(), all_planets))
    return jsonify({"msg":arreglo_planets})

@app.route('/planets/<int:planets_id>', methods=['GET'])
def getPlanetsID(planets_id):
    one_planet = Planets.query.get(planets_id)
    if one_planet:
        return jsonify({"msg": one_planet.serialize()})
    else:
        return "Error, ingresa otro id"

@app.route('/favPeople', methods=['GET'])
def getfavPeople():
    all_favPeople= Fav_people.query.all()
    arreglo_fav = list(map(lambda x:x.serialize(), all_favPeople))
    return jsonify({"msg": arreglo_fav})

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def addFavPeople(people_id):
    user = request.get_json()
    #chequear si existe el usuario
    checkUser = User.query.get(user['id'])
    if checkUser:
        newFav = Fav_people()
        newFav.id_user = user['id']
        newFav.uid_people=people_id

        db.session.add(newFav)
        db.session.commit()
        return("todo salió bien :D")
    else:
        return("Algo salio mal :c")

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def deleteFavPeople(people_id):
    user = request.get_json()
    allFavs = Fav_people.query.filter_by(id_user=user['id'], uid_people=people_id).all()

    for i in allFavs:
        db.session.delete(i)
    db.session.commit()
    return("Todo salio bien!")

@app.route('/favPlanets', methods=['GET'])
def getfavPlanets():
    all_favPlanets= Fav_planets.query.all()
    arreglo_fav = list(map(lambda x:x.serialize(), all_favPlanets))
    return jsonify({"msg": arreglo_fav})

@app.route('/favorite/planets/<int:planets_id>', methods=['POST'])
def addFavPlanets(planets_id):
    user = request.get_json()
    #chequear si existe el usuario
    checkUser = User.query.get(user['id'])
    if checkUser:
        newFav = Fav_planets()
        newFav.id_user = user['id']
        newFav.uid_planets=planets_id

        db.session.add(newFav)
        db.session.commit()
        return("todo salió bien :D")
    else:
        return("Algo salio mal :c")

@app.route('/favorite/planets/<int:planets_id>', methods=['DELETE'])
def deleteFavPlanets(planets_id):
    user = request.get_json()
    allFavs = Fav_planets.query.filter_by(id_user=user['id'], uid_planets=planets_id).all()

    for i in allFavs:
        db.session.delete(i)
    db.session.commit()
    return("Todo salio bien!")


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
