from ariadne import gql, make_executable_schema
from .query_resolvers import query

schema = make_executable_schema(gql("""
    type Cuisine {
        id: ID!
        name: String!
    }

    type Restaurant {
        id: ID!
        name: String!
        customer_rating: Int!
        distance: Int!
        price: Int!
        cuisine: Cuisine!
    }

    type Query {
        restaurants(
           name: String,
           customer_rating: Int,
           distance: Int,
           price: Int,
           cuisine_name: String
        ): [Restaurant]!
    }
"""), query)
