from flask import Flask
from flask_migrate import Migrate
from models import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'mysecret001'
    app.debug = True

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flagio.db"
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432/flask-app'

    # Database
    db.init_app(app)

    # Migration 
    migrate.init_app(app, db)
    return app