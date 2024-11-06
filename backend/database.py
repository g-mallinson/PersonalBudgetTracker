"""
Sets up the database connection and session for the Personal 
Budget Tracker application.

Modules:
    sqlalchemy: Provides SQL toolkit and Object-Relational Mapping (ORM).
    sqlalchemy.ext.declarative: Provides the base class for declarative 
        class definitions.
    sqlalchemy.orm: Provides sessionmaker for creating new Session 
        objects.
        
Constants:
    DATABASE_URL (str): The database URL for connecting to the 
        PostgreSQL database.
        
Variables:
    engine: The SQLAlchemy engine instance connected to the specified 
        database URL.
    SessionLocal: A configured sessionmaker instance for creating 
        database sessions.
    Base: The declarative base class for defining ORM models.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:3009@localhost/budget_db"

# Create the database engine, sessionmaker, and declarative base
# instances
#
# The engine instance is used to connect to the database.
# The sessionmaker instance is used to create new Session objects.
# The declarative base instance is used to define ORM models.
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
