from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://postgres:abdu200400@localhost/books" #db://user:password@host/database-name

engine = create_engine(DATABASE_URL)


Base = declarative_base()
session = sessionmaker()