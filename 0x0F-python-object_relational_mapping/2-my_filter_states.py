#!/usr/bin/python3
""" Filtering result from database based on User Input

"""
import sys
import MySQLdb


def filter_user():
    """ Filter result using user input condition """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name = \'{}\''.format(sys.argv[4]))
    print(cur.fetchone())


if __name__ == "__main__":
    filter_user()
