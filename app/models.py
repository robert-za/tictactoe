from sqlalchemy import Column, Integer, String
from db import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    won = Column(Integer)
    lost = Column(Integer)
    draws = Column(Integer)
    credits = Column(Integer)