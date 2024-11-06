
"""
Defines the Transaction model for the Personal Budget Tracker 
Classes:
    Transaction: A SQLAlchemy ORM model representing a financial transaction.
"""

from sqlalchemy import Column, Integer, String, Date, Numeric
from database import Base

class Transaction(Base):
    """
    This class defines the Transaction model for the Personal Budget Tracker 
    application.
    
    Attributes:
        __tablename__ (str): The name of the database table.
        id (int): The primary key for the table.
        date (str): The date of the transaction.
        description (str): The description of the transaction.
        category (str): The category of the transaction.
        amount (float): The amount of the transaction.
    """
    
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=True)
    amount = Column(Numeric(10, 2), nullable=False)
