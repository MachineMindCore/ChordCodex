from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Chord, Base  # Import the Chord model and Base from your model file
import os
from dotenv import load_dotenv

def get_engine(env_file: str=".env"):
    """
    Create and return a SQLAlchemy engine using the connection details from .env.
    """
    params = load_dotenv(env_file)

    HOST = params.get("DB_HOST")
    PORT = params.get("DB_PORT")
    USER = params.get("DB_USER")
    PASSWORD = params.get("DB_PASSWORD")
    NAME = params.get("DB_NAME")
    
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"
    return create_engine(DATABASE_URL, echo=True)

def init_db():
    """
    Initialize the database and create all tables.
    """
    engine = get_engine()  # Get the engine
    Base.metadata.create_all(engine)  # Create tables based on the Base metadata
    print("Database and table initialized!")
    return engine

# Main script to initialize the database
if __name__ == "__main__":
    try:
        init_db()
    except Exception as e:
        print(f"Error initializing the database: {e}")
