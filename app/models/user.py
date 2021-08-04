from flask import current_app
from main import db
# i didnt have following in tasklist but i did it videosotre.  do i need?
from sqlalchemy import Table, Column, Integer, ForeignKey


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    trips = db.relationship('Trip', backref='user', lazy=True)  
    
    def api_response(self):
        return (
            {
                "user_id": self.user_id,
                "name": self.user_name,
                }
            ) 