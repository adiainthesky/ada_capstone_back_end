from flask import Blueprint
from main import db
from app.models.user import User
from app.models.trip import Trip
from app.models.photo import Photo
from flask import request, Blueprint, jsonify, Response, make_response
import requests
import os
from dotenv import load_dotenv

users_bp = Blueprint("users", __name__, url_prefix="/users")
trips_bp = Blueprint("trips", __name__, url_prefix="/trips")
photos_bp = Blueprint("photos", __name__, url_prefix="/photos")
# journal_entries_bp = Blueprint("journal_entries", __name__, url_prefix="/journal_entries")

@trips_bp.route("", methods=["POST"])
def post_trip():
    request_body = request.get_json()
    if not request_body:
        return make_response(
            # apparently it didnt like dict format here (but i could do it in dict for if i used .jsonify): {"details": "expected request body to be in JSON"}
            "expected request body to be in JSON"
        ), 400
    elif not "name" in request_body.keys():
        return make_response("expected 'name' to exist in the request body"), 400
    else:
        trip = Trip(trip_name=request_body["name"],
                    country=request_body["country"], 
                    start_date=request_body.get("start_date",None),
                    end_date=request_body.get("end_date",None),
                    category=request_body["category"],
                    description=request_body["description"],
                    )
        db.session.add(trip)
        db.session.commit()
    return jsonify({"trip": trip.api_response()}), 201

@trips_bp.route("", methods=["GET"])
def get_trips():
    # can sort here if i want
    trips = Trip.query.all()
    trips_response = [trip.api_response() for trip in trips] 
    return jsonify(trips_response), 200        

@trips_bp.route("/<trip_id>", methods=["GET"])
def get_trip(trip_id):
    trip = Trip.query.get_or_404(trip_id, description=f'ID #{trip_id} not found')
    return jsonify({"trip": trip.api_response()}), 200    



# NEEDS WORD! even with .get_or_404, the 
@trips_bp.route("/<trip_id>", methods=["PUT"])
def put_trip(trip_id):
    trip = Trip.query.get_or_404(trip_id, description=f'ID #{trip_id} not found')
    request_body = request.get_json()
    if not request_body:
        return make_response("expected request body to be in JSON"), 400
    trip.trip_name = request_body.get("name",None)
    trip.country = request_body.get("country",None)
    trip.start_date = request_body.get("start_date",None)
    trip.end_date = request_body.get("end_date",None)
    trip.category = request_body.get("category",None)
    trip.description = request_body.get("description",None)
    db.session.commit()
    return jsonify({"trip": trip.api_response()}), 200 

@trips_bp.route("/<trip_id>", methods=["DELETE"])
def delete_trip(trip_id):
    trip = Trip.query.get_or_404(trip_id, description=f'ID #{trip_id} not found')
    db.session.delete(trip)
    db.session.commit()
    return make_response(f'"{trip.trip_name}" successfully deleted'), 200






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
    request_body = request.get_json()
    photo.url_link = request_body["img"]
    photo.description = request_body["description"]
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