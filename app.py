from flask import Flask
from flask_migrate import Migrate
from models import db, User
from guards.auth_guard import guard

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'mysecret001'
    app.debug = True

    guard.init_app(app, User)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flagio.db"
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432/flask-app'
    app.config["JWT_ACCESS_LIFESPAN"] = {"hours": 12}
    app.config["JWT_REFRESH_LIFESPAN"] = {"days": 30}

    # Database
    db.init_app(app)

    # Migration 
    migrate.init_app(app, db)
    return app