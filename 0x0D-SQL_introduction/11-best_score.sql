-- list rows above 10 score sorted by score
SELECT score, name FROM second_table WHERE score >= 10
ORDER BY score DESC;