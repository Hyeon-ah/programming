## 1. form <br>
+ <p></p>는 줄바꿈을 해줌. <br>
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
  <a href="creat.py">create</a>
  <p><input type="text" name="title" placeholder="title"></P> 
  <p><textarea> row="4" name="discription" placeholder="description"></textarea></p> 
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
: action, method 추가. <br>
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
  <a href="creat.py">create</a>
  <form action="process_creat.py" method="host">
    <p><input type="text" name="title" placeholder="title"></P>
    <p><textarea row="4" name="discription" placeholder="description"></textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))
```
