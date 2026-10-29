import sqlite3
#create a datbase connection
conn=sqlite3.connect("om_db")
#print("database connect sussesfuiiy")
#create table scheam inside of database
cur=conn.cursor()
#create a country tables
cur.execute("""
 create table if not exists country(
 cid integer primary key autoincrement,
 cname text,
 created_at text
 )

""")
#create a state tables
cur.execute("""
 create table if not exists state(
 sid integer primary key autoincrement,
 sname text,
 cid integer,
 foreign key(cid) references country(cid)
 )

""")
#create a city tables
cur.execute("""
 create table if not exists city(
 ctid integer primary key autoincrement,
 cityname text,
 sid integer,
foreign key(sid) references state(sid)
  
 )

""")
 
#create a city tables
cur.execute("""
 create table if not exists user(
 userid integer primary key autoincrement,
 age integer ,
 name text,
 address text,
 eductaion text,
 cid integer,
 sid integer,
 ctid integer,
foreign key(cid) references country(cid),
foreign key(sid) references state(sid),
foreign key(ctid) references city(ctid)
  
 )

""")



print("table created succesfully")
#save quary
conn.commit()
#close connection
conn.close()