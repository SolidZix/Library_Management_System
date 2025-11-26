from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .database_models import Base
from .config import db_url

engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)