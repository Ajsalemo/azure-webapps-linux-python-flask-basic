from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "azure-webaps-linux-python-flask-basic (v1.0)"


@app.route("/api/health")
def health():
  print("Health Check endpoint hit")
  return "OK";
