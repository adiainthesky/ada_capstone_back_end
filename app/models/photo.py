from flask import current_app
from main import db
from  app.models.trip import Trip
from sqlalchemy import Table, Column, Integer, ForeignKey

class Photo(db.Model):
    photo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url_link = db.Column(db.String)
    # tasklisk had the following as nullable but i dont think i want it nullable
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id')) 
    ###### how do i get user name/id in here????
    ###### how do i get journal_entries in here????

    def api_response(self):
        return (
            {
                "id": self.photo_id,
                "img": self.url_link,
                "trip_id": self.trip_id,
                }
            ) 