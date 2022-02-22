# DATABASE2 - MySQL
+ 파일의 한계 극복-> 데이터 잘 정리할 수 있도록 -->> database 탄생
+ 관계형 데이터베이스(Relational Database) 사용하면?
  1) 데이터를 표의 형태로 정리 가능
  2) 정렬, 검색을 빠르고 안전하게
+ 관계형 데이터베이스의 종류?
  - MySQL, Oracle, SQL Server, PostgreSQL, DB2, Access
 

## 1. 데이터베이스의 목적
+ 엑셀과 아주 비슷
+ spread sheet vs database
  - spread sheet: 클릭클릭해서 데이터 조작
  - database: SQL이라는 컴퓨터 언어 이용해 데이터 조작(via 코드)
 
## 2. MySQL의 구조
+ 데이터 기록의 최종 = table(표)
+ database=표들을 grouping한 것 = schema(서로 연관된 데이터를 그룹핑한 폴더)
+ table > database(schema) > database server

## 3. database의 효용
1) 보안
  - 자체적인 보안체계 갖춤.
  - 권한 기능-> 차등적으로 여러 사람을 등록할 수 있음(CRUD 가능)

## 4. schema의 사용
+ 검색엔진 사용, 명령어 외울 필요 없음.
  - ex) database 만드는 법 <br>
```
MariaDB [(none)]> CREATE DATABASE opentutorials;
Query OK, 1 row affected (0.006 sec)

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| opentutorials      |
| performance_schema |
| test               |
+--------------------+
5 rows in set (0.024 sec)

MariaDB [(none)]> USE  opentutorials;
Database changed
MariaDB [opentutorials]>
```
+ `CREATE DATABASE opentutorials;`(opentutorials는 파일 이름) <BR>
+ `USE opentutorials;` --> 지금부터 하는 명령은 **opentutorials;**를 실행하게 됨.

## 5. SQL과 테이블의 구조
+ Structured Query Language
+ SQL 언어를 통해 MySQL Server에 요청하는 것.
+ SQL의 특징
  - 쉽다
  - 중요하다: 관계형 데이터베이스를 사용하는데 많이 사용됨.
+ 용어 정리
  - table, 표
  - x축: row, record,행 = **데이터 하나하나**
  - y축: column, 열 (수직으로 된 칸 하나하나) = **데이터 type, 종류**

## 6. table의 생성
+ column의 data type을 정할 수 있음
+ 표 생성의 몇 가지 명령어
  - NOT NULL: 값이 없는 것을 허용안함
  - AUTO_INCREMENT: 자동 숫자 증가
  - VANCHAR: 글자수 제한
  - PRIMARY KEY: 성능&중복 방지함, 각 행의 식별자로서 제일 중요한 KEY
+ 사용한 코드
```
MariaDB [opentutorials]>  CREATE TABLE topic(
    ->  id INT(11) NOT NULL AUTO_INCREMENT,
    ->  title VARCHAR(100) NOT NULL,
    ->  description TEXT NULL,
    ->  created DATETIME NOT NULL,
    ->  author VARCHAR(30) NULL,
    ->  profile VARCHAR(100) NULL,
    ->  PRIMARY KEY(id));
```
`SHOW TABLES;`<br>
`SHOW DATABASES;`<br> 
`DESC` 
  
## 7. CRUD
+ (**Create**, **Read**, Update, Delete)
+ WHERE문 꼭 넣기(데이터 망가질 수 있음.)
+ 매뉴얼의 `[]`는 생략가능. <br>
  
  1) INSERT
  + 데이터 생성
  + 사용한 코드 <br>
    (1) 데이터 입력 <br>
  `INSERT INTO topic (title,description,created,author,profile) VALUES('MongoDB','MongoDB is',NOW(),'egoing','developer');` <br>
    (2) 데이터 보기 <br>
  `SELECT * FROM topic;` <br>

  2) SELECT
  + 데이터 읽기
  + 사용한 코드 <br>
  `SELECT "egoing", 1+1;`
  `SELECT id, title, created, author FROM topic WHERE author="egoing" ORDER BY id DESC LIMIT 2;`
```
+----+---------+---------------------+--------+
| id | title   | created             | author |
+----+---------+---------------------+--------+
|  5 | MongoDB | 2022-02-21 14:55:39 | egoing |
|  2 | ORACLE  | 2022-02-21 14:51:57 | egoing |
+----+---------+---------------------+--------+
```

  3) UPDATE  
  + 데이터 추가 <br>
   `UPDATE topic SET author = "dura",description = 'SQL Server is ...'  WHERE id = 3;` 

  4) DELETE
  + 데이터 삭제 <br>
  ` DELETE FROM topic WHERE id = 5;`

## 8. 관계형데이터베이스의 필요성


  

  
