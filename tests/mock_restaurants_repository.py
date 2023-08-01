from src.db import SQLDB
from src.domain import Base, Restaurant, Cuisine
from src.repositories.restaurants import RestaurantsRepository

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


mock_data = [
    Restaurant(
        id = 1,
        name = 'Deliciousgenix',
        customer_rating = 4,
        distance = 1,
        price = 10,
        cuisine_id = 11,
    ),
    Restaurant(
        id = 2,
        name = 'Herbed Delicious',
        customer_rating = 4,
        distance = 7,
        price = 20,
        cuisine_id = 9,
    ),
    Restaurant(
        id = 3,
        name = 'Deliciousscape',
        customer_rating = 3,
        distance = 7,
        price = 50,
        cuisine_id = 1,
    ),
    Restaurant(
        id = 7,
        name = 'Hilltop Delicious',
        customer_rating = 3,
        distance = 3,
        price = 45,
        cuisine_id = 6,
    ),
    Restaurant(
        id = 39,
        name = 'Chowology',
        customer_rating = 5,
        distance = 9,
        price = 30,
        cuisine_id = 6,
    ),
    Cuisine(
        id = 1,
        name = 'American',
    ),
    Cuisine(
        id = 9,
        name = 'Vietnamese',
    ),
    Cuisine(
        id = 11,
        name = 'Spanish',
    ),
    Cuisine(
        id = 6,
        name = 'Japanese',
    ),
]

config = {
    'db_url': 'sqlite:///:memory:',
    'debug': False,
}

mock_db = SQLDB(config, Base.metadata, mock_data)
repo = RestaurantsRepository(mock_db)
