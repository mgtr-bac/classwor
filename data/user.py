from sqlalchemy import Column, INTEGER, String, DateTime, orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String)
    age = Column(INTEGER)
    position = Column(String)
    address = Column(String)
    email = Column(String, unique=True)
    hashed_password =  Column(String)
    modified_date = Column(DateTime)

    jobs = orm.relationship("Jobs", back_populates="user")