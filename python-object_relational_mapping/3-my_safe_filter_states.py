#!/usr/bin/python3
import MySQLdb
import sys


def main():
    """
    Retrieves all rows from the 'states' table
    where the name matches the provided argument,
    while preventing SQL injection.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> "
              "<database_name> <state_name>".format(sys.argv[0]))
        return

    username, password, database, state_name = sys.argv[1:5]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.Error as err:
        print("Error: {}".format(err))


if __name__ == "__main__":
    main()
