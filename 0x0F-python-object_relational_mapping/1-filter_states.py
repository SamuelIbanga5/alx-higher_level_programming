#!/usr/bin/python3
# Script that lists all states with a name starting with N
# from the database hbtn_0e_0_usa
# Usage: ./1-filter_states.py <mysql username> \
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
    print('Database cannot connect...')
cur = db.cursor()
cur.execute(f"SELECT * FROM {database_name}.states WHERE name LIKE 'N%'")
rows = cur.fetchall()
for row in rows:
    print(row)
