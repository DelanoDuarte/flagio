from flask import Blueprint, request, jsonify
from models import User, db
from guards.auth_guard import guard

from flask_praetorian import current_user_id
import flask_praetorian

users = Blueprint('users', __name__)

@users.route('/', methods=['POST'])
def register():
    """
    Registers a new user by parsing a POST request containing new user info and
    dispatching an email with a registration token

    .. example::
       $ curl http://localhost:5000/register -X POST \
         -d '{
           "username":"Brandt", \
           "password":"herlifewasinyourhands" \
           "email":"brandt@biglebowski.com"
         }'
    """
    req = request.get_json(force=True)
    username = req.get('username', None)
    #email = req.get('email', None)
    password = req.get('password', None)
    new_user = User(
        username=username,
        hash_password=guard.hash_password(password),
        roles='operator, patient',
    )

    db.session.add(new_user)
    db.session.commit()

    # guard.send_registration_email(email, user=new_user)
    ret = {'message': 'successfully sent registration email to user {}'.format(
        new_user.username
    )}
    return (jsonify(ret), 201)


@users.route('/', methods=["GET"])
@flask_praetorian.auth_required
def get_all():
    users = User.query.all()
    return jsonify([item.toJson() for item in users])

@users.route('/<id>', methods=["GET","PUT"])
@flask_praetorian.auth_required
@flask_praetorian.roles_required(['admin'])
def update(id: str):
    user: User = User.query.get(id)

    if request.method == "GET":
        return jsonify(user.toJson())
    
    req = request.get_json()

    user.username = req.get('username', user.username)
    user.roles = req.get('roles', user.roles)
    user.is_active = req.get('active', user.is_active)

    db.session.commit()

    return jsonify(user.toJson())