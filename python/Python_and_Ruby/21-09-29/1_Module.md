## 1. Module(모듈) = 부품
+ 함수는 부품으로서 중요한 역할을 함.
+ 함수가 커지면서 편리하게 하기 위해 존재.
+ 양이 많아지면서 일어날 불편함을 해결.
+ 비유: 학교의 학급 & 컴퓨터의 directory-성격이 비슷한 파일을 하나의 폴더로 모으는 것.
## 2. 내부 모듈
+ ex) `math`라는 모듈 import
```import math
print(math.ceil(2.1)) #2.1보다 더 큰 정수
print(math.floor(2.9)) # 2
print(math.sqrt(16)) # 4.0
```
+ math라는 directory안에 ceil, floor, sqrt가 저장되어 있는 꼴
+ https://docs.python.org/3/library/math.html

## 번외)- ruby
```
puts(Math.sqrt(16)) # 4.0
```

## 3. 모듈 없을 때
+ 경우1)-중간에 다른 사람이 코드 넣어버리면 값이 바뀌어 버림ㅜ
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

## 4-1. 모듈의 도입(Python)
+ 각각의 함수를 각각의 파일로 분리_hyeon.py & ah.py
+ 1) hyeon.py
```
def a():
    return 'a'
def b():
    return 'b'
def c():
    return 'c'
```
+ 2) ah.py
```
def a():
    return 'B'
```
+ import module/function
```
import hyeon 
import ah 
print(hyeon.a()) # a
print(ah.a())  # B
```
+ fom ~ import ~
```
from hyeon import a # hyeon이라는 module로 부터 a라는 함수를 가져옴.
import ah 
print(a()) # a # hyeon이라는 module을 표시 x. -> a 라는 이름으로 a라는 함수를 가리킬 수 있게 됨.
print(ah.a()) # B
```
+ `함수` 이름, `모듈` 이름 변경
```
from hyeon import a as z # hyeon 모듈의 a 함수를 z로 이름 변경
import ah as k # ah 모듈을 모듈 k 로 이름 변경
print(z()) # a # 바뀐 함수로 부르기
print(k.a()) # B # 바뀐 모듈로 부르기
```
+ 정리 
import만 있으면 module만 부르는 것. <br>
from이 있으면 모듈에서 특정 함수를 가져오는 것 <br>
즉, import가 가져오는 것이 함수 일수도 있고, 모듈일 수도 있다. <br>
