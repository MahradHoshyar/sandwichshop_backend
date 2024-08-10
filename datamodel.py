import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import *






engine = create_engine("postgresql+psycopg2://postgres:Mh8913hoshyar8913@localhost:5432/postgres", echo=True)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)


class Customer(Base):
    pass


class Product(Base):
    pass

class sell(Base):
    pass

class employee(Base):
    pass


class Session(Base):
    pass

