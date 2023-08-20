#!/usr/bin/python3
""" A script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument. But
this time, write one that is safe from MySQL injections """
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
    d = c.cursor()
    try:
        d.execute("SELECT * FROM states WHERE name = %s ORDER BY\
        states.id", (sys.argv[4],))
        y = d.fetchall()
        for x in y:
            print(x)
    except MySQLdb.Error:
        print("execution failed")
    d.close()
    c.close()
