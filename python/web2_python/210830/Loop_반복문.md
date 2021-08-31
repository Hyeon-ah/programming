## LOOP_반복문 <br>
### 1. 반복문 `for`의 문법 <br>
```
>>> family = ['mother', 'father', 'gentleman', 'baby']
>>> for x in family:        # family의 각 항목 x에 대하여:
...     print(x, len(x))    # x와 x의 길이를 출력하라.
```
답은 아래와 같이. <br>
```
mother 6
father 6
gentleman 9
baby 4
```
### 2. range() <br>
: 어떤 정수를 인자로 주면 그 범위 안의 정수들을 만들어줌. <br>
```
>>> list(range(2, 7))   #파이썬 3 
>>> range(2, 7)         #파이썬 2
```
답은 아래와 같이. <br>
```
[2, 3, 4, 5, 6] #2 이상 7 미만인 숫자로 리스트를 만들어 줌.
```

### 3. `for` 문에 `range()`를 사용 <br>
< 사용한 예제 명시 > <br>
```
>>> a = [4, 5, 6, 7]
>>> for i in a:
...     print(i)
``` 
답은 아래와 같이. <br>
```
4
5
6
7
```
< 위의 예시를 `for`과 `range` 사용 > <br>
```
>>> for i in range(4, 8):
...     print(i)
```

### 4. if 문: compound statement <br>
+ []안의 것을 계속 value에 대입. <br>
```
for value in ['a','b','c']:
    print(value)
#range
for value in range(10):
    print(value)
```

### 5. while statement. <br> 
: While문 기본 구조 <br>
```
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
```

### 6. 응용 <br>
+ python3 file list in directory <br>
+ listdir <br>

```
#!python
print("Content-Type: text/html")
print()
import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))
```

### 7. form 사용.<br>
#url qurey string을 만드는 것<br>
```
input
textarea
```
`<form>`과 `</form>`으로 감싸기<br>
#사용자가 데이터입력이나 수정할 수 없도록 하는 법=query string 있으면 안된다.<br>
