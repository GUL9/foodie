
import dataclasses

from data import database as db

@dataclasses.dataclass(frozen=True)
class Ingredient:
    id: int
    name: str

class DbIngredient(db.INSTANCE.Model):
    id = db.INSTANCE.Column(db.INSTANCE.Integer, primary_key=True)
    name = db.INSTANCE.Column(db.INSTANCE.String, unique=True, nullable=False)

    @classmethod
    def from_ingredient(ingredient: Ingredient) -> "DbIngredient":
        return DbIngredient(**dataclasses.asdict(ingredient))

    def to_ingredient(self) -> Ingredient:
        return Ingredient(id=self.id, name=self.name)


class IngredientApi:
    def insert_new(self, name: str) -> None:
        new_ingredient = DbIngredient(name=name)
        db.INSTANCE.session.add(new_ingredient)
        db.INSTANCE.session.commit()

    def get_by_name(self, name: str) -> Ingredient:
        db_ingredient = DbIngredient.query.filter_by(name=name).first()
        return db_ingredient.to_ingredient()