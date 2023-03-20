from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)
# Base = declarative_base()


SQLALCHEMY_DATABASE_URL = "postgresql://ndlvgrnp:6PmHoKfOUWKOBw2omx9_BSGnDMyYVkH1@mahmud.db.elephantsql.com/ndlvgrnp"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)
Base = declarative_base()