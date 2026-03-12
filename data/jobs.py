from sqlalchemy import Column, INTEGER, String, DateTime, ForeignKey, Boolean
from sqlalchemy import orm
#from .db_session import SqlAlchemyBase

class Jobs(SqlAlchemyBase):
    __tablename__ = "jobs"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    team_leader = Column(INTEGER, ForeignKey("users.id"))
    user = orm.relationship("User")
    job = Column(String)
    work_size = Column(INTEGER)
    collaborators = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)