 
# what is sql?
1. SQL stand for structure query langage
2. SQL is used to create database and table structure 
3. SQL is used as a structure query langage and it is create an
structure of database and table or structure type of data
 **table structure**
 **user**

|uid| uname| gender | address|
|---|------|--------|--------|
| 1 | A    | male   | rjt    |
| 2 | B    | female | rjt    |

4. Sql is case-insesative languge
 example :INSERT |insert| Insert (camlae case)
5. SQL is not conditional
6. SQL is used to provides relation between table using Normalition
7. SQL create some query or commands to create database or table structure

 ## sql type od Query or command
 1. DDL : **data defination language**
 2. DML : **data manipulation language**
 3. DQL : **data query language**
 4. TCL : **transation controle language**
 
## DDL ... data defination language
 1. DDL stans for data efination language 
 2. DDL is used to create database|create table |alter data |rename table |
  changed table column name | drop database & table structured|truncate data
  -create  
  -alter  
  -drop  
  -change  
  -rename
  -truncate  
  
## how to create database
  **syntax**
``` 
 create database database name 
```

  **example**
  ```
  create database da_db
  ```


# SQL Data Types Reference
| Column Name | Data Type | Size | Description |
|-------------|-----------|------|-------------|
| id | INT | 11 | Integer value, commonly used as a primary key |
| name | CHAR | 1–255 | Fixed-length character string |
| name | VARCHAR | 0–255 | Variable-length string; accepts letters, numbers, and special characters |
| password | VARCHAR | 8–255 | Variable-length string used to store a password/hash |
| email | VARCHAR | 5–255 | Stores an email address |
| phone | VARCHAR | 7–20 | Stores a phone number |
| age | INT | 11 | Stores an integer value such as age |
| price | DECIMAL | 10,2 | Stores exact decimal numbers, e.g. 99999.99 |
| salary | DECIMAL | 10,2 | Stores salary or monetary values |
| quantity | INT | 11 | Stores whole-number quantities |
| status | TINYINT | 1 | Commonly used for boolean values such as 0 = false, 1 = true |
| is_active | BOOLEAN | 1 | Stores TRUE or FALSE |
| gender | CHAR | 1 | Stores a single character |
| description | TEXT | 65,535 bytes | Stores long text |
| address | VARCHAR | 0–255 | Stores an address |
| city | VARCHAR | 0–100 | Stores a city name |
| state | VARCHAR | 0–100 | Stores a state name |
| country | VARCHAR | 0–100 | Stores a country name |
| pincode | VARCHAR | 4–10 | Stores postal/PIN codes |
| date_of_birth | DATE | 3 bytes | Stores a date in `YYYY-MM-DD` format |
| created_at | DATETIME | 8 bytes | Stores date and time |
| updated_at | DATETIME | 8 bytes | Stores date and time of last update |
| login_time | TIMESTAMP | 4 bytes | Stores a timestamp |
| year | YEAR | 1 byte | Stores a year |
| image | BLOB | Up to 65,535 bytes | Stores binary data such as a small image |
| file_data | LONGBLOB | Up to 4 GB | Stores large binary files |
| notes | TEXT | 65,535 bytes | Stores additional text/notes |
| json_data | JSON | Variable | Stores JSON-formatted data |
| uuid | CHAR | 36 | Stores a UUID |


**syntax**
``` sql
create table tablename
(
  id int auto_increment primary key,
  columname datatype(size),
  .
  .
  .
  columnname data type
)
```
**what is primary key**
1. a pk is never stored null values
2. a pk only defined once time in a table
3. a pk stored unique values

**example**
```sql
(
    cretae table users
    (
        id int auto_increment primary key,
        name varchar(255) ,
        email varchar(255) ,
        epassword varchar(255) ,
        pincode int,
        salary float,
        address text,
        phone bigint
    )
)
'''
''' sql
create table products
(
    pid int AUTO_INCREMENT PRIMARY KEY,
    pname varchar(255),
    photo blob ,
    oldprice int ,
    offerprice int,
    qty int ,
    status enum('active','deactive'),
    descriptions text
)

create tabal employee
(
    empid int auto_increment primary key ,

)
```
# alter
1. alter is used to change tabel columname | add tabel new column alter is used 
2. alter is also update columname of tabel and also add unique key in tabel 
3. alter is used to change or update or modify tabel column name 

**syntax**
``` sql
alter tabel tabelname add columnname datatype(255)
or
alter tabel users add gender varchar(255)
``` 
 
# add columname specific column
 ```sql
 alter tabel user add photo varchar(255) after name;
 
 select tabel users add photo varchar(255) after name;
```
 

# update any specific columnname
 ```
 alter tabel user change phone mobile bigint;
 ```
