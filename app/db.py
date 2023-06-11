import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    db_url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    print(db_url)
except KeyError:
    print("DEBUG: Failed to getenv")
    db_url = "postgresql://postgres:postgres@flask_db:5432/postgres"

db = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')
Base = declarative_base()
SessionLocal = sessionmaker(bind=db, expire_on_commit=False)
