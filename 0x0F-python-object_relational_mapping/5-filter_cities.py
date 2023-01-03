#!/usr/bin/python3
""" Filter the query based on user input

"""
import sys
import MySQLdb


def filter_cities():
    """ Filter the  result """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute('SELECT cities.name '
                'FROM cities INNER JOIN states '
                'ON cities.state_id = states.id '
                'WHERE states.name = \'{}\' '
                'ORDER BY cities.id ASC'.format(sys.argv[4]))
    data = cur.fetchall()
    for index, row in enumerate(data):
        if index != len(data) - 1:
            print(row[0], end=', ')
        else:
            print(row[0])

    if len(data) == 0:
        print()


if __name__ == "__main__":
    filter_cities()
