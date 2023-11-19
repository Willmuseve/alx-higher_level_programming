#!/usr/bin/python3

"""
A script that lists all states that start with  a name
starting with the letter n from the db hbtn_0e_0_us
"""


import MySQLdb
import sys

"""
access to get states from the database
"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY\
            id ASC")

    rows = db_cursor.fetchall()
    for r in rows:
        print(r)

    db_cursor.close()
    db.close()
