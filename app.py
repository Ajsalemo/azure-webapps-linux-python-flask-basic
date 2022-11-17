from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  print("This is a debug breakpoint")
  return "Deployed with Local Git!"

