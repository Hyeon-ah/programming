# Oracle
관계형데이터베이스(Relational Database)_Oracle_ <br>
ORACLE은 유료, 무료가 있음.

## 1. ORACLE 설치 및 접속
+ `sys AS SYSDBA`입력해 접속
+ 접속 방법
  - `sqlplus` -> 사용자 명:`sys AS SYSDBA`
## 2. User와 Schema의 개념
database=표들을 grouping한 것 = schema(서로 연관된 데이터를 그룹핑한 폴더)
+ SCHEMA: 서로 연관된 표들을 grouping하는 directory
  - SCHEMA의 본질적인 정의: SCHEMA에 속하는 표들을 정의하는 정보 
+ USER(사용자): SCHEMA를 사용 (단, Schema != User)
  - ORACLE이 USER 생성 -> 각 USER에 해당하는 SCHEMA 생성 -> 각 USER는 자신이 관리하는 table에 접속 가능

## 3. USER(사용자)생성
'hyeonah'라는 USER 생성 = 'hyeonah'라는 SCHEMA가 생성되었다는 뜻

## 4.사용자 권한 부여
`GRANT DBA TO hyeonah;` <br>
최소한의 권한만 주기  <br>
  - DBA는 최대한의 권한

## 5. table 생성
+ `commit;`해야 함.
```
테이블 개요 보기 : SELECT * FROM 테이블 ;
만들어진 테이블에 행 추가하기:
INSERT INTO 테이블 (칼럼1,칼럼2 ...)
VALUES(추가할 값) ;

CF) 행 삭제 :
DELETE FROM 테이블
WHERE 조건 ; # 조건 만족하는 행 삭제

CF) talbe 삭제 :
DROP TABLE 테이블 ;

행 수정:
UPDATE 테이블
SET 변경할 조건
WHERE 원래 조건 ;

행 조회 :
SELECT * FROM 테이블 WHERE 조건 :
```

## 6. SQL 이란?
 = Structured Query Language, 관계형 데이터베이스에서 SQL 사용. <br>
명령어를 통해 database 제어할 수 있다. -> 자동화

## 7. Server와 clinet
+ 인터넷에 연결된 컴퓨터 한대 한대를 host라고 함
+ 정보 요청=client
+ 정보 제공=server
+ sqlplus/TOAD/SQL DEVELOPER(clients) > oracle server
+ gui 형식=sql developer

## 8. SQL developer

# 실습
## 1. SELECT 행 읽기
+ 모든 행 읽기
    - `SELECT * FROM topic;`
+ 행과 칼런 제한하기
    -  `SELECT id, title FROM topic;`
    - `SELECT * FROM topic WHERE id = 1;`
    - `SELECT id, title FROM topic;`
+ 정렬
    - `SELECT * FROM topic ORDER BY id DESC;`
+ 페이징(데이터 부분부분만 가져오기)
    - `SELECT * FROM topic OFFSET 1 ROWS;` 
    -  OFFSET N: 어디부터 가져올지 <br>
        - OFFSET 1: 0번째 이후의 행(=1번째 행부터) <br>
        - OFFSET 2: 1번째 이후의 행(=2번째 행부터) <br>
    - `SELECT * FROM topic OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY;` <br>
        - 0번째 이후 행 1개만 가져옴. <br>
    - `SELECT * FROM topic OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY;` <br>
        - 1번째 이후 행 1개만 가져옴. <br>

## 2. UPDATE 행 수정
+ `UPDATE topic SET title = 'MSSQL', description = 'MSSQL is ...' WHERE id = 3;`
+ WHERE 꼭 넣어주어야 함!

## 3. DELETE 행 삭제
+ `DELETE FROM topic WHERE id=3;`

## 4. PRIMARY KEY
+ 중복되면 안된다! 유일무이
+ 테이블 생성시 설정 OR 생성후 `ALTER` 명령어 사용해 설정 가능
```
 CREATE TABLE topic (
    id NUMBER NOT NULL, 
    title VARCHAR2(50) NOT NULL, 
    description VARCHAR2(4000), 
    created DATE NOT NULL,
    CONSTRAINT PK_TOPIC PRIMARY KEY(id)
);
```

## 5. SEQUENCE
+ PRIMARY KEY는  sequence와 family!
+ SEQUENCE 생성
   `CREATE SEQUENCE SEQ_TOPIC;`
```
INSERT INTO topic (id, title, description, created)
VALUES(SEQ_TOPIC.NEXTVAL,'ORACLE','ORACLE is ...', SYSDATE);

INSERT INTO topic (id, title, description, created)
VALUES(SEQ_TOPIC.NEXTVAL, 'MySQL','MySQL is ...', SYSDATE);

INSERT INTO topic (id, title, description, created)
VALUES(SEQ_TOPIC.NEXTVAL,'SQL Server','SQL Server is ...', SYSDATE);

INSERT INTO topic (id, title, description, created)
VALUES(SEQ_TOPIC.NEXTVAL,'MongoDB','MongoDB is ...', SYSDATE);
```
+ SEQUENCE의 현재를 반환
  - `SELECT SEQ_TOPIC.CURRVAL FROM topic;` # sequence의 현재 
  - `SELECT SEQ_TOPIC.CURRVAL FROM DUAL;` # sequence의 현재를 1개만 반환.

## 6. 테이블 분해/조립
+ MySQL과 동일

## Cf) 연속된 수의 합
```
WITH CONTINUOUS(NUM, RESULT) AS
  (
  SELECT 1,1 FROM DUAL
  UNION ALL
  SELECT
  NUM+1, (NUM+1) + RESULT
  FROM CONTINUOUS
  WHERE NUM < 9
  )
SELECT NUM, RESULT
FROM CONTINUOUS;
```
