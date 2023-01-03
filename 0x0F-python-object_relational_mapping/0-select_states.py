#!/usr/bin/python3
""" Access a database from python scripts using SQL queries and
   the module MySQLdb

"""
import sys
import MySQLdb


def access_database():
    """ Access a database """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3360)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    data = cur.fetchall()
    for row in data:
        print(row)


if __name__ == "__main__":
    access_database()
