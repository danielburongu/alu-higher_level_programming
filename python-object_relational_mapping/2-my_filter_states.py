#!/usr/bin/python3
"""
takes an argument and matches name with the said states
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    tsk = MySQLdb.connect(user=argv[1], passwd=argv[2], tsk=argv[3])
    cur = tsk.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY states.id ASC".format(argv[4]))
    states = cur.fetchall()
    for k in states:
        if k[1] == argv[4]:
            print(k)
    cur.close()
    tsk.close()
