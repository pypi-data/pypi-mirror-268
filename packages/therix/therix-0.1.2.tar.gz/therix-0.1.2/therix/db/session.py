# db/session.py

from sqlalchemy.orm import sessionmaker
from therix.db.db_manager import DatabaseManager

# Example PostgreSQL connection string
# Format: postgresql://user:password@hostname/database_name
db_manager = DatabaseManager()
SQLALCHEMY_DATABASE_URL = db_manager.SQLALCHEMY_DATABASE_URL

engine = DatabaseManager().engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
