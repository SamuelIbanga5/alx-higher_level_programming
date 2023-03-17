#!/usr/bin/python3
# Script that lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb
args = sys.argv
mysql_username = args[1]
mysql_password = args[2]
database_name = args[3]
try:
    db = MySQLdb.connect(user=mysql_username, passwd=mysql_password, db=database_name)
except:
    print('Cannot connect to database')

cur = db.cursor()
cur.execute(f"SELECT * FROM {database_name}.states")
rows = cur.fetchall()
for row in rows:
    print(row)
