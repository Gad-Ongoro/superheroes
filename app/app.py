#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

migrate = Migrate(app, db)

api = Api(app)

db.init_app(app)

@app.route('/')
def home():
    return ("""
        <body style = 'background-color: powderblue; text-align: center;'> 
            <div>
                <h1>Heroes and Powers App!</h1>
            </div>
        </body>
    """)

class Heroes(Resource):    
    def get(self):
        all_heroes = [hero.to_dict() for hero in Hero.query.all()]
        response = make_response(jsonify(all_heroes), 200)        
        return response
    
    pass
api.add_resource(Heroes, '/heroes')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
