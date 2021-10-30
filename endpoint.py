import flask
import sys
from flask import request, jsonify

# Create a flask instance
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def post_result():
    username = request.json['username']
    password = request.json['password']
    print("\n\nUsername: " + username + "\n", file = sys.stderr)
    print("Password: " + password + "\n\n", file = sys.stderr)
    return "success"



app.run()