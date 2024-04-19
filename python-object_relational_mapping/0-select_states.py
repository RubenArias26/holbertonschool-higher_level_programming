#!/usr/bin/python3
"""
this module connect with mysql
"""

import MySQLdb
import sys
if __name__ == "__main__":

    db = MySQLdb.connect(
        host = "localhost",
        user = sys.argv[1],
        password = sys.argv[2],
        port = 3306,
        database = sys.argv[3],
    )

    cur = db.cursor()
    # this is a query for obtain data order by id
    cur.execute("SELECT * FROM states ORDER BY states.id")

    # retrive all the rows
    rows = cur.fetchall()

    # show the result of the query
    for row in rows:
        print(row)

    # close the cursor and connection
    cur.close
    db.close