from . import db, ma
# TODO: Figure out how to split each model into a seperate file


class User(db.Model):
    """Model for user accounts."""

    __tablename__ = 'user'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                     index=False,
                     unique=False,
                     nullable=False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    phone = db.Column(db.String(100),
                      index=False,
                      unique=False,
                      nullable=True)
    note = db.relationship("Note",
                           back_populates="user")

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Note(db.Model):
    """Model for user accounts."""

    __tablename__ = 'note'
    id = db.Column(db.Integer,
                   primary_key=True)
    content = db.Column(db.Text,
                        index=False,
                        unique=False,
                        nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id'),
                        nullable=False)
    user = db.relationship("User", back_populates="note")
