#!/usr/bin/python3

"""
a script that lists all states in the db hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Allows access to the db to get the states
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    sql_query = "SELECT * FROM states ORDER BY states.id"
    rows = cursor.execute(sql_query)

    for r in range(rows):
        print(cursor.fetchone())

    cursor.close()
    db.close()
