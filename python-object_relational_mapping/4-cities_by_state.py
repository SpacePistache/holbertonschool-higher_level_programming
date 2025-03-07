#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa,
sorting results in ascending order by cities.id.
"""


import MySQLdb
import sys


def main():
    """Connects to the database and retrieves all cities with their states."""
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password>"
              "<database_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()

        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """
        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.Error as err:
        print("Error:", err)
        sys.exit(1)


if __name__ == "__main__":
    main()
