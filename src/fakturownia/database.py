from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode(128))
    nip = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(Company, self).__init__(*args, **kwargs)


class Buyer(Company):
    __tablename__ = 'buyer'
    id = db.Column(db.Integer, db.ForeignKey('company.id'), primary_key=True)


class Seller(Company):
    __tablename__ = 'seller'
    id = db.Column(db.Integer, db.ForeignKey('company.id'), primary_key=True)


class Invoice(db.Model):
    __tablename__ = 'inovice'
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))
    value = db.Column(db.Numeric(38,4))
    buyer = relationship('Buyer', foreign_keys='Invoice.buyer_id')
    seller = relationship('Seller', foreign_keys='Invoice.seller_id')