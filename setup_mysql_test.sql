-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS mlg_test_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'mlg_test'@'localhost' IDENTIFIED BY 'mlg_test_pwd';

-- Grant all privileges on mlg_test_db to mlg_test
GRANT ALL PRIVILEGES ON mlg_test_db.* TO 'mlg_test'@'localhost';

-- Grant SELECT privilege on performance_schema to mlg_test
GRANT SELECT ON performance_schema.* TO 'mlg_test'@'localhost';
