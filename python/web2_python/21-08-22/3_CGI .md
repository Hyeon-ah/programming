## 1. programming 이란?
+ 응용-> application, 순서대로 작업-> program 
+ 순서대로 작업되는 것 
+ tab이 중요한 요소 
+ giving a list of instructions for a computer to follow = algorithms 
+ `print("Hello world")` is source code -> through PYTHON INTERPRETER -> `Hello world` is output window 
+ 파이썬_대화 하는거-> interactive shell방식
## 실습 준비 전 확인할 것 
+ 127.0.0.1 접속해서 bitnami잘 설치되었는지 확인 

## 2. GUI, CLI 란? <br>
+ 기존에 폴더 직접 생성해서 하는 것-> GUI(Graphical User Interface)
+ window키+r 눌러서 cmd 해서 mkdir이나 rmdir처럼 하는 것 -> CLI(Command Line Interface) 

## 3. CGI 란? <br>
+ Common Gateway Interface 
+ Web 서버가 사용자의 요청을 받았을 때, 그 요청과 관련해서 web application이 어떠한 처리를 할 수 있도록 query string과 같은 약속되어 있는 이름의 데이터를 환경변수라는 형태로 전달해주는 것.<br>
+ index.py(web application)는 id라는 입력값을 받고 있고, id에 따라 다른 값을 출력<br>
+ google에 이미지 검색(cgi web)<br>
+ 웹서버(apache)와 cgi application(application을 만들 수 있는 언어_python, java 등)들이 쉽게 연동하기 위해 표준화된, cgi라는 "약속"을 통해 cgi application(index.py)으로 데이터 전송하면 web-server로 output 나오면 web-brower로 나오게 됨. <br>
http://127.0.0.1/cgi_env.py?id=HTML 처럼 id라는 query를 주면 HTML이 나옴.<br>

+ ex) `cd a` #a로 경로를 바꿔라 <br>
 > `cd \BItnami\wampstack-8.0.9-0\apache2\htdocs\` <br>
+ chrome -> 마우스 우클릭 -> 검사 -> Network -> link 클릭 -> Response -> header 
 > 웹서버가 웹브라우저에게 데이터를 전송할때 데이터가 무엇인지에 대한 것을 header라고 부름 <br>
 > ex.headers["Content-Type"] #문서형식이면 html, 사진이면 png 등등


## 4. python.org 홈페이지에서 적용시켜보기
+ python홈페이지 - 검사 - Network - 홈페이지 - content type 복사해서 helloworld.py의 print앞에 넣기
+ cmd에 가서 python helloworld.py해보면 header다음에 한 줄 띄고 값이 나오는 걸 볼 수 있음.
```
#!python
a = 3+4+5
b = a/3
print("content-type: text/html; charset=utf-8\n")
print(b)
```
 
