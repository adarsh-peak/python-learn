# database.py
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydb"

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Async database connection using databases library
database = Database(DATABASE_URL)

# Base class for ORM models
Base = declarative_base()
