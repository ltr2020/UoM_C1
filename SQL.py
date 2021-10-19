DB Function
- SUM(), AVG(), MIN(), MAX()
- ROUND(), LENGTH(), uCASE(), LCASE
- YEAR(), MONTH(), DAY(), DAYOFMONTH(), DAYOFWEEK(), DAYOFYEAR(), WEEK(), HOUR(), MINUTE(), SECOND()

Overcome limitations of agg func by sub-queries and nested selects

Sub-queries & nested selects    # can be used when multi tables
SELECT EMP_ID, F_NAME, L_NAME, SALARY
FROM employees
WHERE SALARY < (select AVG(SALARY)  #here
                from employees);

SELECT EMP_ID, SALARY, (select MAX(SALARY) FROM employees ) AS MAX_SALARY  #here
FROM employees;

select * from employees where JOB_ID <talbe1> IN (select JOB_IDENT from jobs <table2> where JOB_TITLE= 'Jr. Designer');

Multitables with implicit join
SELECT * FROM <table1> A, <table2> B
WHERE <A.column1> = <B.column2>;    #A, B are short aliases for faster input, can use whole name


Pros of using Cloud DB
# - ease of use, users can access Cloud databases from virtually anywhere using a vendor's API or web interface
# - Scalability. Cloud databases can expand and shrink their storage and compute capacities during runtime to accommodate changing needs and usage demands, so organizations only pay for what they actually use
# - Disaster recovery. In the event of a natural disaster or equipment failure or power outage, data is kept secure through backups on Remote Servers on Cloud in geographically distributed regions


Data Manipulation Language (DML) statements are used to read and modify data in tables. These are also sometimes referred to as CRUD operations,
that is, Create, Read, Update and Delete rows in a table. Common DML statement types include INSERT, SELECT, UPDATE, and DELETE

SELECT *(all) / column1, column2,
FROM table_name

WHERE <COL> e.g. LIKE "A%" / Range / ... or ... equivalent to <COL> in ("value", "value")#String pattern, returns when <COL> starts with A
# NOT LIKE
# "%A% anywhere in <COL>
# "__A%" starts with 3rd position
# can't use agg function in WHERE clause

sub-queries to evaluate agg func


ORDER BY <COL1> DESC, <COL2> #ordered in descending order by <COL1> & within order by <COL2> in ASEC
# can use number 1, 2, 3 to specify which col if multiple col called

GROUP BY <COL>
SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID;

HAVING <PREDICATE> #ONLY WORKS FOR GROUP BY, unlike where clause works for whole result set

COUNT()
SELECT COUNT(*) from FilmLocations where ReleaseYear < 1950;

DISTINCT    #retrieve unique value
SELECT COUNT(DISTINCT ReleaseYear) FROM FilmLocations WHERE ProductionCompany="Warner Bros. Pictures";

LIMIT #similar to .head()
SELECT * FROM FilmLocations LIMIT 15 OFFSET 10; #retrieve first 15 rows starting from 11th row

INSERT INTO <tablename> VALUES
("xx" , "XX", ...),    #first row
("xx", "XX", ...), ...    #2nd row

UPDATE <Table>  #change variable
SET <Column = "xx">, ...
WHERE <Predicate>

DELETE from <Table> WHERE <Predicate>



Data Definition Language (DDL) statements are used to define, change, or drop database objects such as tables
Common DDL statement types include CREATE, ALTER, TRUNCATE, and DROP

CREATE
CREATE TABLE Student(Name VARCHAR(20) PRIMARY KEY NOT NULL,
                    Gender CHAR(6)); # Primary Keys  constraint uniquely identifies each record in a table, can help speed up your queries significantly
INSERT into Student VALUES('Herry', 'Male');
INSERT into Student VALUES('Mahi', 'Female');
SELECT LENGTH(Name) FROM Student;

# VAR() used when data values is of fixed length(size), if less than fixed length padded with extra memory space
# varchar(60) used when data values is of var length(size), w/o padded extra space, performance not as good as CHAR()

ALTER #change str of existing table e.g. add, modify, drop

ALTER <table>
ADD <column> <dtype> column_constraint;     #ADD COLUMN

#then add in new data
UPDATE <table> SET <column=xx> WHERE <predicate>

ALTER <table>
DROP <column>;    #del col

ALTER <table>
ALTER <column> SET <dtype>;   #alter col dtype

ALTER <table>
RENAME <column> current_column_name TO new_column_name;   #rename col name


DROP <table>
# del all data and table

TRUNCATE <table>
    IMMEDIATE:\;
# del all data but keep table


DB-API
Python lib for different DB systems
IBM Db2: ibm_db
MySQL: MySQL Connector/Python
PostgreSQL: psycopg2
MongoDB: PyMongo

Connection Objects for DB connections and Manage transaction
Connecton = connect("db_name", "userid","pwd")


Cursor Objects for DB queries, scroll thru result set and retrieve results
Cursor = Connection.cursor()
Connection.commit()
Connection.rollback()
Connection.close()

Cursor.callproc()
CUrsor.execute("select * from <table>")
.executemany()
.fetchone()
.fetchmany()
Results = Cursor.fetchall()
.nextset()
.arraysize()
Cursor.close()

port": 30367
"database": "bludb"
"hostname": "815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
"password": "juFr8vgUo7ILSTyg",
"username": "ylg89839"