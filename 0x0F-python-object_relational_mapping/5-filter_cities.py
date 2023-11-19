#!/usr/bin/python3

"""
a script tat Takes in the name of a state as an argument and
lists all cities of that state
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor_db = db.cursor()
    cursor_db.execute(
        """
        SELECT cities.name
        FROM cities
        INNER JOIN states on states.id=cities.state_id
        WHERE states.name=%s""", (sys.argv[4],)
    )

    rows = cursor_db.fetchall()

    print(", ".join(row[0] for row in rows))

    cursor_db.close()
    db.close()
