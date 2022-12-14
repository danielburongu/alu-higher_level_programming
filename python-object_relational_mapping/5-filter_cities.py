#!/usr/bin/python3
"""
Script that lists all cities of that state
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    check = (argv[4], )
    cur.execute("SELECT * FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC", check)
    states = cur.fetchall()
    cities = []
    for k in states:
        if k[4] == check[0]:
            cities.append(k[2])
    print(', '.join(cities))
    cur.close()
    db.close()
