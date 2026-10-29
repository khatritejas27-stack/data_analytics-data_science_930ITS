## Tasks 1:Install the sqlite3 module in Python and write a script to create a new database called 
# foode.db with a table Restaurants (id, name, cuisine, rating).

import sqlite3

conn=sqlite3.connent("food.db")

cur = conn.cursor()

cur.execute("""
   create table if not exist restaurant(
   id integer primary key autoincrement,
   name text,
   cuisin text,
   rating text
   
   )

""")