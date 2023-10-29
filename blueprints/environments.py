from flask import Blueprint, jsonify, request, Response
from models import Environment, Flag, db

environments = Blueprint('environments', __name__)

@environments.route("", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        payload = request.get_json()
        environment = Environment(payload['name']) 

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

@environments.route("/<id>/flags", methods=["PUT"])
def add_flag(id: str):
    environment: Environment = Environment.query.get_or_404(id)

    payload: list = request.get_json()
    for item in payload:
        flag: Flag = Flag.query.get_or_404(item)
        environment.flags.append(flag)
    db.session.commit()
    
    return jsonify(environment.toJson())