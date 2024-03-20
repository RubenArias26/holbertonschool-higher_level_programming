-- Create a database and a table inside of the new database.
CREATE DATABASE IF NOT EXISTS hbtn_od_usa;

USE hbtn_od_usa;

CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
