#!/usr/bin/python3
"""This module makes a query from hbtn_0e_4_usa an join both tables"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    database = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                               db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN\
                   states ON cities.state_id=states.id ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()
