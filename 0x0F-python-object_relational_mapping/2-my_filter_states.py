#!/usr/bin/python3

"""
a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access to the db
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    db_cursor = db.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'\
        ORDER BY states.id ASC".format(sys.argv[4])
    )

    rows = db_cursor.fetchall()
    for r in rows:
        print(r)

    db_cursor.close()
    db.close()
