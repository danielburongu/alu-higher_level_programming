-- a script that creates the table unique_id on your MySQL server.
--  The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256))
