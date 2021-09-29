## 1. Module(모듈) = 부품
+ 함수는 부품으로서 중요한 역할을 함.
+ 함수가 커지면서 편리하게 하기 위해 존재.
+ 양이 많아지면서 일어날 불편함을 해결.
+ 비유: 학교의 학급 & 컴퓨터의 directory-성격이 비슷한 파일을 하나의 폴더로 모으는 것.
## 2. 내부 모듈
+ 
```import math
print(math.ceil(2.1)) #2.1보다 더 큰 정수
print(math.floor(2.9)) # 2
print(math.sqrt(16)) # 4.0
```
+ math라는 directory안에 ceil, floor, sqrt가 저장되어 있는 꼴
+ https://docs.python.org/3/library/math.html

## 3. ruby
```
puts(Math.sqrt(16)) # 4.0
```

## 4. 모듈 없을 떄
+경우1)-중간에 다른 사람이 코드 넣어버리면 값이 바뀌어 버림ㅜ
```
def a():
    return 'a'
# 엄청 많은 코드
def a():
    return 'B'
# 엄청 많은 코드
print(a())
```
+ 경우2)-함수의 이름에 자신의 이름 넣어서 분별하면 됨!
```
def hyeon_a():
    return 'a'
# 엄청 많은 코드
def ah_a():
    return 'B'
# 엄청 많은 코드
print(a())
```
그러나 모듈을 이용하면 더 용이함.
