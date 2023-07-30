from . import Base, Column, Integer, String


class Cuisine(Base):
    __tablename__ = 'cuisines'
    id = Column(Integer, primary_key=True)
    name = Column(String)
