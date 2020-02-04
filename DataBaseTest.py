import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Person, Order, Base


def recreate_database(db_engine):
    Base.metadata.drop_all(db_engine)
    Base.metadata.create_all(db_engine)


basedir = os.path.abspath(os.path.dirname(__file__))
# connStr = 'mysql+mysqlconnector://root:4Belki8Sov@localhost:3306/doudb'
connStr = 'sqlite:///' + os.path.join(basedir, 'app.db')
engine = create_engine(connStr, echo=False)
recreate_database(engine)
Session = sessionmaker(bind=engine)

session = Session()

person = Person()
person.name = 'Eugeny Bobylev'
person.email = 'ebobylev@gmail.com'
person.phone = '+79247401790'
person.is_customer = True
session.add(person)

order = Order()
order.customer = person
order.url_source='https//contoso.com'
session.add(order)

session.commit()
print(order.customer)

for ord in person.customer_orders:
    print(ord)

session.close()
