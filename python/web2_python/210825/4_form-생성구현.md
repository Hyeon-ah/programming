## 1. 생성구현1_ form <br>
+ `<p></p>`는 줄바꿈을 해줌. <br>
+ form이란 사용자로터 정보를 입력받는 양식 <br>
+ `placeholder`는 글쓰기 전에 쓰여있는 글씨이고, `name`은 전송할때 적혀지는 것. <br>

```
#!python
print("Content-Type: text/html")
print()
import cgi, os

files = os.listdir('data')
print(files)
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

#한글깨짐오류        
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
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
  <a href="create.py">create</a>
  <p><input type="text" name="title" placeholder="title"></P> 
  <p><textarea> rows="4" name="description" placeholder="description"></textarea></p> 
  <p><input type="submit"></p> 
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))
```
+ form이 무엇인가? <br>
: form = url query string을 생성자 <br>
: url query string은 입력값 역할을 함. <br>
+ form은 어떻게 만드나? <br>
: `<form>`과 `</form>`으로 감싸기 <br>
+ 사용자가 데이터입력이나 수정할 수 없도록 하는 법=query string 있으면 안된다. <br>
: action, method 추가. -> 잘 안되었음 -> 스펠링 제대로 써야 함. <br>
```
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
  <a href="create.py">create</a>
  <form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="title"></P>
    <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))
```
## 2. 생성구현2_ 전송한 정보의 처리 <br>
+ 입력하여 submit한 값이 페이지에서 나타나도록 하는 것 <br>
+ create.py, process_create.py활용
```
#!python
print("Content-Type: text/html")
print()


import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

print(title, description)
```
+ html form을 활용하여 전송한 데이터를 Python 어플리케이션이 받아서 처리하는 방법
```
#!python



import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value
#print하는 건 없애줘야 함, 그렇지 않으면 header에 변화가 생겨버림.
'''
print(title, description)
'''
#title에 입력한 것이 data의 파일로 생성됨.
opened_file = open('data/'+title, 'w')
opened_file.write(description)

#Redirection
#웹서버가 웹브라우져에게 Location~으로 이동해!
print("Location: index.py?id"+title)
print()
```
