--a script that creates the database hbtn_0d_usa and the table cities
-- cities description:
-- 	  id INT unique, auto generated, can’t be null and is a primary key
--	  state_id INT, can’t be null and must be a FOREIGN KEY
-- 	  name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT AUTO INCREMENT PRIMARY KEY UNIQUE NOT NULL, state_id INT NOT NULL, name VARCHAR(256),
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
