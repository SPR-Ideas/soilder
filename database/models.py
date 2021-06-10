from .database import Base
from sqlalchemy import Column , Integer, String, Float

#create databasetabel by inheriting Base class

class soldier(Base):
    __tablename__ = "soldiers"
    soldier_id = Column(String,unique=True)
    name = Column(String)
    id = Column(Integer,primary_key=True)
    BPM = Column(Integer)
    temp = Column(Float)
