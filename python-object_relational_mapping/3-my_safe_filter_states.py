#!/usr/bin/python3
"""
script that is safe from SQL injections
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    tsk = MySQLdb.connect(user=argv[1], passwd=argv[2], tsk=argv[3])
    cur = tsk.cursor()
    check = (argv[4], )
    cur.execute("SELECT * FROM states WHERE name = %s\
    ORDER BY states.id ASC", check)
    states = cur.fetchall()
    for k in states:
        print(k)
    cur.close()
    tsk.close()
