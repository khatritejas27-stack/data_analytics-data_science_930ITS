import sqlite3
#create a datbase connection
conn=sqlite3.connect("om_db")
#create table scheam inside of database
cur=conn.cursor()
insertCountry=[
    (1,'india','29-10-2026'),
    (2,'usa','29-10-2026'),
    (3,'china','29-10-2026')
    ]
#insert a country tables
cur.executemany("""

insert or ignore into country values(?,?,?)

""",insertCountry)

insertstate=[
    (1,'gujrat',1),
    (2,'uttarpradash',1),
    (3,'calfornia',2),
    (4,'shagi',3)
    ]
#insert a country tables
cur.executemany("""

insert or ignore into state values(?,?,?)

""",insertstate)

insertcity=[
    (1,'ahmdabad',1),
    (2,'vododra',1),
    (3,'mirzapur',2),
    (4,'vanasi',2)
    ]
#insert a country tables
cur.executemany("""

insert or ignore into city values(?,?,?)

""",insertcity)

insertUser=[
    (1,'19','om','railnager',' 12th',  1,1,1),
    (2,'19','ram','railnager','12th',  1,1,2),
    (3,'19','shaym','railnager','12th',1,2,3),
    (4,'19','ajay','railnager','12th', 1,2,4),
    (5,'19','raj','railnager','12th',  1,1,1)
    
    ]
#insert a country tables
cur.executemany("""

insert or ignore into user values(?,?,?,?,?,?,?,?)

""",insertUser)

conn.commit()
print("data add succesfully in table")
conn.close()