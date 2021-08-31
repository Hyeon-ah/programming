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
<list>
```
s = [1, 'four', 9, 16, 25] 
print(s) #1, 'four', 9, 16, 25
print(s[1]) #four
print(len(s)) #5
s[1] = 4 
del s[2]
print(s) #1,4, 16, 25
```

<str>
```
a = '1, four, 9, 16, 25'
print(a) #1, four, 9, 16, 25
print(a[1]) #,
print(len(a)) #18
a[1] = 4 #오류
del a[2] #오류
```

: 즉, list와 str 모두 sequence operation이지만, str은 텍스트이기 때문에 n번째 원소를 다른 값으로 바꾸거나 삭제 불가.
    
## 3. other container_dict(Mapping Types)<br>
```
person = {'name':'hyeonah', 'address':'seoul'}
person['name'] #hyeonah.
```


4. 반복문_LOOP<br>
반복문 for의 문법<br>
(if 문: compound statement)

#[]안의 것을 계속 value에 대입.<br>
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
