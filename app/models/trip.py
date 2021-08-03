from flask import current_app
from app import db
# i didnt have following in tasklist but i did it videosotre.  do i need?
# from sqlalchemy import Table, Column, Integer, ForeignKey

class Trip(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trip_name = db.Column(db.String)
    country = db.Column(db.String, nullable=True, default=None)
    start_date = db.Column(db.Date, nullable=True, default=None)
    end_date = db.Column(db.Date, nullable=True, default=None)
    category = db.Column(db.String, nullable=True, default=None)
    description = db.Column(db.String, nullable=True, default=None)
    photos = db.relationship('Photo', backref='trip', lazy=True)  
    journal_entries = db.relationship('Journal_Entry', backref='trip', lazy=True)  
    # need to connect to user ...
    
    def api_response(self):
        return (
            {
                "id": self.trip_id,
                "name": self.trip_name,
                "country": self.country,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "category": self.category,
                "description": self.description,
                }
            ) 