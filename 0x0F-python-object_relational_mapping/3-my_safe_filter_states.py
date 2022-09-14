#!/usr/bin/python3
""" Using queries safe from SQL injection

"""
import sys
import MySQLdb


def safe_query():
    """ Access a database with a query safe from SQL
        injection
    """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    user_input = sys.argv[4].split()
    cur.execute('SELECT * FROM states WHERE name = \'{}\''
                'ORDER BY id ASC'.format(user_input[0]))
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    safe_query()
