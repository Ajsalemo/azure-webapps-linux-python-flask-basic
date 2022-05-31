from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloWorld():
  return "Deployed with DevOps build and release!"
