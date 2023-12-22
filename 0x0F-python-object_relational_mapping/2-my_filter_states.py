#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table
of hbtn_0e_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'\
                ORDER BY states.id ASC".format(stateName))
    querry_rows = cur.fetchall()
    for row in querry_rows:
        print(row)
    cur.close()
    conn.close()