## alter used to add unique key in tabels (unique key never store dublicate values)
**syntax**
```
ALTER TABLE `employee` ADD UNIQUE (`email`);  
```
# change is used in alter to change any columnname 
**syntax**
```
 alter tabel user change phone mobile bigint;
```
 # rename : rename is used to change a tabel name
 **syntax**
```
rename tabel tablename  to  new table name;
or
rename tabel users to  tbl_users;
```
# truncate : truncate is used to empty or delete all data at once time
 ## note : after truncate we never rollback our data
 ```
 truncate tabel  tbl_employee:
 ```
# drope : drope is used to drop or delete database  or tabel strutures
## note: after drop we never rollback
**syntax**
```
drop database databasename; ,

drop table tabelname ;
```


# crate product table
```sql
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    -- Basic Information
    sku VARCHAR(100) UNIQUE NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    product_code VARCHAR(100),
    barcode VARCHAR(100),
    description TEXT,
    short_description text,
    -- Category & Brand
    category_id INT,
    subcategory_id INT,
    brand_id INT,
    -- Pricing
    cost_price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    selling_price DECIMAL(10,2) NOT NULL,
    discount_price DECIMAL(10,2),
    tax_rate DECIMAL(5,2) DEFAULT 0.00,
    -- Inventory
    stock_quantity INT DEFAULT 0,
    minimum_stock INT DEFAULT 0,
    maximum_stock INT DEFAULT 0,
    reorder_level INT DEFAULT 0,
    -- Physical Attributes
    weight DECIMAL(10,2),
    length DECIMAL(10,2),
    width DECIMAL(10,2),
    height DECIMAL(10,2),
    unit VARCHAR(50),
    -- Product Details
    color VARCHAR(100),
    size VARCHAR(100),
    material VARCHAR(255),
    model VARCHAR(100),
    manufacturer VARCHAR(255),
    country_of_origin VARCHAR(100),
    -- Images
    image_url VARCHAR(500),
    thumbnail_url VARCHAR(500),
    -- SEO
    slug VARCHAR(255) UNIQUE,
    meta_title VARCHAR(255),
    meta_description TEXT,
    meta_keywords TEXT,
    -- Status
    is_active BOOLEAN DEFAULT TRUE,
    is_featured BOOLEAN DEFAULT FALSE,
    is_digital BOOLEAN DEFAULT FALSE,
    -- Dates
    manufacture_date DATE,
    expiry_date DATE,
    -- Audit Fields
    created_by INT,
    updated_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

);
```

## DML..data manipulation language
**thare are Quary in DML**
1. insert 
1. delete
3. update  

# how to insert data 

**syntax**

**single data insert**
``` sql
insert into tablename(columname) value ('value')
or
INSERT into tbl_employee
value(null,'kumar',kumar@gmail,'8156514561','railnager',null,'male','5156156',null), (null,'ramsh',rumash@gmail,'899999999','railnager',null,'male','821549',null);
or
INSERT into tbl_employee
colume(name,email,mobile,address,photo,gender,adhar card ,uid)
value('kumar',kumar@gmail,'8156514561','railnager',,'male','5156156',), (null,'ramsh',rumash@gmail,'899999999','railnager',null,'male','821549',null);
```

## delete data from tables
**syntax**
``` sql
delete all data
delete from tablename ;
or
delete particular data
delete from tablename whare cid = 3;
delete from country whare cid = 3;
or
delete 2 data at once times
delete from tablename whare cid in (4,6,9);
delete from country whare cid in (4,6,9);
or
delete range of data
delete from tablename whare cid between 2 and 8; 
delete from country whare cid between 2 and 8; 

```
1.delete is used to delete all data from table
2.delete is used to delete particular data from table
3.delete is used to delete range of data from table 
4.delete is used to delete  altenate of data

# update the data or row
 **syntax**
```sql
update table set columname='value' where id='id'
or
update table tbl_country set cname='bhutan' where cid=10;
```
## DQL : data Quary lanuage

 1. DQl is handle to select all data from table
 2. DQl is handle to fretch all data from table
 3. DQl is handle particular fetch data from table
 4. DQl is handle particular fetch range of data from table
 5. DQl is handle particular fetch altenet data from table
 6. DQl is handle particular fetch limit of data from table

