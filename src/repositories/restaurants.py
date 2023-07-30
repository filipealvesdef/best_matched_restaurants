from ..domain import Restaurant, Cuisine
from sqlalchemy import desc


class RestaurantsRepository:
    def __init__(self, db):
        self.session = db.session


    def get_best_match(self, **params):
        try:
            query = self.session.query(Restaurant)

            if 'cuisine_name' in params:
                cuisine_name = params['cuisine_name']
                query = query.join(Cuisine)
                query = query.filter(Cuisine.name.like(f'%{cuisine_name}%'))

            if 'name' in params:
                name = params['name']
                query = query.filter(Restaurant.name.like(f'%{name}%'))

            if 'distance' in params:
                distance = params['distance']
                query = query.filter(Restaurant.distance <= distance)

            if 'customer_rating' in params:
                customer_rating = params['customer_rating']
                query = query.filter(Restaurant.customer_rating >= customer_rating)

            if 'price' in params:
                price = params['price']
                query = query.filter(Restaurant.price <= price)

            query = query.order_by(
                Restaurant.distance,
                desc(Restaurant.customer_rating),
                Restaurant.price,
            )

            return query.limit(5).all()
        except Exception as e:
            raise Exception(f'An error has occurred during the query: {str(e)}')
