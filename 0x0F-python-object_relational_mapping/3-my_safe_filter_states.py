#!/usr/bin/python3

"""
a script that takes in an argument and displays all vvalues in the
states where 'name' matches the argument.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Allows access to the database
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name=%s\
        ORDER BY states.id ASC", (sys.argv[4],))

    rows = db_cursor.fetchall()
    for r in rows:
        print(r)

    db_cursor.close()
    db.close()
