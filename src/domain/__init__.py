from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, declarative_base
Base = declarative_base()

from .restaurant import Restaurant
from .cuisine import Cuisine
