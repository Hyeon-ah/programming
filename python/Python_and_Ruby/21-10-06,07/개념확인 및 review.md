## Review <br>
모듈 = 클래스의 경로 <br> 
from은 모듈의 경로알려줌. <br>
import는 (모듈안의)class를 함. <br>
모듈 > 클래스 > 함수 <br>
클래스 불러오는 거 = instance화 하는 것 <br>
+ factorial 
```
#for문
def fac(c):
    n = 1
    for i in range (1, c+1):
        n = n * i
    return(n)

print(fac(4)) #24

#while 문
def fact(c):
    num = 1
    while  c >= 1:
        num = num * c
        c = c - 1
    return num

fact(4) #24

# Factorial of a number using recursion
def factorialRecursion(n):
   if n == 1:
       return n
   else:
       return n*factorialRecursion(n-1)

factorialRecursion(5) #120
```
## 개념확인 
+ 객체 지향 <-> 절차 지향 <br>
+ 객체 지향 (OOP)
: 데이터와 절차를 하나로 생각. <br>
: 캡슐화(데이터와 코드가 하나의 묶음) <br>
/ 상속(이미 작성된 class 이어받기 때문에 코드 재사용) <br>
/ 다형성(동일한 작업을 하는 함수에 같은 이름 부여 가능 -> 코드 간결화) <br>
: 코드 재활용 o (장) <br>
: 처리속도 느림, 설계에 시간투자 많음. (단) <br>

+ 절차 지향(Procedural Programming
: 순차적인 처리가 중시 됨. (장) <br>
: 그래서 코드의 순서가 바뀌면 결과 보장 x (단) <br>
: 실행속도가 빠름 <br>

