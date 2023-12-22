#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name\
                FROM cities JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (stateName,))
    querry_rows = cur.fetchall()
    cities = []
    for row in querry_rows:
        cities.append(row[0])
    print(', '.join(cities))
    cur.close()
    conn.close()
