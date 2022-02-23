# SQL join
+ 관계형 데이터베이스의 join
+ 양 쪽에만 있는 표를 출력: INNER JOIN
+ 양 쪽에만 있는 표를 출력+왼쪽만 있는 정보도 출력: LEFT OUTER JOIN(LEFT JOIN)
  - RIGHT JOIN도 있으나, 많이 사용하지 않음. 방향이 바뀌었을 뿐 동작 방법은 똑같음.


## 1. 표 쪼개기
+ 정보가 중복되기 시작하면 분가(쪼개기)가 필요함.
+ 쓰기가 좋음: 표 쪼개서, 읽기가 좋음: 한 표에 한꺼번에

## 2. LEFT join
+ left join은 기준이 되는 표를 왼쪽에 두고, 이 표를 기준으로 오른쪽의 표를 합성해서 하나의 표를 만드는 방법
+ `SELECT * FROM topic `
+ `SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.aid`
+ `SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.aid LEFT JOIN profile ON author.profile_id = profile.pid;`
  - LEFT JOIN 여러개 할 수 있음
+ `SELECT tid, topic.title, author_id, name, profile.title AS job_title FROM topic LEFT JOIN author ON topic.author_id = author.aid LEFT JOIN profile ON author.profile_id = profile.pid;`
  - LEFT JOIN 여러개 할 수 있음 + 읽고싶은 열만 선택
+ `SELECT tid, topic.title, author_id, name, profile.title AS job_title FROM topic LEFT JOIN author ON topic.author_id = author.aid LEFT JOIN profile ON author.profile_id = profile.pid WHERE aid = 1;`
  - LEFT JOIN 여러개 할 수 있음 + 읽고싶은 열만 선택	+ WHERE을 가지고 특정 author만 읽을 수 있음																						

## 3. INNER join
+ 교집합
+ 양 쪽에만 있는 표를 출력
+ NULL 행이 존재하지 않게 됨!
+ `SELECT * FROM topic INNER JOIN author ON topic.author_id = author.aid;`
+ `SELECT * FROM topic INNER JOIN author ON topic.author_id = author.id INNER JOIN profile ON profile.pid = author.profile_id;`
  - INNET JOIN 여러개 가능
 
## 4. FULL OUTER JOIN
+ 합집합
+ LEFT JOIN, RIGHT JOIN 값 모두 가져와서 중복 없앰.
+ `SELECT * FROM topic FULL OUTER JOIN author ON topic.author_id = author.id;`
  - OUTER JOIN을 지원하지 않는 database의 경우가 있음.
+ `(SELECT * FROM topic LEFT JOIN author ON topic.author_id=author.aid) UNION (SELECT * FROM topic RIGHT JOIN author ON topic.author_id=author.aid);`			
  - UNION DISTINCT로 DISTINCT가 생략된 것
  - 중복은 제거함							

## 5. EXCLUSIVE join
+ 제외하는 것, 많이 사용하지는 않음.
+ `SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.aid WHERE author.aid is NULL;`
