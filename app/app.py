#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
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


""" HEROES """
class Heroes(Resource):    
    def get(self):
        all_heroes = [hero.to_dict() for hero in Hero.query.all()]
        response = make_response(jsonify(all_heroes), 200)        
        return response
    
    pass
api.add_resource(Heroes, '/heroes')

class Hero_by_id(Resource):
    def get(self, id):
        hero = Hero.query.filter_by(id = id).first()
        if hero:
            return make_response(jsonify(hero.to_dict()), 200)
        else:
            response = make_response({"error": "Hero not found"}, 404)
            return response
                
api.add_resource(Hero_by_id, '/heroes/<int:id>')

""" POWERS """
class Powers(Resource):
    def get(self):
        powers = [power.to_dict() for power in Power.query.all()]
        response = make_response(jsonify(powers), 200)
        return response
    
api.add_resource(Powers, '/powers')

class Powers_by_id(Resource):
    def get(self, id):
        power = Power.query.filter_by(id = id).first()
        if power:            
            response = make_response(jsonify(power.to_dict()), 200)
            return response
        else:
            response = make_response(jsonify({"error": "Power not found"}), 404)
            return response
        
    def patch(self, id):
        power = Power.query.filter_by(id = id).first()
        if power:
            data = request.get_json()
            for attr in data:
                setattr(power, attr, data.get(attr))
                
            db.session.commit()
            
            response = make_response(jsonify({
                "id" : power.id,
                "name" : power.name,
                "description" : power.description                
            }), 200)            
            return response
        
        else:
            response = make_response(jsonify({
                "error": "Power not found"
            }), 404)
            return response
api.add_resource(Powers_by_id, '/powers/<int:id>')


""" HERO_POWERS """
class Hero_Powers(Resource):
    def post(self):
        data = request.get_json()
        new_hero_power = HeroPower(
            strength = data["strength"],
            power_id = data['power_id'],
            hero_id = data["hero_id"]
        )
        db.session.add(new_hero_power)
        db.session.commit()
        
        response = make_response(jsonify(new_hero_power), 201)
        return response
        pass

api.add_resource(Hero_Powers, '/hero_powers')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
