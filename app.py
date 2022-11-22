from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
  print("This is a debug breakpoint")
  return "Deployed with Local Git!"

