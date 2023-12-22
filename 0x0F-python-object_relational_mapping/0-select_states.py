#!/usr/bin/python3
"""Module to get all states"""

import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="samuel",
                       passwd="50samuel", db="hbtn_0e_0_usa")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
querry_rows = cur.fetchall()
for row in querry_rows:
    print(row)
