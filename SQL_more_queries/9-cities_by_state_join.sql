-- Lists a join of two tables cities and states but only some columns.
SELECT DISTINCT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
