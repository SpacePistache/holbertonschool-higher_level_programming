#!/usr/bin/python3
"""
This script safely retrieves all rows from the 'states' table
where the name matches the provided argument, preventing SQL injection.
"""


import MySQLdb
import sys


def main():
    """Connects to MySQL database and performs a safe query."""
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> "
              "<database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as err:
        print("Error:", err)
        sys.exit(1)


if __name__ == "__main__":
    main()
