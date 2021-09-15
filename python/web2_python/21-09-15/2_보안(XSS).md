## 1. 보안(XSS) <br>
보안 공격의 사례 중 하나인 XSS(Cross-Site Scripting) <br>
### examples <br>
+ 다른 사용자가 들어와서 description에 이런거 써서 에러메시지를 뜨게 하는 것 <br>
:  `hehe <script>alert('haha')</script>` <br>
+ 다른 사용자가 들어와서 웹페이지로 가도록 하게 하는 것 <br>
: `hehe <script>location.href="http://opentutorials.org"</script>` <br>
--> <script></script>는 java script 실행하게 하는 것임.
+ XSS.html <br>
1) 경고 pop up이 뜨게 <br>
```
<html><body>
<script>alert(1)</script>
</body></html>
```
2) 페이지 자체헤 나오도록 <br>
: <는 `&lt;`(less than), >는 `&gt;`(greater than)
```
<html><body>
&lt;script&gt;alert(1)&lt;/script&gt;
</body></html>
```

## 2. XSS 해결하는 방법 1
+ <script>가 실행되지 않고, 화면에 나타나도록 하기
+ `replace` 넣기.
```
#!python
print("Content-Type: text/html")
print()
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    description = description.replace('<','&lt;')
    description = description.replace('>','&gt;')
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action =''
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
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(
    title=pageId,
    desc=description,
    listStr=view.getList(),
    update_link=update_link,
    delete_action=delete_action))
```
