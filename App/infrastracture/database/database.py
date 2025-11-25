from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .database_models import Base


db_url = "postgresql://postgress:123456789@localhost:5432/postgres"
engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)