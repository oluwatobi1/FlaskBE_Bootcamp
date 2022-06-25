from db import db


class UserModel(db.Model):
    __tablename__ = "user_wk4"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    # never save raw password values always encrypt them before storing
    password = db.Column(db.String())

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    @classmethod
    def find_by_name(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def create(cls, user):
        db.session.add(user)
        db.session.commit()

    @classmethod
    def delete(cls):
        db.session.delete(cls)
        db.session.commit()


