#!/usr/bin/python3
"""This module makes a query to the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    database = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                               db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT id, name FROM states WHERE name LIKE '{}' ORDER BY\
                   id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
           print(row)
    cursor.close()
    database.close()
