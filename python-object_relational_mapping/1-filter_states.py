#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N'
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM states where name LIKE 'N%'\
                 ORDER BY states.id ASC")
    states = curr.fetchall()
    for k in states:
        if k[1][0] == 'N':
            print(k)
    curr.close()
    db.close()
