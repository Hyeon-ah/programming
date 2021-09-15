## 1. Module
Python의 모듈: 서로 연관된 변수와 함수 그리고 객체를 정리 정돈하는 도구


+ module.py에서 mathmatics라는 모듈을 가져오기.
+ mathmatics.py(각종 함수가 있음)
```
def average(a,b,c) :
    s=a+b+c
    r=s/3
    return r


def plus(a,b) :
    return a+b

pi = 3.14
```
+ module을 가져오는 법 
  1) mathmatics라는 module을 import
```
import mathmatics
#파일명과 일치 해야 함.

print(mathmatics.average(1,2,3))
print(mathmatics.plus(1,2))
print(mathmatics.pi)
```
  2) 각각의 함수를(average 등) import; mathmatics라는 module로 부터!
```
from mathmatics import average, plus, pi

print(average(1,2,3))
print(plus(1,2))
print(pi)
```

module보다 큰 가방=package!
