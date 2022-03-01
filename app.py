from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(flaskapp)

@flaskapp.route("/")
def helloWorld():
  return "Deployed with a zip"
