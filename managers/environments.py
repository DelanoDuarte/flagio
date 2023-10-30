from models import Environment, db
from uuid import uuid4

class EnvironmentManager():

    def update_key(self, id) -> Environment:
        environment: Environment = Environment.query.get(id)
        environment.key = str(uuid4())

        db.session.add(environment)
        db.session.commit()
        return environment