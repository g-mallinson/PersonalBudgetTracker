CREATE DATABASE budget_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

\c budget_db

CREATE TYPE category AS ENUM ('salary', 'food', 'transport', 'entertainment', 'utilities', 'other');
CREATE TYPE transaction_type AS ENUM ('income', 'expense');

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    category category NOT NULL,
    type transaction_type NOT NULL,
    description TEXT,
    date DATE NOT NULL
);

INSERT INTO transactions (amount, category, type, description, date)
VALUES (1000, 'salary', 'income', 'First salary', '2021-01-01'),
    (100, 'food', 'expense', 'Lunch', '2021-01-01'),
    (50, 'transport', 'expense', 'Bus ticket', '2021-01-01'),
    (200, 'entertainment', 'expense', 'Concert ticket', '2021-01-01'),
    (100, 'utilities', 'expense', 'Electricity bill', '2021-01-01'),
    (50, 'other', 'expense', 'Gift', '2021-01-01');
