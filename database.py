from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from sqlalchemy import Table, MetaData
from sqlalchemy import insert, delete

SQL_URL = 'mysql+pymysql://회원db'

engine = create_engine(SQL_URL)

metadata_obj = MetaData(bind=engine)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
db = SessionLocal()
Base = declarative_base()




