from flask import Flask
<<<<<<< HEAD
=======
from dotenv import load_dotenv

import os

load_dotenv()
>>>>>>> 16d4a8dd562c7191e7222b24007dc6578c95f88f

app = Flask(__name__)

@app.route("/")
<<<<<<< HEAD
def index():
  return "azure-webaps-linux-python-flask-basic"


@app.route("/api/health")
def health():
  print("Health Check endpoint hit")
  return "OK";
=======
def helloWorld():
  o = os.environ.get('TEST')
  return f"Deployed with Github Actions! - {o}"
>>>>>>> 16d4a8dd562c7191e7222b24007dc6578c95f88f
