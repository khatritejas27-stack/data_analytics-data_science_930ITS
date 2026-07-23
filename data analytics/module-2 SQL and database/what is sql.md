#what is sql?
1. SQL stand for structure query langage
2. SQL is used to create database and table structure 
3. SQL is used as a structure query langage and it is create an
structure of database and table or structure type of data
 **table strutre**
 **user**
|uid| uname| gender | address|
|---|------|-------|--------|
| 1 | A     | male | rjt    |
| 2 | B     | female | rjt  |

4.Sql is case-insesative languge
 example :INSERT |insert| Insert (camlae case)
5.SQL is not conditional
6.SQL is used to provides relation between table using Normalition
7. SQL create some query or commands to create database or table structure

 ## sql type od Query or command
 1.DDL : **data defination language**
 2.DML : **data manipulation language**
 3.DQL : **data query language**
 4.TCL : **transation controle language**
 
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
  |  id (pk) auto_incremnts|  int (default size 11) |
  | name ,eamial ,password | char ,varchar (0-255)  |
  | date ,datetime         | date,date time(default)|
  | address , massage      | text                   |
  | multiple chioce        | enum                   |
  | photo, image           | blob ,varchar(255)     |
  | salary ,price (dacimal)| int ,float ,money      |
  | phone                  | int , bigInt(20)       |
  | defaul datetime        | timestamp              |

**syntax **
create table tablename
(
    id int auto_increment primary key,
    columname datatype(size),
    .
    .
    .
    columnname data type
)


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

