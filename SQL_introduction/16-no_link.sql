-- a script that lists all records of the table second_table
-- of the database in MYSQL sever
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
