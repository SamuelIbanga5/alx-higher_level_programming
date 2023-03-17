#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
Usage: ./4-cities_by_state.py <mysql username>\
                              <mysql password>\
                              <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    passwd = args[2]
    dbname = args[3]
    db = MySQLdb.connect(user=user, passwd=passwd, db=dbname)
    cur = db.cursor()
    cur.execute(f"SELECT `c`.`id`, `c`.`name`, `s`.`name`\
            FROM {dbname}.cities as `c`\
            INNER JOIN `states` as `s`\
            ON `c`.`state_id` = `s`.`id`\
            ORDER BY `c`.`id`")
    rows = cur.fetchall()
    for row in rows:
        print(row)
