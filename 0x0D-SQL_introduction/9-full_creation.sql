--a script that creates a second_table in the database hbtn_0c_0 in 
-- your MYSQL server and add multipE rows

CREATE TABLE IF NOT second_table(id INT, name VARCHAR(256), score INT);

INSERT INTO second_table(id INT, name VARCHAR(256), score INT)
VALUES(
	(1, "John", 10),
	(2 "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8)
)

