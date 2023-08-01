# Best Matched Restaurants (Backend) - GraphQL API

## Introduction
This project features the web application server of a search system that filters and ranks the best matched restaurants based on its name, distance, price, customer ratings or cuisine type.

The code of this application was written in **python**; it features a **relational database** to store and query data in **.csv** files; **ORM** to abstract database methods and facilitate data-model mapping; exposes a **GraphQL API** which can be accessed through a **web application playground**. 

## Search
The search results are composed by the **top 5** restaurants, filtered by search parameters and ranked according to their attributes to determine the best matches, as described bellow.

### Filter
Fist the results are filtered by the **union (and relationship)** of **optional** filter parameters:

- **Restaurant Name:** The name of the filtered restaurants should match either completely or partially with the search parameter.

- **Cuisine Type:** The cuisine type (Japanese, American, Italian, etc.) should match either completely or partially with the search parameter.

- **Distance:** The distance of the filtered restaurants will be **less than or equal** to the specified search parameter. Its values are integers and should be *1 <= distance <= 10*.

- **Customer Ratings:** The customer ratings of the filtered restaurants will be **greater than or equal** to the specified search parameter. Its values are integers and should be *1 <= customer rating <= 5*.

- **Price:** The price of the filtered restaurants will be **less than or equal** to the specified search parameter. Its values are integers and should be *10 <= price <= 50*.

### Rank
After filtering, the **top 5** restaurants are ranked. To avoid ties, three restaurant attributes are evaluated in order of priority. In case of a tie in any of these attributes, the next attribute in the priority list is considered for ranking:
1. Distance (ascending order)
2. Customer ratings (descending order)
3. Price (ascending order)

## Usage
To use the restaurant search API, you need to have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.

1. Clone this repository to your local machine.

2. The `.env` file containing the required environment variables has been created and committed in this repository just for convenience. You can adjust the values of `DB_URL` and `DEBUG` as per your requirements.
   ```
   DB_URL=sqlite:///tmp/restaurants.db
   DEBUG=true
   ```

3. Build and start the services using the following command:
   ```
   docker-compose up
   ```

4. The GraphQL server will be up and running at `http://localhost:3000/graphql`.


## Interacting with the API
You can interact with the API through the provided web playground or by using an HTTP client like cURL or Insomnia.

The GraphQL API features a single query resolver called `restaurants`. This query accepts the following **optional** parameters: `name` (string), `distance` (int), `customer_rating` (int), `price` (int), and `cuisine_name` (string).

### Using Web Playground
To interact with the API via the provided web playground, open a web browser and navigate to `http://localhost:3000/graphql`. The playground allows you to send GraphQL queries directly from the browser.

Sample GraphQL Query:
```graphql
{
  restaurants(cuisine_name: "jap", price: 35, distance: 4) {
    id
    name
    distance
    customer_rating
    price
    cuisine {
      id
      name
    }
  }
}
```

Sample Result:
```json
{
  "data": {
    "restaurants": [
      {
        "id": "176",
        "name": "Kitchenish",
        "distance": 2,
        "customer_rating": 3,
        "price": 20,
        "cuisine": {
          "id": "6",
          "name": "Japanese"
        }
      },
      {
        "id": "190",
        "name": "Safety Kitchen",
        "distance": 4,
        "customer_rating": 2,
        "price": 20,
        "cuisine": {
          "id": "6",
          "name": "Japanese"
        }
      },
      {
        "id": "98",
        "name": "Festive Grill",
        "distance": 4,
        "customer_rating": 2,
        "price": 35,
        "cuisine": {
          "id": "6",
          "name": "Japanese"
        }
      }
    ]
  }
}
```

