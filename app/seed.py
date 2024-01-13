from app import app
from models import db, Hero, Power, HeroPower
from random import choice as rc

# heroes
heroes = [
    { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
    { "name": "Doreen Green", "super_name": "Squirrel Girl" },
    { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
    { "name": "Janet Van Dyne", "super_name": "The Wasp" },
    { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
    { "name": "Carol Danvers", "super_name": "Captain Marvel" },
    { "name": "Jean Grey", "super_name": "Dark Phoenix" },
    { "name": "Ororo Munroe", "super_name": "Storm" },
    { "name": "Kitty Pryde", "super_name": "Shadowcat" },
    { "name": "Elektra Natchios", "super_name": "Elektra" }
]
with app.app_context():
    Hero.query.delete()
    for hero in heroes:
        new_hero = Hero(name = hero["name"], super_name = hero["super_name"])
        db.session.add(new_hero)
        db.session.commit()

# powers
powers = [
    { "name": "super strength", "description": "gives the wielder super-human strengths" },
    { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
    { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
    { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
]
with app.app_context():
    Power.query.delete()
    for power in powers:
        new_power = Power(name = power["name"], description = power["description"])
        db.session.add(new_power)
        db.session.commit()

# hero_powers
strengths = ["Strong", "Weak", "Average"]
hero_identities = list(range(len(heroes)))
power_identities = list(range(len(powers)))

with app.app_context():
    HeroPower.query.delete()
    for hero in heroes:
        new_hero_power = HeroPower(strength = rc(strengths), hero_id = rc(hero_identities), power_id = rc(power_identities))
        db.session.add(new_hero_power)
        db.session.commit()