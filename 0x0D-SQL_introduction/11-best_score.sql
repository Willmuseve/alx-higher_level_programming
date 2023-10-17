-- a script that lists all records with score above or equal 10
--in the second_table
-- results should be ordered by score(top first)
--displays both the score and the name

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
