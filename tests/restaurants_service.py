import unittest
from .mock_restaurants_repository import repo
from src.services import RestaurantsService

service = RestaurantsService(repo)

class TestRestaurantsService(unittest.TestCase):
    error_msg = 'Invalid value \'%d\' for argument \'%s\'. '
    error_msg += 'Values must be >= %d and <= %d.'

    def get_err_msg(self, val, arg, lower, higher):
        return TestRestaurantsService.error_msg % (val, arg, lower, higher)


    def test_distance_errors(self):
        values_to_test = [-1, 11]
        for d in values_to_test:
            with self.assertRaises(Exception) as e:
                service.best_match(distance=d)
            self.assertEqual(str(e.exception), self.get_err_msg(d, 'distance', 1, 10))


    def test_distance(self):
        results = service.best_match(distance=1)
        self.assertEqual(list(map(lambda x: x.id, results)), [1])


    def test_price_errors(self):
        values_to_test = [9, -1, 51]
        for v in values_to_test:
            with self.assertRaises(Exception) as e:
                service.best_match(price=v)
            self.assertEqual(str(e.exception), self.get_err_msg(v, 'price', 10, 50))


    def test_price(self):
        results = service.best_match(price=10)
        self.assertEqual(list(map(lambda x: x.id, results)), [1])

        results = service.best_match(price=20)
        self.assertEqual(list(map(lambda x: x.id, results)), [1, 2])

        results = service.best_match(price=30)
        self.assertEqual(list(map(lambda x: x.id, results)), [1, 2, 39])


    def test_customer_rating_errors(self):
        values_to_test = [0, 6]
        for v in values_to_test:
            with self.assertRaises(Exception) as e:
                service.best_match(customer_rating=v)
            self.assertEqual(str(e.exception), self.get_err_msg(v, 'customer_rating', 1, 5))


    def test_customer_rating(self):
        results = service.best_match(customer_rating=5)
        self.assertEqual(list(map(lambda x: x.id, results)), [39])
