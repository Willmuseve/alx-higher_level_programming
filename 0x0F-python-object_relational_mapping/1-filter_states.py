#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    connect_db = MySQLdb.connect(
            host="localhost",port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cursor_db = connect_db.cursor()

    cursor_db.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    y = cursor_db.fetchall()

    for x in y:
        print(x)
