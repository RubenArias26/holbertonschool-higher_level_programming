#!/usr/bin/python3
"""
COnecta con mysql
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # establece coneccion con mysql
    db = MySQLdb.connect(
        host = "localhost",
        user = sys.argv[1],
        password = sys.argv[2],
        port = 3306,
        database = sys.argv[3],
    )

    # establecemos un cursor
    cur = db.cursor()
    # creamos la consulta
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    # recuperamos los datos de la consulta
    rows = cur.fetchall()

    # imprimimos la consulta
    for row in rows:
        print(row)

    # cerramos el cursor y el connect
    cur.close
    db.close
