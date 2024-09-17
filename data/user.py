
import dataclasses

from data import database as db

@dataclasses.dataclass(frozen=True)
class User:
    id: int
    username: str


class DbUser(db.INSTANCE.Model):
    id = db.INSTANCE.Column(db.INSTANCE.Integer, primary_key=True)
    username = db.INSTANCE.Column(db.INSTANCE.String, unique=True, nullable=False)

    @classmethod
    def from_user(user: User) -> "DbUser":
        return DbUser(**dataclasses.asdict(user))

    def to_user(self) -> User:
        return User(id=self.id, username=self.username)


class UserApi():

    def insert_new(self, username: str) -> None:
        db_user = DbUser(username=username)
        db.INSTANCE.session.add(db_user)
        db.INSTANCE.session.commit()

    def get_by_username(self, username: str) -> User:
        db_user = DbUser.query.filter_by(username=username).first()
        return db_user.to_user()


        
    