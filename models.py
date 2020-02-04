from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    name = Column("Name", String(128), nullable=False)
    email = Column("Email", String(128))
    phone = Column("Phone", String(64))
    is_customer = Column("IsCustomer", Boolean)
    is_performer = Column("IsPerformer", Boolean)

    customer_orders = relationship("Order", lazy='dynamic', back_populates="customer")
    performer_orders = relationship("Order", lazy='dynamic', back_populates="performer")

    def __repr__(self):
        return f'id={self.id}; name={self.name}; email={self.email}; phone={self.phone}'


class Order(Base):
    __tablename__ = "orders"

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    id_customer = Column("IdCustomer", Integer, ForeignKey("persons.Id"))
    id_performer = Column("IdPerformer", Integer, ForeignKey("persons.Id"))
    url_source = Column("UrlSource", String(255), nullable=False)
    url_result = Column("UrlResult", String(255))

    customer = relationship("Person", back_populates="customer_orders")
    performer = relationship("Person", back_populates="performer_orders")

    def __repr__(self):
        return f'id={self.id}; customer={self.customer}; performer={self.performer}' \
               f'url_spurce={self.url_source}; url_result={self.url_result}'
