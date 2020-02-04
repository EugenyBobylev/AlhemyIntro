from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    name = Column("Name", String(128), nullable=False)
    email = Column("Email", String(128))
    phone = Column("Phone", String(64))
    is_customer = Column("IsCustomer", Boolean)
    is_performer = Column("IsPerformer", Boolean)

    customer_orders = relationship("Order", back_populates="customer")
    performer_orders = relationship("Order", back_populates="performer")


class Order(Base):
    __tablename__ = "order"

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    id_customer = Column("IdCustomer", Integer, ForeignKey("person.Id"))
    id_performer = Column("IdPerformer", Integer, ForeignKey("person.Id"))
    url_source = Column("UrlSource", String(255), nullable=False)
    url_result = Column("UrlResult", String(255))

    customer = relationship("Person", back_populates="customer_orders")
    performer = relationship("Person", back_populates="performer_orders")

