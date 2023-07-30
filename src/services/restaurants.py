from ..domain import Restaurant


class RestaurantsService:
    def __init__(self, restaurants_repository):
        self.repository = restaurants_repository


    def best_match(self, **params):
        constraints = {
            'distance': (1, 10),
            'price': (10, 50),
            'customer_rating': (1, 5),
        }

        try:
            for k, v in params.items():
                if k in constraints:
                    lower, higher = constraints[k]
                    if v < lower or v > higher:
                        error_msg = f'Invalid value \'{v}\' for argument \'{k}\'. '
                        error_msg += f'Values must be >= {lower} and <= {higher}.'
                        raise Exception(error_msg)
            return self.repository.get_best_match(**params)
        except Exception as e:
            raise e


