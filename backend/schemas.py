"""
This module defines the Pydantic models for the Personal Budget Tracker 
application.

Classes:
    TransactionBase: A base model for transaction data, including date, 
        description, category, and amount.
    TransactionCreate: A model for creating new transactions, inheriting 
        from TransactionBase.
    Transaction: A model for transaction data with an additional 
        id field, inheriting from TransactionBase.
        Config: A nested class to enable ORM mode for compatibility with 
            ORMs like SQLAlchemy.
"""
from datetime import date
from pydantic import BaseModel

class TransactionBase(BaseModel):
    """
    Pydantic model that represents the base schema for a financial 
    transaction.

    Attributes:
        date (date): The date of the transaction.
        description (str): A brief description of the transaction.
        category (str): The category under which the transaction falls 
            (e.g., groceries, utilities).
        amount (float): The monetary amount of the transaction.
    """
    date: date
    description: str
    category: str
    amount: float
        
class TransactionCreate(TransactionBase):
    """
    Schema for creating a new transaction.

    This class inherits from TransactionBase and does not add any 
    additional fields or methods. It is used to validate the data when 
    creating a new transaction.
    """
    pass

class Transaction(TransactionBase):
    """
    Schema class that inherits from TransactionBase.
    
    Attributes:
        id (int): Unique identifier for the transaction.
        Config (class): 
            orm_mode (bool): Enables compatibility with ORMs by allowing the 
                model to be populated from ORM objects.
    """
    id: int
    
    class Config:
        """
        Configuration class for Pydantic models.

        Attributes:
            orm_mode (bool): Enables compatibility with ORMs by allowing 
            the model to be populated from ORM objects.
        """
        orm_mode = True
