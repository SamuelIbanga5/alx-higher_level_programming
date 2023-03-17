#!/usr/bin/python3
# Script that takes in arguments and displays all values\
# in the states table of hbtn_0e_0_usa where name matches\
# the argument. But tis time a script that is safe from MySQL injections.
# Usage: ./3-my_safe_filter_states.py <mysql username> \
#                                     <mysql password> \
#                                     <database_name> \
#                                     <state name searched>
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
    cur.execute(f"SELECT * FROM {dbname}.states WHERE\
            (name = '@{state_name}')")
    rows = cur.fetchall()
    for row in rows:
        print(row)
