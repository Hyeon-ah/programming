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
+ list
```
s = [1, 'four', 9, 16, 25] 
print(s) #1, 'four', 9, 16, 25
print(s[1]) #four
print(len(s)) #5
s[1] = 4 
del s[2]
print(s) #1,4, 16, 25
```

+ string
```
a = '1, four, 9, 16, 25'
print(a) #1, four, 9, 16, 25
print(a[1]) #,
print(len(a)) #18
a[1] = 4 #오류
del a[2] #오류
```

: _즉, list와 str 모두 sequence operation이지만, str은 텍스트이기 때문에 n번째 원소를 다른 값으로 바꾸거나 삭제 불가._
    
## 3. other container_dict(Mapping Types)<br>
```
person = {'name':'hyeonah', 'address':'seoul'}
person['name'] #hyeonah.
```


## 3. LOOP_반복문 <br>
+반복문 `for`의 문법 <br>
: 
>>> family = ['mother', 'father', 'gentleman', 'sexy lady']
저희 가족이 이랬었는데 기억나시지요? 그냥 따라 치지 마시고 여러분의 가족을 나타내는 리스트를 만들어 보세요.

for 문
다음은 for 문을 이용해서 저희 가족들의 이름과 문자열 길이를 출력하는 프로그램입니다.

>>> for x in family:        # family의 각 항목 x에 대하여:
...     print(x, len(x))    # x와 x의 길이를 출력하라.
...
답은 아래와 같이 나오게 되지요.

mother 6
father 6
gentleman 9
sexy lady 9
in family for x:라고 쓰면 안되냐구요?

안되네요. --;

문법이 그런 거니까 그대로 써주시면 됩니다.

range()
이번엔 range()라는 것을 배워보도록 하지요. range는 범위라는 뜻인데 여기서는 어떤 정수를 인자로 주면 그 범위 안의 정수들을 만들어줍니다. 말은 좀 어렵지만 별 거 아니랍니다.

>>> list(range(2, 7))   # 파이썬 3
>>> range(2, 7)         # 파이썬 2
이렇게 쳐 보세요. 어떤 답이 나오나요?

[2, 3, 4, 5, 6]
예, 2 이상 7 미만인 숫자로 리스트를 만들어 주었군요. 위에서 설명한 말이 이해되시죠?

그런데, for를 설명하다가 갑자기 웬 range()가 나오는 걸까요? 그렇습니다. for 문에 range()를 사용할 수 있습니다.

>>> a = [4, 5, 6, 7]
>>> for i in a:
...     print(i)
...
위의 리스트를 사용한 예제와 아래의 range()를 사용한 예제는 출력이 같습니다.

>>> for i in range(4, 8):
...     print(i)
...
답이 어떻게 나올까요? 따라서 치시기 전에 먼저 생각을 해보세요. 그리 어렵지 않죠?

프로그래밍은 아무리 쉬운 것도 직접 해보지 않으면 자기 것으로 만들기 힘들답니다. 또, 생각 없이 책만 보고 따라한다고해서 빨리 늘지도 않구요.

배우는 과정을 즐기면서 차근차근 연습하다보면 실력이 늘게 된답니다.
+ if 문: compound statement
+ []안의 것을 계속 value에 대입.<br>
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
