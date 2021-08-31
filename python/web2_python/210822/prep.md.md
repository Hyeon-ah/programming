## programming 이란?
+ 응용-> application, 순서대로 작업-> program 
+ 순서대로 작업되는 것 
+ tab이 중요한 요소 
+ giving a list of instructions for a computer to follow = algorithms 
+ `print("Hello world")` is source code -> through PYTHON INTERPRETER -> `Hello world` is output window 
+ 파이썬_대화 하는거-> interactive shell방식
## 실습 준비 전 확인할 것 
+ 127.0.0.1 접속해서 bitnami잘 설치되었는지 확인 

## GUI, CLI 란? <br>
+ 기존에 폴더 직접 생성해서 하는 것-> GUI(Graphical User Interface)
+ window키+r 눌러서 cmd 해서 mkdir이나 rmdir처럼 하는 것 -> CLI(Command Line Interface) 

## CGI 란? <br>
+ Common Gateway Interface 
+ ex) `cd a` #a로 경로를 바꿔라 <br>
 > `cd \BItnami\wampstack-8.0.9-0\apache2\htdocs\` <br>
+ chrome -> 마우스 우클릭 -> 검사 -> Network -> link 클릭 -> Response -> header 
 > 웹서버가 웹브라우저에게 데이터를 전송할때 데이터가 무엇인지에 대한 것을 header라고 부름 <br>
 > ex.headers["Content-Type"] #문서형식이면 html, 사진이면 png 등등
## python.org 홈페이지에서 적용시켜보기
+ python홈페이지 - 검사 - Network - 홈페이지 - content type 복사해서 helloworld.py의 print앞에 넣기
+ cmd에 가서 python helloworld.py해보면 header다음에 한 줄 띄고 값이 나오는 걸 볼 수 있음.
```
+ #!python
a = 3+4+5
b = a/3
print("content-type: text/html; charset=utf-8\n")
print(b)
```
 
