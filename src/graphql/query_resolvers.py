from ariadne import QueryType

query = QueryType()

@query.field('restaurants')
def resolve_restaurants(_, info, **params):
    restaurants_service = info.context['restaurants_service']

    try:
        return restaurants_service.best_match(**params)
    except Exception as e:
        raise e
