"""
NEED TO CREATE ENDPOINTS
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


# USER ENDPOINTS
@app.route('/users', methods=['GET','POST'])
def get_or_create_users():
    if request.method == "GET":
        return "This is a GET request from Users endpoint"
    elif request.method == "POST":
        return "This is a POST request from 'Users' endpoint"
    

@app.route('/users/<int:user_id>', methods=['GET','DELETE'])
def get_or_delete_single_user(user_id):
    if request.method == "GET":
        return "This is a GET request from 'Single User' endpoint"
    elif request.method == "POST":
        return "This is a POST request from 'Single User' endpoint"


# CHARACTER ENDPOINTS
@app.route('/characters', methods=['GET','POST'])
def get_or_post_characters():
      if request.method == "GET":
          return "This is a GET request from 'Get all or Post Character' endpoint"
      elif request.method == "POST":
          return "This is a POST request from 'Get all or Post Character' endpoint"


@app.route('/characters/<int:character_id>', methods=['GET','DELETE'])
def get_or_delete_single_character(character_id):
    if request.method == "GET":
        return "This is a GET request from 'Single Character' endpoint"
    elif request.method == "POST":
          return "This is a POST request from 'Single Character' endpoint"
    

# PLANET ENDPOINTS
@app.route('/planets', methods=['GET','POST'])
def get_or_post_planets():
      if request.method == "GET":
          return "This is a GET request from 'All planets' endpoint"
      elif request.method == "POST":
          return "This is a POST request from 'All planets endpoint"


@app.route('/planets/<int:planet_id>', methods=['GET','DELETE'])
def get_or_delete_single_planet(planet_id):
    if request.method == "GET":
        return "This is a GET request from 'Single Planet' endpoint"
    elif request.method == "POST":
          return "This is a POST request from 'Single Planet' endpoint"


# FAVORITE ENDPOINTS
@app.route('/favorites/<int:favorite_id>', methods=['GET','DELETE'])
def get_or_delete_favorite(favorite_id):
    if request.method == "GET":
        return "This is a GET request from 'Favorite' endpoint"
    elif request.method == "DELETE":
        return "This is a DELETE request from 'Single Planet' endpoint"


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
