"""
Configures the database connection, and provides a session object to 
interact with the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:3009@localhost/budget_db"
