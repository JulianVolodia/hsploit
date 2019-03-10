from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Exploit(Base):
    __tablename__ = 'searcher_exploit'

    id = Column(Integer, primary_key=True)
    file = Column(String)
    description = Column(String)
    date = Column(String)
    author = Column(String)
    type = Column(String)
    platform = Column(String)
    port = Column(Integer)
