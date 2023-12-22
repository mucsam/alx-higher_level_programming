#!/usr/bin/python3
"""lists states with a name starting with N from the database
hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'"
                "ORDER BY states.id ASC")
    querry_rows = cur.fetchall()
    for row in querry_rows:
        print(row)
