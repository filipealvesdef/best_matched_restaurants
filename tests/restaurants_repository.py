import unittest
from .mock_restaurants_repository import repo


class TestRestaurantsRepository(unittest.TestCase):
    def test_cuisine_name(self):
        results = repo.get_best_match(cuisine_name='jap')
        ids = list(map(lambda x: x.id, results))
        self.assertEqual(ids, [7, 39])

        results = repo.get_best_match(cuisine_name='sp')
        ids = list(map(lambda x: x.id, results))
        self.assertEqual(ids, [1])


    def test_distance(self):
        results = repo.get_best_match(distance=1)
        ids = list(map(lambda x: x.id, results))
        self.assertEqual(ids, [1])


    def test_name(self):
        results = repo.get_best_match(name='deli')
        ids = list(map(lambda x: x.id, results))
        self.assertEqual([1, 7, 2, 3], ids)


    def test_customer_rating(self):
        results = repo.get_best_match(customer_rating=5)
        ids = list(map(lambda x: x.id, results))
        self.assertEqual([39], ids)


    def test_price(self):
        results = repo.get_best_match(price=10)
        ids = list(map(lambda x: x.id, results))
        self.assertEqual([1], ids)

        results = repo.get_best_match(price=20)
        ids = list(map(lambda x: x.id, results))
        self.assertEqual([1, 2], ids)

        results = repo.get_best_match(price=30)
        ids = list(map(lambda x: x.id, results))
        self.assertEqual([1, 2, 39], ids)


    def test_invalid_parameter(self):
        results = repo.get_best_match(invalid='foo')
        ids = list(map(lambda x: x.id, results))
        self.assertEqual([1, 7, 2, 3, 39], ids)


    def test_all(self):
        results = repo.get_best_match()
        ids = list(map(lambda x: x.id, results))
        self.assertEqual([1, 7, 2, 3, 39], ids)
