from sqlalchemy import Column, BigInteger, String, Numeric, CheckConstraint, Integer, DateTime
from sqlalchemy.sql.functions import current_timestamp

from app import db


class Product(db.Model):
    __tablename__ = 'Product'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(128),nullable=False)
    price = Column(Numeric(10,2), CheckConstraint('price >= 0.0'), nullable=False, server_default="0.0")
    amount = Column(Integer, CheckConstraint('Amount >= 0'),nullable=False, server_default="0")
    creation_date = Column(DateTime, server_default=current_timestamp())
    last_updated = Column(DateTime, server_default=current_timestamp(), onupdate=current_timestamp())

    def __init__(self, name: str = "", price: float = 0.0, amount: int = 0) -> None:
        self.name = name
        self.price = price
        self.amount = amount

    def create(self):
        db.session.add(self)
        db.session.commit()
        return  self

    def __repr__(self):
        return f'<Product: {self.name}'
