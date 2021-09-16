## Pypi와 패키니 매니저 <br>
:타인이 만든 소프트웨어를 자신의 소프트웨어에 부품으로서 사용하기 위한 방법으로서 패키지 매니저Pypi와 PIP를 사용하는 방법. <br>
: XSS를 통해 웹사이트 관리자가 아닌 사용자가 웹페이지에 악성 스크립트를 삽입할수 있기 때문에 <br>
sanitize-html은 이러한 공격 기법을 막기위해 나온 module. <br>
+ Python html sanitizer(세탁) <br>
+ PyPI(the Python Package Index) 중에서 html-sanitizer은 보안 module오염될 가능성 <br> 
+ pip3 install html-sanitizer 설치 <br>
```
#!python
print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer() 

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    # description = description.replace('<','&lt;')
    # description = description.replace('>','&gt;')
    title =  sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    title = pageId = 'Welcome'
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
    title=title,
    desc=description,
    listStr=view.getList(),
    update_link=update_link,
    delete_action=delete_action))
