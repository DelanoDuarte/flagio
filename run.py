from flask import jsonify
from flask_cors import CORS

from app import create_app

from blueprints.flags import blueprint
from blueprints.environments import environments

app = create_app()

# CORS
CORS(app)

@app.route("/api", methods=["GET"])
def index_api():
    return jsonify({"data":"Api Running"})

app.register_blueprint(blueprint, url_prefix="/api/flags")
app.register_blueprint(environments, url_prefix="/api/environments/")

if __name__ == "__main__":
    app.run(host='0.0.0.0')