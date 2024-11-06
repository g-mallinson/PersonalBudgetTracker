## Personal Budget Tracker

### Description


### Features

- **Transaction Management**: 
  - Add new transactions with details such as date, description, category, amount, and transaction type (income or expense).
  
- **Database Integration**:
  - PostgreSQL database setup with SQLAlchemy ORM for efficient data management.
  - Predefined database schema for transactions, including categories and transaction types.

- **API Endpoints**:
  - FastAPI-based backend providing RESTful API endpoints for managing transactions.
  - Endpoints to create and retrieve transactions.

- **Frontend**:
  - SvelteKit-based frontend for a responsive and interactive user interface.
  - Form to add new transactions and display the list of transactions.

### Technologies Used

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: SvelteKit, Axios
- **Others**: Docker for containerization, GitHub Actions for CI/CD

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/personal-budget-tracker.git
   cd personal-budget-tracker
   ```

2. **Backend Setup**:
   - Navigate to the backend directory:
     ```sh
     cd backend
     ```
   - Create a virtual environment and install dependencies:
     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     pip install -r requirements.txt
     ```
   - Set up the PostgreSQL database and apply migrations:
     ```sh
     psql -U postgres -f create_database.sql
     ```

3. **Frontend Setup**:
   - Navigate to the frontend directory:
     ```sh
     cd ../budget-tracker
     ```
   - Install dependencies and start the development server:
     ```sh
     npm install
     npm run dev
     ```

### Usage

- **Run the Backend**:
From the `root` directory, run the following command to start the backend server:
  ```sh
  uvicorn backend.main:app --reload
  ```

- **Access the Frontend**:
  Open your browser and navigate to `http://localhost:5173/transactions`.

### Notes

- Ensure PostgreSQL is running and accessible.
- Adjust the database connection settings in `database.py` if necessary.

