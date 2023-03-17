#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <mysql username>\
                            <mysql password>\
                            <database name>\
                            <state name>
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
    cur.execute("SELECT * FROM `cities` as `c`\
            INNER JOIN `states` as `s`\
            ON `c`.`state_id` = `s`.`id`\
            ORDER BY `c`.`id`")
    rows = cur.fetchall()
    print(", ".join([row[2] for row in rows if row[4] == state_name]))
