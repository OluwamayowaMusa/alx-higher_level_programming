#!/usr/bin/python3
""" Access a table in database from Python Script

"""
import sys
import MySQLdb


def cities():
    """ Access the cities table """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name '
                'FROM cities INNER JOIN states '
                'ON cities.state_id = states.id '
                ' ORDER BY cities.id ASC')
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    cities()
