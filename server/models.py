from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Plant(db.Model, SerializerMixin):
    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    price = db.Column(db.Integer)
    is_in_stock = db.Column(db.Boolean, default=True)

    # include all fields when serializing
    serialize_only = ("id", "name", "image", "price", "is_in_stock")

    def __repr__(self):
        return f"<Plant {self.id}: {self.name}>"


