# SQL join
+ 관계형 데이터베이스의 join
# 1. 표 쪼개기
+ 정보가 중복되기 시작하면 분가(쪼개기)가 필요함.
+ 쓰기가 좋음: 표 쪼개서, 읽기가 좋음: 한 표에 한꺼번에
# 2. LEFT join
+ left join은 기준이 되는 표를 왼쪽에 두고, 이 표를 기준으로 오른쪽의 표를 합성해서 하나의 표를 만드는 방법
+ `SELECT * FROM topic `
+ `SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.aid`
+ 양 쪽에만 있는 표를 출력+왼쪽만 있는 정도도 출력
+ OUTER JOIN은 조인 USING, ON 조건절을 필수적으로 사용해야 한다.<br>
(출처: https://haenny.tistory.com/34 [Haenny])
# 3. INNER join
+ 양 쪽에만 있는 표를 출력
# 4. FULL join
# 5. EXCLUSIVE join
