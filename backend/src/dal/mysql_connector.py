from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
import os

# Database configuration
DB_HOST = os.getenv("MYSQL_HOST", "localhost")
DB_USER = os.getenv("MYSQL_USER", "root")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
DB_NAME = os.getenv("MYSQL_DATABASE", "mydatabase")

# MySQL connection URL
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Create SQLModel engine
engine = create_engine(DATABASE_URL, echo=True)

def init_mysql_db():
    SQLModel.metadata.create_all(engine)

def get_mysql_session() -> Session:
    return Session(engine)
