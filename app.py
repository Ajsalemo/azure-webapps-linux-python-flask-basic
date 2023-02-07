from flask import Flask
from dotenv import load_dotenv

import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def helloWorld():
  o = os.environ.get('TEST')
  return f"Deployed with Github Actions! {o}"
