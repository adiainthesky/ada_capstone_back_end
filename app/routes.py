from flask import Blueprint

users_bp = Blueprint("users", __name__, url_prefix="/users")
trips_bp = Blueprint("trips", __name__, url_prefix="/trips")
photos_bp = Blueprint("photos", __name__, url_prefix="/photos")
journal_entries_bp = Blueprint("journal_entries", __name__, url_prefix="/journal_entries")



# @hello_world_bp.route("/hello_world", methods=["GET"])
# def say_hello_world():
#     my_response_body = "Hello, World!"
    
#     return my_response_body


@trips_bp.route("", methods=["POST"])
def post_trip():
    request_body = request.get_json()
    if "name" in request_body.keys():
        trip = Trip(trip_name=request_body["name"],
                    country=request_body["country"], 
                    start_date=request_body["start_date"],
                    end_date=request_body["end_date"],
                    category=request_body["category"],
                    description=request_body["description"],
                    )
        db.session.add(trip)
        db.session.commit()
        return jsonify({"trip": trip.api_response()}), 201
    else:
        return make_response(
            {"details": "Invalid data"
            }
        ), 400

@trips_bp.route("", methods=["GET"])
def get_trips():
    # can sort here if i want
    trips = Trip.query.all()
    trips_response = [trip.api_response() for trip in trips] 
    return jsonify(trips_response), 200        

@trips_bp.route("/<trip_id>", methods=["GET"])
def get_trip(trip_id):
    trip = Trip.query.get(trip_id)
    if trip is None:
        return make_response(jsonify(None), 404)
    return jsonify({"trip": trip.api_response()}), 200    

@trips_bp.route("/<trip_id>", methods=["PUT"])
def put_trip(trip_id):
    trip = Trip.query.get(trip_id)
    if trip is None:
        return Response(None),404
    form_data = request.get_json()
    trip.trip_name = form_data["name"]
    trip.country = form_data["description"]
    trip.start_date = form_data["start_date"]
    trip.end_date = form_data["end_date"]
    trip.category = form_data["category"]
    trip.description = form_data["description"]
    db.session.commit()
    return jsonify({"trip": trip.api_response()}), 200 

# do i need a patch??        

@trips_bp.route("/<trip_id>", methods=["DELETE"])
def delete_trip(trip_id):
    trip = Trip.query.get(trip_id)
    if trip is None:
        return Response(None),404
    db.session.delete(trip)
    db.session.commit()
    return make_response(
        {"details": f'Trip {trip.id} "{trip.title}" successfully deleted'
        }
    ), 200