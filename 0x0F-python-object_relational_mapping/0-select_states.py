#!/usr/bin/python3
"""This module makes a query to the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    database = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                               db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()
