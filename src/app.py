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
from models import db, User,Personas,Planetas, FavoritosPersonas,FavoritosPlanetas,FavoritosNaves, Naves
#importar "cada cajita del modelos" con su nombre

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db) #dejar como esta##
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object----dejar como esta---
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints-----dejar como esta---
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])   #TIPO ESTO, GET THE USER (Todo usuario)
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

    
    
#--------------- mi codigo---------#
#endpoint @ GET ALL "user"
@app.route('/user', methods=['GET'])
def get_user():
     
     user_query = User.query.all()
     """ results_user = list(map(lambda item: item.serialize(), user_query)) """
     if not user_query:
          return jsonify({"msg":"NO hay user"}),404
     else:
          return jsonify(user_query),200
     
#endpoint Get "1 user (por id)"
@app.route('/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):

    user_query = User.query.get(user_id)  

    if not user_query:
        return jsonify({"msg": "User not found"}), 404
    else:
        return jsonify(user_query.serialize()), 200 
# endpoint @ - GET ALL "personas"
@app.route('/personas', methods=['GET'])
def get_personas():
     
     personas_query = Personas.query.all()
     if not personas_query:
          return jsonify({"msg":"NO hay personas"}),404
     else:
          return jsonify(personas_query),200
    
#endpoint Get each "personas" by ID
@app.route('/personas/<int:personas_id>', methods=['GET'])
def get_one_personas(personas_id):

    personas_query = Personas.query.get(personas_id)  

    if not personas_query:
        return jsonify({"msg": "Personas not found"}), 404
    else:
        return jsonify(personas_query.serialize()), 200 
#endpoint GET ALL "planetas"
@app.route('/planetas', methods=['GET'])
def get_planetas():
     
     planetas_query = Planetas.query.all()
     if not planetas_query:
          return jsonify({"msg":"NO hay planetas"}),404
     else:
          return jsonify(planetas_query),200
     
#endpoint GET each "planeta" by ID
@app.route('/planetas/<int:planetas_id>', methods=['GET'])
def get_one_planetas(planetas_id):

    planetas_query = Planetas.query.get(planetas_id)  

    if not planetas_query:
        return jsonify({"msg": "Planetas not found"}), 404
    else:
        return jsonify(planetas_query.serialize()), 200 
#endpoint GET ALL "naves"
@app.route('/naves', methods=['GET'])
def get_naves():
     
     naves_query = Planetas.query.all()
     if not naves_query:
          return jsonify({"msg":"NO hay naves"}),404
     else:
          return jsonify(naves_query),200
     
#endpoint GET each "nave"
@app.route('/naves/<int:naves_id>', methods=['GET'])
def get_one_naves(naves_id):

    naves_query = Naves.query.get(naves_id)  

    if not naves_query:
        return jsonify({"msg": "naves not found"}), 404
    else:
        return jsonify(naves_query.serialize()), 200 
    
    #### POST ######
#endpoint for POST "personas" FAVORITOS
@app.route('/favoritos/personas/', methods=['POST'])
def create_favoritos_personas():
 body = request.json
 favoritos_personas_query = FavoritosPersonas.query.filter_by(Personas_id=body["personas_id"]).first()
 if favoritos_personas_query:
    return jsonify({"msg": "Favorite already exists"}), 409

 new_personas_favoritos = FavoritosPersonas(Personas_id=body["personas_id"], user_id=body["user_id"])
 db.session.add(new_personas_favoritos)
 db.session.commit()
 return jsonify({"msg": "Favorito created"}), 200

# endopoint for POST planetas FAVORITOS

@app.route('/favoritos/planetas/', methods=['POST'])
def create_favoritos_planetas():
  body = request.json
  favoritos_planetas_query = FavoritosPlanetas.query.filter_by(Planetas_id=body["planetas_id"]).first()
  if favoritos_planetas_query:
    return jsonify({"msg": "Favorite already exists"}), 409

  new_planetas_favoritos = FavoritosPlanetas(Planetas_id=body["planetas_id"], user_id=body["user_id"])
  db.session.add(new_planetas_favoritos)
  db.session.commit()
  return jsonify({"msg": "Favorito created"}), 200

#endpoint for POST naves FAVORITOS
@app.route('/favoritos/naves/', methods=['POST'])
def create_favoritos_naves():
  body = request.json
  favoritos_naves_query = FavoritosNaves.query.filter_by(Naves_id=body["naves_id"]).first()
  if favoritos_naves_query:
    return jsonify({"msg": "Favorite already exists"}), 409

  new_naves_favoritos = FavoritosNaves(Naves_id=body["naves_id"], user_id=body["user_id"])
  db.session.add(new_naves_favoritos)
  db.session.commit()
  return jsonify({"msg": "Favorito created"}), 200

### endpoint DELETE user ###
@app.route('/user/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    remove_user = User.query.get(user_id)
    if not remove_user:
        return jsonify({"msg": "User not found"}), 400
    
    db.session.delete(remove_user)
    db.session.commit()

    return jsonify({"msg":"user deleted"}), 200

#endpoint DELETE personas.favs
@app.route('/favorospersonas/<int:favoritospersonas_id>/', methods=['DELETE'])
def delete_personas(user_id):
    remove_personas = Personas.query.get(user_id)
    if not remove_personas:
        return jsonify({"msg": "personas not found"}),200
    
    db.session.delete(remove_personas)
    db.session.commit()

    return jsonify({"msg":"prsonas deleted"})

#enpoint DELETE naves.fav
@app.route('/favoritosnaves/<int:favoritosnaves_id>/', methods=['DELETE'])
def delete_naves(user_id):
    remove_naves = Naves.query.get(user_id)
    if not remove_naves:
        return jsonify({"msg": "naves not found"}),200
    
    db.session.delete(remove_naves)
    db.session.commit()

    return jsonify({"msg":"naves deleted"})

#endpoint DELETE planetas.favs
@app.route('/favoritosplanetas/<int:favoritosplanetas_id>/', methods=['DELETE'])
def delete_planetas(user_id):
    remove_planetas = Planetas.query.get(user_id)
    if not remove_planetas:
        return jsonify({"msg": "planetas not found"}),200
    
    db.session.delete(remove_planetas)
    db.session.commit()

    return jsonify({"msg":"planetas deleted"})

#BORRAR TODOS LOS DATOS 
@app.route('/wipeall', methods=['GET'])
def database_wipe():
    try:
        db.reflect()
        db.drop_all()
        db.session.commit()
    except Exception as e:
        return "mec", 500
    return "ok", 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)







