from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import relationship, backref

from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Theaters(db.Model):
    __tablename__ = "theaters"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    address = db.Column('address', db.String)
    rating = db.Column('rating', db.Integer)
    description = db.Column('description', db.String)

    performances = db.relationship('Performances', secondary='schedule')

    def __repr__(self):
        return '<Theaters {}>'.format(self.id, self.name)

class Performances(db.Model):
    __tablename__ = "performances"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    duration = db.Column('duration', db.Time)
    main_actors = db.Column('main_actors', db.String)
    description = db.Column('description', db.String)
    reviews = db.Column('reviews', db.String)
    rating = db.Column('rating', db.Integer)

    theaters = db.relationship('Theaters', secondary='schedule')

    def __repr__(self):
        return '<Performances {}>'.format(self.name)

class Genres(db.Model):
    __tablename__="genres"
    id_performances = db.Column('id_performances', db.Integer,  db.ForeignKey('performances.id'), primary_key=True)
    genre = db.Column('genre', db.String)

    performances = db.relationship('Performances', foreign_keys=id_performances)

    def __repr__(self):
        return '<Genres {}>'.format(self.genre)

class Schedule(db.Model):
    __tablename__ = "schedule"
    __table_args__ = (
        PrimaryKeyConstraint('id_theaters', 'id_performances'),
    )
    id_theaters = db.Column('id_theaters', db.Integer,  db.ForeignKey('theaters.id'))
    id_performances = db.Column('id_performances', db.Integer, db.ForeignKey('performances.id'))
    date = db.Column('date', db.DATE, default=datetime.utcnow )
    time = db.Column('time', db.Time)
    price = db.Column('price', db.Numeric(10,2))
    free_places = db.Column('free_places', db.Integer)

    theaters = db.relationship('Theaters',  backref=backref("schedule", cascade="all, delete-orphan"))
    performances = db.relationship('Performances', backref=backref("schedule", cascade="all, delete-orphan"))
    def __repr__(self):
        return '<Schedule {}>'.format(self.id_theaters, self.id_performances, self.date, self.time, self.price, self.free_places)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()