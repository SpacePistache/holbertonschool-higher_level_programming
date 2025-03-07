#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa,
sorting results in ascending order by cities.id while preventing SQL injection.
"""


import MySQLdb
import sys


def main():
    """Connects to the database and retrieves cities for the given state."""
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> "
		      "<database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, 
                             passwd=password, db=database)
        cursor = db.cursor()

        query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
        """
        cursor.execute(query, (state_name,))
        
        cities = [row[0] for row in cursor.fetchall()]
        print(", ".join(cities))

        cursor.close()
        db.close()
    except MySQLdb.Error as err:
        print("Error:", err)
        sys.exit(1)


if __name__ == "__main__":
    main()
