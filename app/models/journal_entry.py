from flask import current_app
from app import db
from  app.models.trip import Trip

class Journal_Entry(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entry = db.Column(db.String)
    # tasklisk had the following as nullable but i dont think i want it nullable
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id')) 
    ###### how do i get user name/id in here????
    ###### how do i get photos in here????

    def api_response(self):
        return (
            {
                "id": self.entry_id,
                "entry": self.entry,
                "trip_id": self.trip_id,
                }
            ) 