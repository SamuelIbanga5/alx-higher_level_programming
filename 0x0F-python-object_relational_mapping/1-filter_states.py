#!/usr/bin/python3
# Script that lists all states with a name starting with N
# from the database hbtn_0e_0_usa
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    passwd = args[2]
    dbname = args[3]
    db = MySQLdb.connect(user=user, passwd=passwd, db=dbname)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {dbname}.states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
