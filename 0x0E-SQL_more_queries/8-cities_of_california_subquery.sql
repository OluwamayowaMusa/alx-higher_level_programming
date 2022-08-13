-- List all the cities in a states using subquery
SELECT id, name
 FROM cities
 WHERE state_id = (SELECT id
	            FROM states
		    WHERE name = "California");