**quary in DQL**
```
select
1. how to select all data
    select * from tbl_employee
2. select particular data from id or name
    select *from tbl_employee whare empid=8
    or
    select *from tbl_employee whare name=deep
3. select particular data of columns
    select empid,name,email,gender,phone,deprtment from tbl_employee
4. select particular columns of one data
    select empid,name,email,gender,phone,deprtment from tbl_employee where name ='deep'
5. select particular range of data
    select * from tbl_employee whare empid between 3 and 8;
6. select particular alternet data
    select * from tbl_employee where empid in (3,8,5,4);
    or
    select * from tbl_employee where name in ('astha','punit','deep');
    or
    select * from tbl_employee where name in ('astha','punit','deep') order by name dsc;
    or
    select * from tbl_employee where name in ('astha','punit','deep') order by name asc;(by default);
7. select data using limit 
    select *from tbl_employee where empid limit 0,3; first number is ofset number
    or
    select *from tbl_employee where empid limit 2,6; ex: print data 3 to 8

8. select or filter data using **order by**
    select*from tbl_employee order by name desc ;
9. group by..
   select data or filter data on group of columns

   select sum(salary) ,departmaent from tbl_employee group by deprtment;
```
# alias : 
1. alias is change any column name in SQL temporary
```
select salary as salary_of_employee from tbl_employee where salary >=20500;
```


# TCL : transactional control language

1. TCL is used for transactional control language 
2. TCL is used for transaction query 
3. TCL query are 

**examples :** 
- commit 
- rollback 

# what is is commit ? 

1. commit is part of TCL 
2. after delete any data we rollback but before delete we done **commit**
3. commit is used to save data in tables 

**examples**

```
START TRANSACTION;
delete from tbl_employee where empid=1;
commit;
```

# what is is  rollback ? 

1. rollback is part of TCL 
2. after delete any data we rollback but before delete we done **commit**
3. rollback is used to rollback data after delete in tables 

**examples**

```
START TRANSACTION;
delete from tbl_employee where empid=1;
select * from tbl_employee where empid=1
rollback;
select * from tbl_employee where empid=1

```


## SQL function
1. SQL function is used as pre-define function
2. type of function
  - aggrigate function
  - scalar function

# aggrigate function :
 1. sum()
 2. avg()
 3. count()
 4. max()
 5. min()

# scalar function:
1. first()
2. last()
3. lcase()
4. ucase()
5. now()
6. round()
7. date()
  
  **whare (clasue)**
# sum() :

1. sum the value
```sql
select sum (salary) as sum_of_salary from tbl_employee ; --as : alyas nick name 
```
2. sum of salary on group of columns **group by**
```sql
select sum(salary),department from tbl_employee group by department 
```
3. sum of salary on group of columns **group by** and select depatment
```sql
select sum(salary),department from tbl_employee where department in ('it','cse') group by department;
```
# avg(): find the avg
1. select avg(salary) from tbl_employee
# count():
1. select count(empid) as total_number_employee from tbl_employe;
# max(): find max value
1. selct max(salary) as highest_salary from tbl_employe 
2. find second salary **using subquary method**
```sql
SELECT max(salary) from employee where salary <(select max (salary) from employee); 
```
3. find second salary using limit and order by
```sql
SELECT *from employee ORDER by salary desc LIMIT 1,1;
```

# min(): find min value
1. selct min(salary) as lowest_salary from tbl_employe 

**subquary**

# find first rows data
```sql
select first (empid) from employee
```
# find last row data
```sql
select last (empid) from employee
```
# convert in lcase row data
```sql
select lcase(name) from employee
```
# convert in ucase row data
```sql
select ucase(name) from employee
```
# round values 
```sql
select round(salary) from employee
```
# now()
```sql
select now(),date from employee
```

# date() find the date from tables
 ```sql
 select date(), date from employee
 ```

## what is like opertaor in SQL ?
1. like opertor is used serch data from table with keybord
2. like opertor is used serch using its wildcard (%)
 
 star character with 'd%'
 or
```sql
select * from employee where name like '%d';
 or
 select * from employee where name like 'h%';
 or
 select * from employee where name like '%a%';

```
# what is subquery ?

1. query within another query i.e called subquery

**solution to find second highest salary**

- select max(salary) as second_highest_salary from tbl_employee where salary < (select max(salary) from tbl_employee);


## key constraints in sql ?
 1.key constraints provides limit on table
 2.key constraints used to set primry key | unique key | foreign key on table
 3.key constraints provide limitation on table
 4.key constraints provide relationship b/w table

# what is key constraints ?
1. provides limit on tables via pk | uk | fk | ck
2. types of key constraints 
1. primary key
2. unique key
3. foreign key
4. compound key

## primary key

1. a pk onliy provide one time in tables
2. a pk key never repetad more than one time
3. a pk unique value and never return null value
4. a pk should be auto incremnts

**users**

|uid(pk)|  uname  | age | address  | company   |
|-------|---------|-----|----------|-----------|
|   1   | brij007 |  35 |  rjt     |  tops     |
|   2   | anil007 |  35 |  rjt     |  tops     |
|   3   | anshu007|  25 |  rjt     |  tops     |     


**SQL provides PK**

