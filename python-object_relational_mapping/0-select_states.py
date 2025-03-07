#!/usr/bin/python3
"""A module that connects to MySQL database retrieves and lists
all the states from the hbtn_0e_0_usa database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    for row in cur.fetchall():
        print(row)

    for state in states:
        print(state)

    cursor.close()
    db.close()
