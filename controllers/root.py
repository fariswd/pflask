def get_root_controller():
  return {
    "status": 200,
    "message": "GET FROM CONTROLLER"
  }

def post_root_controller():
  return {
    "status": 200,
    "message": "POST FROM CONTROLLER"
  }

def any_root_controller():
  return {
    "status": 400,
    "message": ":("
  }