```sql

create table users(

uid int auto_increment primary key,
uname varchar(100),
age int,
address text,
company varchar(200)

)
```
## unique key

1. a uk provide more than one time in tables
2. a uk key not repetad more than in a table
3. a pk store unique value and  return one time a null
4. a pk never return duplicate values

**users**

|  uid(pk)  | uname(uk) |   age   | address  | company   | phone(uk)|
|-----------|-----------|---------|----------|-----------|----------|
|     1     |   brij007 |   35    |  rjt     |  tops     |9154545544|
|     2     |   anil007 |   35    |  rjt     |  tops     |9312121211|
|     3     |   anshu007|   25    |  rjt     |  tops     |6010212121|     


**SQL provides UK**

```
alter table users add unique(`uname`);
or 
alter table users add unique(`phone`);

```    

## forign key ?
1. a fk provide more than one time in tables
2. a fk key repetad more than one time in a table
3. a fk store duplicate value also
4. a fk provides relationship b/w table with common field 

**country**
|cid    |       cname   |
|-------|---------------|
|  1    | india         |
|  2    | usa           |
|  3    | australia     |
|  4    | china         |
|  5    | pakistan      |
|  6    | srilanka      |
|  7    | bhutan        |

**via sql**

```sql
create table tbl_country
(
cid int auto_increment primary key,
cname varchar(255)
)

```

**tbl_users**
|  uid(pk)  |  uname(uk) |  age    | address  | company   | phone(uk)|  cid(fk) |
|-----------|------------|---------|----------|-----------|----------|----------|   
|     1     |   brij007  |   35    |  rjt     |  tops     |9154545544|  1       |
|     2     |   anil007  |   35    |  rjt     |  tops     |9312121211|  2       |
|     3     |   anshu007 |   25    |  rjt     |  tops     |6010212121|  3       |


**SQL provides fK**

```sql
create table tbl_users
(
uid int AUTO_INCREMENT primary key,
uname varchar(255),
age int,
phone bigint,
company varchar(255),
address text,
cid int REFERENCES tbl_country(cid)    
)
```
## case based primary key and foreign key queries and create tables 

# Case 1: Student and Department

- Consider the following tables:

```sql
CREATE TABLE Department (
Dept_ID INT PRIMARY KEY auto_increment,
Dept_Name VARCHAR(50)
);
```

```sql
CREATE TABLE Student (
Student_ID INT PRIMARY KEY auto_increment,
Student_Name VARCHAR(50),
Dept_ID INT,
FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID)
);
```
1. Identify the primary key in the Department table.
2. Identify the primary key in the Student table.
3. Identify the foreign key in the Student table.
3. Which column connects the Student and Department tables?
4. Can two students have the same Student_ID?
5. Can Dept_ID in Student contain a value that does not exist in Department?
6. Write a query to display student names along with their department names.
7. Write a query to display all students belonging to the Computer Science department.
8. Write a query to find the number of students in each department.
9. Write a query to display departments that have no students.


**Anwer following question 1 to 5 is done**
**answer 6 to 9 via query and SQL join**
**6**
```sql
select student_name , dpet_id from student  
```
# distinct:

1. remove duplicate rows in data

**syntax**
```sql
select distinct databasename from colamname ;
```
or
```sql 
select distinct resturant from foodorder ;
``` 

# what is SQL string functions ?
 1. SQL string function are work with 'string' or character
 2. SQL string function are work with 'name', 'email', 'password' etc

**types of string function in SQL**

 1. UPPER()
 2. LOWER()
 3. CONCATE()
 4. length()
 5. trim()
 6. replace()
 7. right()
 8. left()

 1. select upper (name) from tbl_employee 
 2. select lower (name) from tbl_employee 
 3. select concate(name ,",",age) from tbl_employee  **marge column**
 4. select length (name) from tbl_employee **count space and start with 1**
 5. select trim(name) from tbl_employee **remove wide space**
 6. select replace ("om","om","tejas") from tbl_employee **reeplace all**
 6. select replace ("om","om","tejas") from tbl_employee where name= om **relace only name**
 7. select right (name,5) from tbl_employee 
 8. select left (name,5) from tbl_employee **extract some character left side**

# export data of sSQL in csv | excel |



# what is SQL like operator ?

1. like is an opertor in  
 
# what Normalization in SQL ?
1. normlization is use to normlised table with pk|uk|fk\
2. normlistion is removed the duplicate of data in table

#

# what is SQL SQL key constraints ?
1. key constrain is used to set limits on table


# what is SQL join  ?


# what is SQL Case In ?


# what is SQL windows function  ?


# what is SQL index or indexer ?


# what is SQL view  ?


# what is SQL trigger ?


# what is SQL store procedure ?

# what is SQL CTE ?


