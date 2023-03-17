#!/usr/bin/python3
# Script that lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
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
    cur.execute(f"SELECT * FROM {dbname}.states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
