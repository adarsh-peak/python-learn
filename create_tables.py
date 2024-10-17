from database import engine
from models import Base

# This will create all tables in the database based on the models
Base.metadata.create_all(bind=engine)