The response will contain a list of restaurants that match the search criteria, sorted as described in the [Rank](#rank) section. Notice how the results were sorted in this example: "Kitchenish" is the top-1 result because it has the lower `distance` among the results. "Safety Kitchen" and "Festive Grill" tie in `distance` and `customer_rating` as well, but "Safety Kitchen" wins, since it has a lower price than "Festive Grill".

## Running Python Tests
The project has **13 test cases** to validate best match results and error handling. 

### Prerequisites
- Python 3.x installed on your system.

### Steps to Run Tests
1. **Create a Virtual Environment**:

   It is recommended to use a virtual environment to isolate the test environment from the system-wide Python packages. Open your terminal or command prompt and run the following command to create a virtual environment named `venv`:

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   Activate the virtual environment to use the Python interpreter and packages installed within it. The activation command varies depending on your operating system:

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

   On macOS and Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   Install these dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Tests**:
   In project root, run:

   ```bash
   python -m unittest tests
   ```

   The test runner will automatically and execute all test cases in the `tests/` directory. The output should be:

   ```
   .............
   ----------------------------------------------------------------------
   Ran 13 tests in 0.009s

   OK
   ```

## Technical details
### Architecture
The web application architecture follows a layered design to maintain a clear separation of concerns and promote code modularity. Each layer has its specific responsibilities, ensuring that the application's business logic, data access, and presentation are decoupled and can be developed, tested, and maintained independently.

- **Presentation:** This layer is responsible for handling HTTP requests and responses. It serves as the web framework for the application, receiving incoming HTTP requests from clients, routing them to the appropriate GraphQL operations, and sending back HTTP responses with data obtained from the GraphQL layer.

- **GraphQL:** The GraphQL layer serves as the interface between the front-end and the back-end. It handles incoming GraphQL queries and mutations from clients, defines the available data types and operations through a schema, and delegates requests to the appropriate service layer functions for processing.

- **Service:** The service layer contains the application's business logic and acts as an intermediary between the repository and the GraphQL layer. It encapsulates complex operations, coordinates data retrieval from the repository, and performs the necessary transformations before sending data to the GraphQL layer.

- **Repostory:** The repository layer is responsible for handling data persistence and retrieval. It abstracts the underlying database or data storage mechanism, allowing the rest of the application to interact with data without being concerned about the data source.

- **Domain:** The domain layer represents the core business entities and business rules of the application. It defines the structure and behavior of objects that are fundamental to the application's domain, ensuring consistency and encapsulation of business logic.

- **DB:** The database layer manages the actual storage and retrieval of data. It interacts directly with the underlying database system, executing queries and managing data transactions as required by the repository layer.

### Technologies and libraries used
- **[SQLAlchemy](https://www.sqlalchemy.org/):** SQLAlchemy is used as the Object-Relational Mapping (ORM) library to interact with the database. It provides an intuitive and flexible way to work with relational databases, and by default, this project uses a SQLite database.

- **[Flask](https://flask.palletsprojects.com/):** Flask is a lightweight and flexible web framework for Python. It is used to build the RESTful endpoints that handle GraphQL queries and provide a seamless experience for the frontend and client applications.

- **[python-dependency-injector](https://github.com/ets-labs/python-dependency-injector):** This library is used for dependency injection, making it easier to manage and inject dependencies into the application's components, promoting a more modular and testable codebase.

- **[Ariadne](https://ariadnegraphql.org/):** Ariadne is a Python library for implementing GraphQL servers. It helps build the GraphQL schema and resolvers, allowing smooth integration with Flask and the query execution.

- **[python-dotenv](https://github.com/theskumar/python-dotenv):** Python-Dotenv is used to load environment variables from the `.env` file. It enables easy configuration management for the application, allowing you to set environment-specific variables.

- **Apache HTTP Server with mod_wsgi:** The Docker container is built with an Apache HTTP Server and mod_wsgi to deploy the Flask application. mod_wsgi enables hosting Python applications with Apache, providing a robust and production-ready deployment solution.

## Contributing
If you would like to contribute to this project, please feel free to create a pull request. For any questions or support, you can contact me at filipealvesdefernando@gmail.com.
