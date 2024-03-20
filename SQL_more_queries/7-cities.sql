-- create a database and a table inside the database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL, FOREIGN KEY(id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
