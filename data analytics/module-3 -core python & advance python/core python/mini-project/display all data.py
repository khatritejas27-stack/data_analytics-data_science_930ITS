import sqlite3
import pandas as pd
#create a datbase connection
conn=sqlite3.connect("om_db")
#print("database connect sussesfuiiy")
#create table scheam inside of database
cur=conn.cursor()
#display all data
select ="select *from user"
df=pd.read_sql(select,conn)
print(" data fetch succesfully \n",df)
# display all via join data 
# select="select users.*,cname,sname,ctname from users join country on users.cid=country.cid join state on users.sid=state.sid 
# join city on users.ctid=city.ctid"

# # fetched data via pandas 
# df=pd.read_sql(select,conn)
# print("=============display data after join=================== \n")
# print("data fetched successfully \n",df)

# fetched data via execute and cursor 
# select="select users.*,cname,sname,ctname from users join country on users.cid=country.cid join state on users.sid=state.sid join city on users.ctid=city.ctid"
# cur.execute(select)
# df=cur.fetchall()
# print("=============display data after join=================== \n")
# print("data fetched successfully \n",df)


# select="select users.*,cname,sname,ctname from users join country on users.cid=country.cid join state on users.sid=state.sid join city on users.ctid=city.ctid where uid=1"
# cur.execute(select)
# df=cur.fetchall()
# print("=============display data after join=================== \n")
# print("data fetched successfully \n",df)



select="select users.*,cname,sname,ctname from users join country on users.cid=country.cid join state on users.sid=state.sid join city on users.ctid=city.ctid"
df=pd.read_sql(select,conn)
print("=============display data after join=================== \n")
print("data fetched successfully \n",df)

conn.commit()
conn.close()

