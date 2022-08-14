-- List all the cities in the database using the join
SELECT cities.id, cities.name, states.name
FROM  cities INNER JOIN states
 ON cities.state_id = states.id;
