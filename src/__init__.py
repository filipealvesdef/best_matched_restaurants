from ariadne import graphql_sync
from ariadne.explorer import ExplorerPlayground
from dependency_injector.wiring import Provide, inject
from flask import Flask, request, jsonify
from .graphql import schema
from .containers import Container
from dotenv import load_dotenv
import os


app = Flask(__name__)


@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return ExplorerPlayground().html(None), 200


@app.route('/graphql', methods=['POST'])
@inject
def graphql(restaurants_service = Provide[Container.restaurants_service],
            config = Provide[Container.config]):
    success, result = graphql_sync(
        schema,
        request.get_json(),
        context_value={
            'restaurants_service': restaurants_service,
        },
        debug=config['debug'],
    )
    return jsonify(result), 200 if success else 400


@app.teardown_request
@inject
def teardown_request(exception, db = Provide[Container.db_conn]):
    # Close the scoped_session instantiated when the request was created.
    db.session.remove()


# dependency injections
container = Container()

load_dotenv()
container.config.db_url.from_env('DB_URL')
container.config.debug.from_env('DEBUG', as_=bool, default=True)

container.wire(modules=[__name__])
