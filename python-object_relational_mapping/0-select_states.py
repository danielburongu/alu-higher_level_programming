#!/usr/bin/python3
"""
script to list all states from database hbtn_0e_usa:
script takes 3 arguments mysql username, mysql passwd, database name
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    tsk = MySQLdb.connect(user=argv[1], passwd=argv[2], tsk=argv[3])
    cur = tsk.cursor()
    cur.execute("""SELECT * FROM states Asending Order by states.id """)
    states = cur.fetchall()
    for k in states:
        print(k)
    cur.close()
    tsk.close()
