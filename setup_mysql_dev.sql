-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS mlg_dev_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'mlg_dev'@'localhost' IDENTIFIED BY 'mlg_dev_pwd';

-- Grant all privileges on mlg_dev_db to mlg_dev
GRANT ALL PRIVILEGES ON mlg_dev_db.* TO 'mlg_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to mlg_dev
GRANT SELECT ON performance_schema.* TO 'mlg_dev'@'localhost';
