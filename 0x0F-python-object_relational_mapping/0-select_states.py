#!/usr/bin/python3
"""Module to get all states"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[0]
    password = argv[1]
    database = argv[2]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    querry_rows = cur.fetchall()
    for row in querry_rows:
        print(row)
