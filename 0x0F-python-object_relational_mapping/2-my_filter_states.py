#!/usr/bin/python3
# Script that takes in an argument and displays all values in the states table
# of hbtn_0e_0_usa where name matches the argument.
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state name searched>
import sys
import MySQLdb
args = sys.argv
mysql_username = args[1]
mysql_password = args[2]
database_name = args[3]
state_name = args[4]
try:
    db = MySQLdb.connect(user=mysql_username, passwd=mysql_password, db=database_name)
except:
    print("Database not connected...")
cur = db.cursor()
cur.execute(f"SELECT * FROM {database_name}.states WHERE (name = '{state_name}')")
rows = cur.fetchall()
for row in rows:
    print(row)
