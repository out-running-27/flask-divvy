from app import db


class Rides(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, index=True)
    end_time = db.Column(db.DateTime)
    bike_id = db.Column(db.Integer)
    trip_duration = db.Column(db.Float)
    from_station_id = db.Column(db.Integer)
    to_station_id = db.Column(db.Integer)
    user_type = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    birth_year = db.Column(db.Integer)

    def __repr__(self):
        return '<ride_id: {}'.format(self.id)


class Station(db.Model):
    id =
