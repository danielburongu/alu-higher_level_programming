-- A script that lists all the records with the same score in the table
-- of the database in MYSQL sever
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
