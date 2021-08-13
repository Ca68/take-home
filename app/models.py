from app import db
from datetime import datetime

class User(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    starttime= db.Column(db.DateTime)
    stoptime= db.Column(db.DateTime)
    bikeid= db.Column(db.Integer)
    from_station_id= db.Column(db.Integer)
    from_station_name= db.Column(db.String)
    to_station_id= db.Column(db.Integer)
    to_station_name= db.Column(db.String)
    usertype= db.Column(db.String)
    gender= db.Column(db.String)
    birthday= db.Column(db.DateTime)
    trip_duration= db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<User: {self.bikeid}>'

