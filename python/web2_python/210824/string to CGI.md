- CGI로 홈페이지를 출력<br>
- error 발생시, error log참고<br>
```
#!python
print("Content-Type: text/html")
print()
print('hello World')
```

- id설정<br>
```
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
```

- ?id=HTML 을 query string 이라고 함.<br>
```
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
  </ol>
  <h2>{title}</h2>
  <p>The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland.[2][3] The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991.
  </p>
</body>
</html>
''' .format(title=pageId))
```

**CGI란 무엇인가**

- Web 서버가 사용자의 요청을 받았을 때, 그 요청과 관련해서 web application이 어떠한 처리를 할 수 있도록 query string과 같은 약속되어 있는 이름의 데이터를 환경변수라는 형태로 전달해주는 것.<br>
- index.py(web application)는 id라는 입력값을 받고 있고, id에 따라 다른 값을 출력<br>
- google에 이미지 검색(cgi web)<br>
- 웹서버(aparche)와 cgi application(application을 만들 수 있는 언어_python, java 등)들이 쉽게 연동하기 위해 표준화된, cgi라는 "약속"을 통해 cgi application(index.py)으로 데이터 전송하면 web-server로 output나오면 web-brower로 나오게 됨. http://127.0.0.1/cgi_env.py?id=HTML 처럼 id라는 query를 주면 HTML이 나옴.<br>
