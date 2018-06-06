from app import app
from flask import request
from app import db
from god import God




@app.route('/god/<id>')
def get_stuff(id):
    god = God.query.get(id)
    if god is not None:
        return god.__str__()
    else:
        return "god with this id does not exist"


@app.route('/god', methods=['POST'])
def add_stuff():
    god_id = request.json['id']
    price = request.json['price']
    weight = request.json['weight']
    name = request.json['name']
    veres = request.json['veres']

    new_god = God()
    new_god.id = god_id
    new_god.price = price
    new_god.weight = weight
    new_god.name = name
    new_god.veres = veres

    db.session.add(new_god)
    db.session.commit()

    return str(new_god.__str__())


@app.route('/god/<id>', methods=['PUT'])
def stuff_update(id):
    price = request.json['price']
    weight = request.json['weight']
    name = request.json['name']
    veres = request.json['veres']

    new_god = God.query.get(id)
    new_god.fish_id = id
    new_god.price = price
    new_god.weight = weight
    new_god.name = name
    new_god.veres = veres

    db.session.commit()

    return new_god.__str__()


@app.route('/god/<id>', methods=['DELETE'])
def stuff_delete(id):
    fish = God.query.get(id)
    db.session.delete(fish)
    db.session.commit()

    return str("Deleting successful")
