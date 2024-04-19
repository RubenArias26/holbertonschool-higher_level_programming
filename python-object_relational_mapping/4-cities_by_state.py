import MySQLdb
import sys

if __name__ == "__main__":
    # establish the connection
    db = MySQLdb.connect(
        host = "localhost",
        user = sys.argv[1],
        password = sys.argv[2],
        port = 3306,
        database = sys.argv[3],
    )

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id""")

    rows = cur.fetchall()

    # retrive all rows
    for row in rows:
        print(row)
    
    # close the cursor and connect
    cur.close()
    db.close()