from flask import Flask

from .routes import root_route, hello_route

app = Flask(__name__)

@app.route('/', methods=["GET", "POST", "PUT", "DELETE"])
def v1():
  return root_route()

@app.route('/hello', methods=["GET", "POST"])
def hello():
  return hello_route()
