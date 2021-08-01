from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello_world", methods=["GET"])
def say_hello_world():
    my_response_body = "Hello, World!"
    
    return my_response_body