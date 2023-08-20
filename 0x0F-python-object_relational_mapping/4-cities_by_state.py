#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        c = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306,
            db=sys.argv[3]
        )
    except MySQLdb.Error:
        print("error connecting")
    try:
        d = c.cursor()
        d.execute("SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states\
        ON cities.state_id = states.id\
        ORDER BY cities.id")
        y = d.fetchall()
        for x in y:
            print(x)
    except MySQLdb.Error:
        print("execution failed")
    d.close()
    c.close()
