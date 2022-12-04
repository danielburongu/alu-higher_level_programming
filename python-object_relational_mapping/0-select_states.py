#!/usr/bin/python3
"""
script to list all states from database hbtn_0e_usa:
script takes 3 arguments mysql username, mysql passwd, database name
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states Asending Order by states.id """)
    states = cur.fetchall()
    for k in states:
        print(k)
    cur.close()
    db.close()
