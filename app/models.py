from app import db


class Ride(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, index=True)
    end_time = db.Column(db.DateTime)
    bike_id = db.Column(db.Integer)
    trip_duration = db.Column(db.Float)
    from_station_id = db.Column(db.Integer, db.ForeignKey('station.id'))
    to_station_id = db.Column(db.Integer, db.ForeignKey('station.id'))
    user_type = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    birth_year = db.Column(db.Integer)

    def __repr__(self):
        return '<ride_id: {}>'.format(self.trip_id)

    def edge(self):
        return {
            "from_station_id": self.from_station_id,
            "to_station_id": self.to_station_id
        }


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String(150))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    departures = db.relationship('Ride', foreign_keys='Ride.from_station_id', lazy='dynamic')
    arrivals = db.relationship('Ride', foreign_keys='Ride.to_station_id', lazy='dynamic')

    def __repr__(self):
        return '<station_name: {}>'.format(self.station_name)
