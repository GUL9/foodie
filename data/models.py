
from data import database as db


class User(db.INSTANCE.Model):
    id = db.INSTANCE.Column(db.INSTANCE.Integer, primary_key=True)
    username = db.INSTANCE.Column(db.INSTANCE.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    