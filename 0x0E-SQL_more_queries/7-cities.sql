--a script that creates the database hbtn_0d_usa and the table cities

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT AUTO INCREMENT PRIMARY
KEY UNIQUE NOT NULL, state_id INT NOT NULL, name VARCHAR(256),
FOREIGN KEY(state_id) REFERENCES states(id));
