
from data import database as db



class User(db.INSTANCE.Model):
    id = db.INSTANCE.Column(db.INSTANCE.Integer, primary_key=True)
    username = db.INSTANCE.Column(db.INSTANCE.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class UserApi():
    def create_new(self, username: str) -> User:
        new_user = User(username=username)
        db.INSTANCE.session.add(new_user)
        db.INSTANCE.session.commit()

        return new_user
        

    def get_by_username(self, username: str) -> User:
        return User.query.filter_by(username=username).first()

        
    