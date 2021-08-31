+ https://docs.python.org/3/에서 문서 참고가능.<br>

## 1. LIST_new data type(목록)<br>
+ (Metaphor) 짐이 많으면 가구골라서 정리하는 것과 비슷한 개념 <br>
+ CONTAINER <br>
+ 대괄호[] 안 : index <br>

`s = [1, 'four', 9, 16, 25]` #여기 안에 있는 건 원소 <br>
`print(s)` #1, 'four', 9, 16, 25 <br>
`print(s[1])` #four <br>
`print(len(s))` #5 <br>
`s[1] = 4` #원소 수정 <br>
`print(s)` #1, 4, 9, 16, 25 <br>
`del s[2]` #list delete by index <br>
`print(s)` #1,4, 16, 25 <br>
`s.append('hyeonah')` #list add <br>
`print(s)` #1,4, 16, 25, hyeonah <br>



## 2. common sequence operation <br>
+ list(Sequence Type)와 str(Text Sequence Type)은 공통적으로 sequednce operation <br>
+ list와 str 비교 <br>
+ list
```
s = [1, 'four', 9, 16, 25] 
print(s) #1, 'four', 9, 16, 25
print(s[1]) #four
print(len(s)) #5
s[1] = 4 
del s[2]
print(s) #1,4, 16, 25
```

+ string
```
a = '1, four, 9, 16, 25'
print(a) #1, four, 9, 16, 25
print(a[1]) #,
print(len(a)) #18
a[1] = 4 #오류
del a[2] #오류
```

: _즉, list와 str 모두 sequence operation이지만, str은 텍스트이기 때문에 n번째 원소를 다른 값으로 바꾸거나 삭제 불가._
    
## 3. other container_dict(Mapping Types)<br>
```
person = {'name':'hyeonah', 'address':'seoul'}
person['name'] #hyeonah.
```


## 3. LOOP_반복문 <br>
+ 반복문 `for`의 문법 <br>
```
>>> family = ['mother', 'father', 'gentleman', 'baby']
>>> for x in family:        # family의 각 항목 x에 대하여:
...     print(x, len(x))    # x와 x의 길이를 출력하라.
```
답은 아래와 같이.
```
mother 6
father 6
gentleman 9
baby 4
```
+ range()
: 어떤 정수를 인자로 주면 그 범위 안의 정수들을 만들어줌.
```
>>> list(range(2, 7))   #파이썬 3 
>>> range(2, 7)         #파이썬 2
```
답은 아래와 같이.
```
[2, 3, 4, 5, 6] #2 이상 7 미만인 숫자로 리스트를 만들어 줌.
```

+ for 문에 range()를 사용
< 사용한 예제 명시 >
```
>>> a = [4, 5, 6, 7]
>>> for i in a:
...     print(i)
```
답은 아래와 같이. 
```
4
5
6
7
```
< 위의 예시를 for과 range 사용 >
```
>>> for i in range(4, 8):
...     print(i)
```

+ if 문: compound statement
+ []안의 것을 계속 value에 대입.<br>
```
for value in ['a','b','c']:
    print(value)
#range
for value in range(10):
    print(value)
```

#while statement.<br>


5. 활용<br>
#python3 file list in directory<br>
#listdir<br>

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

6. form 사용.<br>
#url qurey string을 만드는 것<br>
```
input
textarea
```
`<form>`과 `</form>`으로 감싸기<br>
#사용자가 데이터입력이나 수정할 수 없도록 하는 법=query string 있으면 안된다.<br>


<list>
list((4, 5, 5)) #[4, 5, 5]
