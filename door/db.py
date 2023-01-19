from pony import orm
from .settings import HOST, PORT, DEBUG, SECRET_KEY

db = orm.Database()
db.bind(provider="sqlite", filename="door.sqlite", create_db=True)


class Member(db.Entity):
    """Member orm model."""

    name = orm.Required(str)
    email = orm.Required(str)
    password = orm.Required(str)
    is_admin = orm.Required(bool, default=False)
    is_active = orm.Required(bool, default=True)
