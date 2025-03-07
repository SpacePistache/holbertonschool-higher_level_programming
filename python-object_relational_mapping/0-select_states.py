#!/usr/bin/python3
"""A script that lists all the states from the hbtn_0e_0_usa database"""

import mySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = mySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
