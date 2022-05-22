from marshmallow import fields

from app import ma, db
from app.models.product import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        sqla_session = db.session
        load_instance = True

    id = fields.Integer()
    name = fields.Str()
    price = fields.Decimal()
    amount = fields.Integer()

