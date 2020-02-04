import os
from sqlalchemy import create_engine
from models import Person, Order, Base


def recreate_database(db_engine):
    Base.metadata.drop_all(db_engine)
    Base.metadata.create_all(db_engine)


basedir = os.path.abspath(os.path.dirname(__file__))
# connStr = 'mysql+mysqlconnector://root:4Belki8Sov@localhost:3306/doudb'
connStr = 'sqlite:///' + os.path.join(basedir, 'app.db')
engine = create_engine(connStr, echo=False)
recreate_database(engine)
