from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models
import schemas
import database

# Initialize database schema
models.Base.metadata.create_all(bind=database.engine)

# Create FastAPI app
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Adjust to match the frontend URL
    allow_credentials=True,  # Required for cookies
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    """
    Dependency that provides a database session to be used in FastAPI 
    routes. Creates a new database session using the SessionLocal class 
    from the database module. It yields the session to the caller and 
    ensures that the session is properly closed after use.
    
    Yields:
        db (Session): A SQLAlchemy database session.
    """
    db = database.SessionLocal()
    try:
        yield db  # Provide the database session to the route
    finally:
        db.close()

@app.get("/transactions/", response_model=list[schemas.Transaction])
def read_transactions(skip: int = 0, limit: int = 100,
                        db: Session = Depends(get_db)):
    """
    Route to retrieve a list of transactions from the database.
    
    Args:
        skip (int): The number of transactions to skip.
        limit (int): The maximum number of transactions to retrieve.
        db (Session): The database session dependency.
        
    Returns:
        list[schemas.Transaction]: A list of Transaction objects.
    """
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions

@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate,
                        db: Session = Depends(get_db)):
    """
    Route to create a new transaction in the database.
    
    Args:
        transaction (schemas.TransactionCreate): The transaction data to 
            create.
        db (Session): The database session dependency.
        
    Returns:
        schemas.Transaction: The created Transaction object.
    """
    db_transaction = models.Transaction(**transaction.model_dump())
    db.add(db_transaction)  # Add the transaction to the session
    db.commit()  # Commit the transaction to the database
    db.refresh(db_transaction)  
    return db_transaction

