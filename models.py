from typing import Dict

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import json


Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    name = Column("Name", String(128), nullable=False)
    email = Column("Email", String(128))
    phone = Column("Phone", String(64))
    is_customer = Column("IsCustomer", Boolean, default=False)
    is_performer = Column("IsPerformer", Boolean, default=False)

    customer_orders = relationship("Order", foreign_keys='Order.id_customer', back_populates="customer", lazy=False)
    performer_orders = relationship("Order", foreign_keys='Order.id_performer', back_populates="performer", lazy=False)

    def __repr__(self):
        return f'id={self.id}; name={self.name}; email={self.email}; phone={self.phone}'

    def from_json(json_str) -> 'Person':
        def parse(key: str):
            if key in from_json:
                return from_json[key]
            else:
                return None

        from_json = json.loads(json_str)
        person = Person()
        person.id = parse('id')
        person.name = parse('name')
        person.email = parse('email')
        person.phone = parse('phone')
        person.is_customer = parse('is_customer')
        person.is_performer = parse('is_performer')
        return person


class Order(Base):
    __tablename__ = "orders"

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    id_customer = Column("IdCustomer", Integer, ForeignKey("persons.Id"))
    id_performer = Column("IdPerformer", Integer, ForeignKey("persons.Id"))
    url_source = Column("UrlSource", String(255), nullable=False)
    url_result = Column("UrlResult", String(255))

    customer = relationship("Person", foreign_keys=[id_customer])
    performer = relationship("Person", foreign_keys=[id_performer])

    def __repr__(self):
        return f'id={self.id}; customer={self.customer}; performer={self.performer}' \
               f'url_spurce={self.url_source}; url_result={self.url_result}'

