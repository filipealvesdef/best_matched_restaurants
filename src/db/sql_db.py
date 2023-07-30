from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class SQLDB:
    def __init__(self, config, metadata, data):
        try:
            debug = config['debug']
            db_url = config['db_url']
            self.engine = create_engine(db_url, echo=debug)
            self.session = scoped_session(sessionmaker(bind=self.engine))
            metadata.create_all(self.engine)
            self.load_data(data)
        except Exception as e:
            print(f'Error initilizing db: {e}')


    def load_data(self, data):
        try:
            self.session.add_all(data)
            self.session.commit()
        except Exception as e:
            print(f'error loading data: {e}')
            self.session.rollback()
        finally:
            self.session.remove()
