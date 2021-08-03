from flask import Blueprint

users_bp = Blueprint("users", __name__, url_prefix="/users")
trips_bp = Blueprint("trips", __name__, url_prefix="/trips")
photos_bp = Blueprint("photos", __name__, url_prefix="/photos")
# journal_entries_bp = Blueprint("journal_entries", __name__, url_prefix="/journal_entries")



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

    # customer = Customer.query.get(customer_id)
    # if customer is None:
    #     return "Customer not found.", 404
    # can turn those three lines into: customer = Customer.query.get_or_404(customer_id, description="Customer Id not found")

@trips_bp.route("/<trip_id>", methods=["PUT"])
def put_trip(trip_id):
    trip = Trip.query.get(trip_id)
    if trip is None:
        return Response(None),404
        # add more a message above as to why, ie: return {message:"trip was not found"}, 404
    form_data = request.get_json()
    trip.trip_name = form_data["name"]
    trip.country = form_data["country"]
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

@photos_bp.route("", methods=["POST"])
def post_photo():
    request_body = request.get_json()
    if "img" in request_body.keys():
        photo = Photo(url_link=request_body["img"],
                    )
        db.session.add(photo)
        db.session.commit()
        return jsonify({"photo": photo.api_response()}), 201
    else:
        return make_response(
            {"details": "Invalid data"
            }
        ), 400

@photos_bp.route("", methods=["GET"])
def get_photos():
    # can sort here if i want
    photos = Photo.query.all()
    photos_response = [photo.api_response() for photo in photos] 
    return jsonify(photos_response), 200        

@photos_bp.route("/<photo_id>", methods=["GET"])
def get_photo(photo_id):
    photo = Photo.query.get(photo_id)
    if photo is None:
        return make_response(jsonify(None), 404)
    return jsonify({"photo": photo.api_response()}), 200    

@photos_bp.route("/<photo_id>", methods=["PUT"])
def put_photo(photo_id):
    photo = photo.query.get(photo_id)
    if photo is None:
        return Response(None),404
    form_data = request.get_json()
    photo.url_link = form_data["img"]
    photo.description = form_data["description"]
    db.session.commit()
    return jsonify({"photo": photo.api_response()}), 200 

# do i need a patch??        

@photos_bp.route("/<photo_id>", methods=["DELETE"])
def delete_photo(photo_id):
    photo = Photo.query.get(photo_id)
    if photo is None:
        return Response(None),404
    db.session.delete(photo)
    db.session.commit()
    return make_response(
        {"details": f'photo {photo.id} "{photo.title}" successfully deleted'
        }
    ), 200    