from flask import Blueprint, jsonify, request, Response
from models import Environment, Flag, db
from managers.environments import EnvironmentManager 
from uuid import uuid4

environments = Blueprint('environments', __name__)
manager = EnvironmentManager()

@environments.route("", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        payload = request.get_json()
        environment = Environment(payload['name'], payload.get('key')) 

        db.session.add(environment)
        db.session.commit()

        return jsonify(environment.toJson())

    envs = Environment.query.all()
    return jsonify([item.toJson() for item in envs])

@environments.route("/<id>", methods=["GET", "DELETE"])
def delete(id: str):
    environment = Environment.query.get_or_404(id)

    if request.method == 'DELETE':
        db.session.delete(environment)
        db.session.commit()
        return Response(status=204)
    
    return jsonify(environment.toJson())

@environments.route("/<id>/key/generate", methods=["PUT"])
def environment_key_generator(id: str):
    environment = manager.update_key(id)
    return jsonify(environment.toJson())

    
@environments.route("/key/generator", methods=["POST"])
def generate_key():
    return jsonify(uuid4())

@environments.route("/<id>/flags", methods=["PUT"])
def add_flag(id: str):
    environment: Environment = Environment.query.get_or_404(id)

    payload: list = request.get_json()
    for item in payload:
        flag: Flag = Flag.query.get_or_404(item)
        environment.flags.append(flag)
    db.session.commit()
    
    return jsonify(environment.toJson())