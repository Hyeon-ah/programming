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
```
input
textarea
`<form>`과 `</form>`으로 감싸기
#사용자가 데이터입력이나 수정할 수 없도록 하는 법=query string 있으면 안된다.
```
