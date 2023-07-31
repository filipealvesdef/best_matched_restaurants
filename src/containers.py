from dependency_injector import containers, providers
from .repositories import RestaurantsRepository
from .services import RestaurantsService
from .db import SQLDB
from .data_loader import load_data_from_csv
from .domain import Base


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_conn = providers.Singleton(
        SQLDB,
        config,
        Base.metadata,
        load_data_from_csv(),
    )

    restaurants_repository = providers.Factory(
        RestaurantsRepository,
        db=db_conn,
    )

    restaurants_service = providers.Factory(
        RestaurantsService,
        restaurants_repository=restaurants_repository,
    )
