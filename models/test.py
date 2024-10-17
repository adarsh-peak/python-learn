from sqlalchemy import Column, Integer, String
from database import Base

class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
