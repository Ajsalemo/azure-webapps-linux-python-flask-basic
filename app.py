from flask import Flask
from flask_cors import CORS

flaskapp = Flask(__name__)
CORS(flaskapp)

@flaskapp.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"