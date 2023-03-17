#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username> \
                               <mysql password> \
                               <database name> \
                               <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    passwd = args[2]
    dbname = args[3]
    state_name = args[4]
    db = MySQLdb.connect(user=user, passwd=passwd, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM\
            {}.states WHERE (name = '{}')".format(dbname, state_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
