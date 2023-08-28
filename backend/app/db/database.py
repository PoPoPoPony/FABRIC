import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine


DB_USER = os.getenv("POSTGRES_USER")
DB_PWD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")


# SQLALCHEMY_DATABASE_URL = "postgresql://" + DB_NAME + ":"+  DB_PWD +"@127.0.0.1:5432/postgres"
# SQLALCHEMY_DATABASE_URL = "postgresql://" + "postgres" + ":"+  "pony5487" +"@172.19.0.3:5432/postgres"
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db 
    finally:
        db.close()
