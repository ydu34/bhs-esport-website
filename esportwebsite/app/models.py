from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), index=True, unique=True)
    lastName = db.Column(db.String(64), index=True, unique=True)
    username = db.Column(db.String(120), index=True, unique=True)
    teamName = db.Column(db.String(64), index=True, unique=True)
    cellphoneNumber = db.Column(db.Integer, index=True, unique=True)


    def __repr__(self):
        return '<User %r    >' % (self.nickname)