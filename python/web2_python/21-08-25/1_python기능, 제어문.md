### Python 기능
#### 1. Python은 서로 같은 블럭에 속하는 코드를 같은 들여쓰기로 구분하는 중요한 특징이 있음. <br>
  ```
user_input = input('password?')
if user_input == '111111':
    print('Helllo master')
else:
    print('Who are you?')
  ```
  
#### 2. '''은 문자화 시키는 것으로, 실행되지 않음. <br>
```
'''
if user_pwd == '111111':
    print('Helllo master')
else:
    print('Who are you?')
'''
```

### 수업활용 자료: conditioanl.py활용_id까지 물어보는 거 <br>
```
user_id =  input('id?')
user_pwd = input('password?')
if user_id == 'hyeonah':
    if user_pwd == '111111':
        print('Hello master')
    else:
        print('Who are you?')
else:
    print('Who are you?')
```
- - -

## 1. 제어문 <br>
+ program->순서대로 컴퓨터가 실행하도록 하는 것.<br>
+ 순서대로>제어문>반복문/조건문<br>
+ 활용 <br>
: id가 없는 경우(Web클릭)-> welcome이 나오도록 index_no_id.py추가로 만들어서 진행_2개의 application만들어서 해결<br>
: index_no_id.py에 pageId를 Welcome으로 박제<br>
+ index_no_id.py <br>
```
import cgi  
pageId = 'Welcome'  
print('''<!doctype html>  
<html>  
<head>  
  <title>WEB1 - Welcome</title>  
  <meta charset="utf-8">  
</head>  
<body>  
  <h1><a href="index_no_id.py">WEB</a></h1>  
  <ol>  
    <li><a href="index.py?id=HTML">HTML</a></li>  
    <li><a href="index.py?id=CSS">CSS</a></li>  
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>  
```
+ index_no_id.py를 넣은 index.py <br>
```
import cgi  
form = cgi.FieldStorage()  
pageId = form["id"].value  
print('''<!doctype html>  
<html>  
<head>  
  <title>WEB1 - Welcome</title>  
  <meta charset="utf-8">  
</head>  
<body>  
  <h1><a href="index_no_id.py">WEB</a></h1>  
  <ol>  
    <li><a href="index.py?id=HTML">HTML</a></li>  
    <li><a href="index.py?id=CSS">CSS</a></li>  
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>  
```
: _간단하게 해결할 수 있지만, 스크립트 수정시, 2개의 파일을 수정해야 하는 번거로움 -> 조건문 사용._<br>


## 2. data types<br>
  1) number(숫자열) #무한 <br>
`print(1)` #Integer <br>
  2) string(문자열) #유한 <br>
`print('Hello world')`<br>
  3) Boolean #단 2개의 데이터로 구성 #논리 <br>
`print(True)` #참 <br>
`print(False)` #거짓 <br>

## 3. Expression <br>
+ 좌항과 우항을 합쳐서 하나로 <br>
`print(1+1)` #2 <br>
`print('Hello '+'world')` #Hello world <br>

## 4. Comparison operator <Br>
+ 비교연산 <br> 
+ Boolean결과값 <br>
`print(1==1)` #True <br>
`print(1<2)` #True <br>
`print(2<1)` #False <br>

## 5. Membership operator 
+ 뒤에 있는 값에 앞에 있는 값이 포함되어 있는가? <br>
`print('world' in 'Hello world')`  #True #world가 helloworld안에 있는가? <br>

+ python3 check exist file in directory <br>
```
import os.path
print(os.path.exists('boolean.py')) #True
print(os.path.exists('boolean2.py')) #False
```

## 6. 조건문(Conditional Statement) <br>
+ 조건문 형식 <br>
```
if xxx(boolean datatype) :
    yyy
```
+ if문에 추가로 조건 생성 <br>
+ elif(else if) <br>
: 잘 안됨 --> 해결 --> 위의 코드를 주석처리하고 진행해야 원하는 값을 얻을 수 있음. <br>
```
if user_id == 'hyeonah' and user_pwd == '111111':
        print('Hello master')
    elif user_id == 'tomato' and user_pwd == '234':
        print('Hello master')
else:
    print('Who are you?')
```
+ id와 pwd를 모두 물어보고 나서야 'Who are you?'를 물어보는게 아니라, id가 틀리면 바로 'Who are you?'를 묻고록 하는 코드
```
user_id =  input('id?')
if user_id == 'hyeonah':
    user_pwd = input('password?')
    if user_pwd == '111111':
        print('Hello master')
    else:
        print('Who are you?')
else:
    print('Who are you?')
```
## 7. 논리 연산자(Logical operator) <br>
    1) and-> 왼쪽과 오른 쪽의 값이 같은지 다른지에 따라 true Or false 
`True and False` #False <br>
`True and True` #True <br>
  
    2) or-> 왼쪽과 오른쪽 값 중에서 하나만 true여도 true임. 
`True or False` #True <br>
`False or False` #False <br>
`True or True` #True <br>
   
    3) not-> 반대를 만듦. 
`not True` #False <br>
`not False` #True <br>
  

