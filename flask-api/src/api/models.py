from .. import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, nullable=False)

    def to_json(self):
        json_user = {"id": self.id, "email": self.email, "username": self.username}
        return json_user

    def __repr__(self):
        return "<User %r>" % self.username
