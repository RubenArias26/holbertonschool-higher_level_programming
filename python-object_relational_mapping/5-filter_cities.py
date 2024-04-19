#!/usr/bin/python3
"""
Conecta con mysql
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

    cu = db.cursor()
    match = sys.argv[4]
    cu.execute ("""SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s """, (match,))
    
    rows = cu.fetchall()

    city_name = [row[0] for row in rows]

    resutl = ", ".join(city_name)

    print(resutl)


    cu.close()
    db.close()