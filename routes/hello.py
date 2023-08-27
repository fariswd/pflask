from flask import request

from ..controllers import get_hello_controller, post_hello_controller, any_hello_controller

def hello_route():
  if(request.method == "GET"):
    return get_hello_controller()
  elif(request.method == "POST"):
    return post_hello_controller()
  else:
    return any_hello_controller()
