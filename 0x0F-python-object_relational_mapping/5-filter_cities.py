#!/usr/bin/python3
"""This module makes a query from hbtn_0e_4_usa an join both tables"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    database = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                               db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT cities.name "
                   "FROM cities "
                   "JOIN states "
                   "ON cities.state_id=states.id AND states.name=%s "
                   "ORDER BY cities.id ASC ", (argv[4],))
    rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows))
    cursor.close()
    database.close()
