\c budget_db

DROP TABLE transactions;

DROP TYPE IF EXISTS category;
DROP TYPE IF EXISTS transaction_type;

\c postgres

DROP DATABASE budget_db;
