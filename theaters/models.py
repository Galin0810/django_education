from app import db
from datetime import datetime

class Theater(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.String(128))
    performance = db.relationship('Performance', backref='theater', lazy='dynamic')

    def __repr__(self):
        return '<Theater {}>'.format(self.name)

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    description = db.Column(db.String(200))
    main_actors = db.Column(db.String(180))
    theater_id = db.Column(db.Integer, db.ForeignKey('theater.id'))

    def __repr__(self):
        return '<Performance {}>'.format(self.name)