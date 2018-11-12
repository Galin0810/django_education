from app import db
from datetime import datetime

class Theaters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.String(128))
    performance = db.relationship('Performance', backref='theater', lazy='dynamic')

    def __repr__(self):
        return '<Theaters {}>'.format(self.name)

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), index=True, unique=True)
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    description = db.Column(db.String(256))
    main_actors = db.Column(db.String(128))
    theaters_id = db.Column(db.Integer, db.ForeignKey('theaters.id'))

    def __repr__(self):
        return '<Performance {}>'.format(self.name)