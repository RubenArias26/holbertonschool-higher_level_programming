#!/usr/bin/python3
"""
Este modulo sirve para con BD MySQL
Muestre todos los valores en la tabla de estados en la BD hbtn_0e_0_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Estableciendo la coneccion con MySQL
    db = MySQLdb.connect(
             host="localhost",
             user=sys.argv[1],
             passwd=sys.argv[2],
             port=3306,
             db=sys.argv[3],
    )
    cu = db.cursor()
    # Consulta para ordenar estados que empiecen con N ordenados por id
    cu.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
               .format(sys.argv[4]))

    # Recupera todas las filas(rows)
    rows = cu.fetchall()

    # Mustra el resultado
    for row in rows:
        print(row)

    # Cerrar el cursor y la coneccion
    cu.close()
    db.close()