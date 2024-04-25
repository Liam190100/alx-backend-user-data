from flask import Flask, jsonify
from flask_cors import CORS

"""A simple Flask app .
"""

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'], strict_slashes=False)
def status() -> str:
    """GET /
    Return:
        - the welcome page.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
