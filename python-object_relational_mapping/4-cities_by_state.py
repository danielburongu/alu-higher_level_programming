#!/usr/bin/python3
"""
Script to list all cities from the database/takes 3 arguments
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    tsk = MySQLdb.connect(user=argv[1], passwd=argv[2], tsk=argv[3])
    cur = tsk.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    states = cur.fetchall()
    for k in states:
        print(k)
    cur.close()
    tsk.close()
