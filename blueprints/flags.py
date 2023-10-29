from flask import Blueprint, jsonify, request, Response
from models import db, Flag
from managers.flags import FlagManager
from utils.date_utils import to_date

blueprint = Blueprint('flags', __name__)
manager = FlagManager()

@blueprint.route("", methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        payload = request.get_json()
        environments = payload['environments']
        
        flag = manager.create(Flag(payload['name'], 
                                   payload['description'], 
                                   to_date(payload['expiration_date'])
                                ), 
                              environments
                            )
        return jsonify(flag.toJson())


    flags = Flag.query.all()
    return jsonify([item.toJson() for item in flags])

@blueprint.route("/<id>", methods=["GET", "DELETE"])
def delete(id: str):
    flag = Flag.query.get_or_404(id)

    if request.method == 'DELETE':
        db.session.delete(flag)
        db.session.commit()
        return Response(status=204)
    
    return jsonify(flag.toJson())

@blueprint.route("/<id>/deactivate", methods=["POST"])
def deactivate(id: str):
    flag = manager.change_flag_stauts_to(id, False)
    return jsonify(flag.toJson())

@blueprint.route("/<id>/activate", methods=["POST"])
def activate(id: str):
    flag = manager.change_flag_stauts_to(id, True)
    return jsonify(flag.toJson())