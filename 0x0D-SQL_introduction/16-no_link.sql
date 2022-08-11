-- Lists all records of the table with a condition
SELECT score, name 
FROM second_table
WHERE name != 'null'
ORDER BY score DESC;
