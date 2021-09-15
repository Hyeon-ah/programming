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
+ module을 가져오는 법 <br>
 1) mathmatics라는 module을 import <br>
```
#파일명과 일치 해야 함.
import mathmatics

#module import 하려면 앞에 모듈쓰고 `.` 
print(mathmatics.average(1,2,3))
print(mathmatics.plus(1,2))
print(mathmatics.pi)
```
2) 각각의 함수를(average 등) import; mathmatics라는 module로 부터! <br>
```
from mathmatics import average, plus, pi

print(average(1,2,3))
print(plus(1,2))
print(pi)
```

module보다 큰 가방=package!

## 2. Python의 함수를 파일로 분리해서 모듈화시키는 방법
+ 모듈을 모아 놓은 view.py를 만들기
+ view.py
```
#getList()함수는 os 모듈을 사용하고 있으니, we shoould import `os` primarily.
import os
def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr
```
+index.py, create.py, update.py에서... 
```
#def getList()부분 없애고, view import. 
import cgi, os, view

#fomat부분
'''.format(
    title=pageId,
    desc=description,
    listStr=view.getList(), #요부분 view.라고 적어서 import `view` module.
    update_link=update_link,
    delete_action=delete_action))
```
