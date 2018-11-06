from app import db
class Theaters(db.Model):
    __tablename__ = "theaters"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    address = db.Column('address', db.String)
    rating = db.Column('rating', db.Integer)
    description = db.Column('description', db.String)

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

    def __repr__(self):
        return '<Performances {}>'.format(self.name)

