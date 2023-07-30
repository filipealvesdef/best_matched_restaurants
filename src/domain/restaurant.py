from . import Base, Column, Integer, ForeignKey, String, relationship


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    distance = Column(Integer)
    customer_rating = Column(Integer)
    cuisine_id = Column(Integer, ForeignKey('cuisines.id'))

    cuisine = relationship('Cuisine', backref='restaurants')
