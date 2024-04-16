from sqlalchemy import create_engine, Engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from alembic.config import Config
from alembic import command
import logging
import os

from therix.db.base import Base


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseManager:
    """
    Database manager / connection handler and session manager
    """

    _instance = None
    engine: Engine
    session: sessionmaker
    SQLALCHEMY_DATABASE_URL: str

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Initializes the database by creating all defined tables
        and running any pending migrations.
        """
        db_type = os.getenv("THERIX_DB_TYPE", "postgresql")
        username = os.getenv("THERIX_DB_USERNAME")
        password = os.getenv("THERIX_DB_PASSWORD")
        host = os.getenv("THERIX_DB_HOST")
        port = os.getenv("THERIX_DB_PORT")
        db_name = os.getenv("THERIX_DB_NAME")
        try:
            if not hasattr(self, "engine"):
                if all(
                    param is not None
                    for param in [db_type, username, password, host, port, db_name]
                ):

                    self.SQLALCHEMY_DATABASE_URL = (
                        f"{db_type}://{username}:{password}@{host}:{port}/{db_name}"
                    )
                    self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
                    self.session = sessionmaker(bind=self.engine)
                    self.session().execute(text("SELECT 1"))

                    Base.metadata.create_all(self.engine)
                    logger.info("All tables created successfully.")
                    # Run Alembic migrations
                    alembic_cfg = Config("alembic.ini")
                    alembic_cfg.set_main_option(
                        "sqlalchemy.url", self.SQLALCHEMY_DATABASE_URL
                    )
                    command.upgrade(alembic_cfg, "head")
                    logger.info("All migrations executed successfully.")
                    logger.info(
                        "Database engine and session factory created successfully."
                    )
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while initializing the database: {e}")
            raise

    def create_session(self):
        return self.session()


db_manager = DatabaseManager()
# Example usage:
# db_manager = DatabaseManager(
#     "postgresql", "postgres", "password", "localhost", "5432", "coditas_dot_ai"
# )
# db_manager1 = DatabaseManager()
# session = db_manager.create_session()
# # Use the session for ORM operations
# db_manager.test_connection()
# session.close()
