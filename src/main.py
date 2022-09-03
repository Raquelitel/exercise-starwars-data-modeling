import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
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

# GET
@app.route('/user', methods=['GET'])
def get_user():
    queryset= User.query.all()
    user_list = [user.serialize() for user in queryset]
    response_body = {

        "success": True,
        "results": user_list,
        "msg": "hola"
    }
    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def get_people():
    response_body = {"msg":"Hola people"}
    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def get_people():
    queryset = people.query.all()
    people_list = [people.serialize() for people in queryset]
    response_body = {

        "success": True,
        "results": people_list
    }
    return jsonify(response_body), 200














if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)