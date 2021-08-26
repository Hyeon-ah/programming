https://docs.python.org/3/에서 문서 참고가능.

1. new data type_LIST(목록)
- 짐이 많으면 가구골라서 정리하는 것과 비슷한 개념.
- 컨테이너
- 대괄호[] 안:index
```
s = [1, 'four', 9, 16, 25] #여기 안에 있는 건 원
print(s) #1, 'four', 9, 16, 25
print(s[1]) #four
print(len(s)) #5
s[1] = 4 #원소 수정
print(s) #1, 4, 9, 16, 25
#list delete by index
del s[2]
print(s) #1,4, 16, 25
#list add
s.append('hyeonah')
print(s) ##1,4, 16, 25, hyeonah
```


2. common sequence operation
list(Sequence Type)와 str(Text Sequence Type)은 공통적으로 sequednce operation.

3. other container_dict(Mapping Types)
person = {'name':'hyeonah', 'address':'seoul'}
person['name'] #hyeonah.

4. 반복문_LOOP
반복문 for의 문법
(if 문: compound statement)

#[]안의 것을 계속 value에 대입.
```
for value in ['a','b','c']:
    print(value)
#range
for value in range(10):
    print(value)
```

#while statement.


5. 활용
#python3 file list in directory
#listdir

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

6. form 사용.
#url qurey string을 만드는 것

input
textarea
<form>과 </form>으로 감싸기
#사용자가 데이터입력이나 수정할 수 없도록 하는 법=query string 있으면 안된다.

