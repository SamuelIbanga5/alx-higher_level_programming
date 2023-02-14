-- SQL script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in MYSQL Server.
-- The result should display the score and the number of records for this score with the label numbere.
-- The list should be sorted by the number of records (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
