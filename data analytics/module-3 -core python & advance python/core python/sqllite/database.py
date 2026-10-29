import sqlite3
con=sqlite3.connect("sms-ab")
print("sql is connected")
cur=con.cursor()
# create an schema of country tables 
cur.execute("""
            create table if not exists country(
                cid integer primary key autoincrement,
                countryname text,
                created_date text
            )
            
            """)
# create an schema of state tables 
cur.execute("""
            create table if not exists state(
                sid integer primary key autoincrement,
                statename text,
                created_date text
            )
            
            """)

# create an schema of city tables 
cur.execute("""
            create table if not exists city(
                ctid integer primary key autoincrement,
                cityname text,
                created_date text
            )
            
            """)

print("table successfully created")

con.commit() #save file
con.close() 