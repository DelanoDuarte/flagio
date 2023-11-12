from flask import Blueprint, request, jsonify
from guards.auth_guard import guard

authentication = Blueprint('authentication', __name__)

@authentication.route("/token", methods=["POST"])
def authenticate():
    req = request.get_json()
    username = req.get("username", None)
    password = req.get("password", None)
    user = guard.authenticate(username, password)
    ret = {"access_token": guard.encode_jwt_token(user)}
    return (jsonify(ret), 200)