-- Prints the state with max_temp in temperatures
SELECT state, MAX(value) AS max_temp
 FROM temperatures
 GROUP BY state
 ORDER BY state;
