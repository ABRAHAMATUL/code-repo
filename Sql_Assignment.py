import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="atulambat",
  database="tataelxsi"
)

mycursor = mydb.cursor()


mycursor.execute("DROP TABLE employee")
mycursor.execute("DROP TABLE department")
mycursor.execute("DROP TABLE project")

mycursor.execute("CREATE TABLE employee (employee_no int PRIMARY KEY,f_name VARCHAR(255), l_name VARCHAR(255),enter_date date,job varchar(200),dept_no int,project_no int)")

mycursor.execute("CREATE TABLE department (dept_no int PRIMARY KEY,dept_name VARCHAR(255), loc VARCHAR(255))")

mycursor.execute("CREATE TABLE project (project_no int PRIMARY KEY,prj_name VARCHAR(255), budget int)")


#inserting values for employee table
mycursor.execute("insert into employee values(2000,'AKASH','SINHA','2017-5-7','ENGINEER',100,20)")
mycursor.execute("insert into employee values(2001,'BOFFIN','SURESH','2016-1-8','MBD ENGINEER',101,21)")
mycursor.execute("insert into employee values(2002,'GOVIND','S R','2015-2-9','ENGINEER',100,23)")
mycursor.execute("insert into employee values(2003,'AKSHAY','KRISHNAN','2018-2-17','MANAGER',102,24)")
mycursor.execute("insert into employee values(2004,'ADARSH','BENOY','2018-7-19','LEAD',104,24)")
mycursor.execute("insert into employee values(2005,'JERRIN','GEORGE','2014-5-20','ENGINEER',103,22)")
mycursor.execute("insert into employee values(2006,'SUDHEESH','SINHA','2019-3-31','SENIOR ENGINEER',102,22)")
mycursor.execute("insert into employee values(2007,'HARI','MOHAN','2013-8-30','AUTOSAR ENGINEER',104,21)")
mycursor.execute("insert into employee values(2008,'MOHANLAL','ETTAN','2018-10-10','SPECIALIST',101,20)")
mycursor.execute("insert into employee values(2009,'MAMOOTTY','ACTOR','2015-11-7','HEAD',102,21)")
mycursor.execute("insert into employee values(2010,'AISWARYA','LAKSHMI','2015-12-3','ENGINEER',104,21)")

#inserting values for department
mycursor.execute("insert into department values(100,'ABU','BANGALORE')")
mycursor.execute("insert into department values(101,'TBU','TRIVANDRUM')")
mycursor.execute("insert into department values(102,'BBU','PUNE')")
mycursor.execute("insert into department values(103,'SBU','CHENNAI')")
mycursor.execute("insert into department values(104,'RBU','TRIVANDRUM')")

#inserting values for project
mycursor.execute("insert into project values(20,'AUTOMATION',100000)")
mycursor.execute("insert into project values(21,'RPI',20000)")
mycursor.execute("insert into project values(22,'STEERING',389933)")
mycursor.execute("insert into project values(23,'DOCS',400000)")
mycursor.execute("insert into project values(24,'MANAGEMENT',50000)")


print('EMPLOYEES WHO ARE WORKING IN BANGALORE')
mycursor.execute("select f_name,l_name from employee where dept_no = (select dept_no from department where loc = 'BANGALORE')")
for x in mycursor:
  print(x)
print('COUNT OF EMPLOYEES WHO ARE WORKING IN BANGALORE')
mycursor.execute("select COUNT(f_name) from employee where dept_no = (select dept_no from department where loc = 'BANGALORE')")
for x in mycursor:
  print(x)


