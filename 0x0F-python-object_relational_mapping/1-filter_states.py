#!/usr/bin/python3
""" Using Python to filter the results gotten for DBAPI2.0

"""
import sys
import MySQLdb


def filter_result():
    """ Filter result from database """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    data = cur.fetchall()
    for row in data:
        if row[1].startswith('N'):
            print(row)


if __name__ == "__main__":
    filter_result()
