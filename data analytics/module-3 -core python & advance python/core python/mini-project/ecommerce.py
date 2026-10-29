import sqlite3
con=sqlite3.connect("ecommerse")
cur=con.cursor()
#create catagory
cur.execute("""
     create table if not exists catagory(
     catid integer,
     cat_name text
     )
""")
#create subcatagory
cur.execute("""
     create table if not exists subcatagory(
     subid integer,
     sub_name text,
     catid integer,
     foreign key(catid) references catagory (catid)
     )
""")

#create product
cur.execute("""
     create table if not exists product(
     proid integer,
     pro_name text,
     catid integer,
     subid integer,
     foreign key(catid) references
     catagory (catid)
     foreign key(subid) references subcatagory(subid)
     )

""")

print("table created succesfully")
#save quary
con.commit()
#close connection
con.close()