from flask import request

from ..controllers import get_root_controller, post_root_controller, any_root_controller

def root_route():
  if(request.method == "GET"):
    return get_root_controller()
  elif(request.method == "POST"):
    return post_root_controller()
  else:
    return any_root_controller()
