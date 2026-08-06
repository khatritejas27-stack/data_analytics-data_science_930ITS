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

  **example**
  '''
  create database da_db
  '''
  ## how to create table ?
  **create a table chart for datatype size**
  |       columname        |   datatype(size)       |
  |------------------------|------------------------| 
  | id (pk) auto_incremnts |  int (default size 11) |
  | name ,eamial ,password | char ,varchar (0-255)  |
  | date ,datetime         | date,date time(default)|
  | address , massage      | text                   |
  | multiple chioce        | enum                   |
  | photo, image           | blob ,varchar(255)     |
  | salary ,price (dacimal)| int ,float ,money      |
  | phone                  | int , bigInt(20)       |
  | defaul datetime        | timestamp              |

**syntax **
'''
create table tablename
(
  id int auto_increment primary key,
  columname datatype(size),
  .
  .
  .
  columnname data type
)
'''

example
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

# alter
1. alter is used to change tabel columname | add tabel new column alter is used 
2. alter is also update columname of tabel and also add unique key in tabel 
3. alter is used to change or update or modify tabel column name 

**syntax**
'''
alter tabel tabelname add columnname datatype(255)

or
alter tabel users add gender varchar(255)
''' 
 
# add columname specific column
 '''
 alter tabel user add photo varchar(255) after name;
 select tabel users add photo varchar(255) after name;
 '''
 

# update any specific columnname
 '''
 alter tabel user change phone mobile bigint;
 '''
## alter used to add unique key in tabels (unique key never store dublicate values)
**syntax**
'''
ALTER TABLE `employee` ADD UNIQUE (`email`);  
'''
# change is used in alter to change any columnname 
**syntax**
'''
 alter tabel user change phone mobile bigint;
'''
 # rename : rename is used to change a tabel name
 **syntax**
'''
rename tabel tablename  to  new table name;
or
rename tabel users to  tbl_users;
'''
# truncate : truncate is used to empty or delete all data at once time
 ## note : after truncate we never rollback our data
 '''
 truncate tabel  tbl_employee:
 '''
# drope : drope is used to drop or delete database  or tabel strutures
## note: after drop we never rollback
**syntax**
''''
drop database databasename; ,

drop table tabelname ;
'''


# crate product table
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

## DML..data manipulation language
**thare are Quary in DML**
1. insert 
1. delete
3. update  

# how to insert data 
** syntax **
**single data insert**
'''
insert into tablename(columname) value ('value')
or
INSERT into tbl_employee
value(null,'kumar',kumar@gmail,'8156514561','railnager',null,'male','5156156',null),           (null,'ramsh',rumash@gmail,'899999999','railnager',null,'male','821549',null);
or
INSERT into tbl_employee
colume(name,email,mobile,address,photo,gender,adhar card ,uid)
value('kumar',kumar@gmail,'8156514561','railnager',,'male','5156156',),           (null,'ramsh',rumash@gmail,'899999999','railnager',null,'male','821549',null);
'''

## delete data from tables
**syntax**
'''
delete all data
delte from tablename ;
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

'''
1.delete is used to delete all data from table
2.delete is used to delete particular data from table
3.delete is used to delete range of data from table 
4.delete is used to delete  altenate of data

# update the data or row
 **syntax**
'''
update table set columname='value' where id='id'
or
update table tbl_country set cname='bhutan' where cid=10;
'''