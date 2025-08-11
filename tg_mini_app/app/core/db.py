from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
import os

DB_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost/robotics_club")

engine = create_engine(DB_URL)

# Создание базы, если не существует
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
