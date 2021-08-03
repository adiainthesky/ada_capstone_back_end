from flask import Blueprint

user_bp = Blueprint("user", __name__, url_prefix="/user")
trip_bp = Blueprint("trip", __name__, url_prefix="/trip")
photo_bp = Blueprint("photo", __name__, url_prefix="/photo")
journal_entry_bp = Blueprint("journal_entry", __name__, url_prefix="/journal_entry")



# @hello_world_bp.route("/hello_world", methods=["GET"])
# def say_hello_world():
#     my_response_body = "Hello, World!"
    
#     return my_response_body