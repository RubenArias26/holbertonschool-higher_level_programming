-- lists all cities from california withotut using JOIN keyword.
SELECT id, name
FROM cities
WHERE state_id =
	( SELECT id
	FROM states
	WHERE name = "California"
	)
ORDER BY id ASC;
