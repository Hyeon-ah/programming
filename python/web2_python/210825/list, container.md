+ https://docs.python.org/3/에서 문서 참고가능.<br>

## 1. LIST_new data type(목록) <br>
+ (Metaphor) 짐이 많으면 가구골라서 정리하는 것과 비슷한 개념 <br>
+ CONTAINER <br>
+ 대괄호[] 안 : index <br>
+ 순서가 있기에 index로 접근 가능. <br>
+ `list((4, 5, 5))` #[4, 5, 5] <br>

`s = [1, 'four', 9, 16, 25]` #여기 안에 있는 건 원소( <br>
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
+ list와 str 비교(공/차) <br>
```
'"a"+"b"' #'ab'
`['a']+['b']` #['a', 'b']
'hyeonah'.capitalize() #'Hyeonah'
'123'.capitalize() #'123'
['hyeonah'].capitalize() #오류
```
_예를 들어, 대문자화 하는 것은 str은 되지만 list는 안되는 것을 확인.
+ list <br>
```
s = [1, 'four', 9, 16, 25] 
print(s) #1, 'four', 9, 16, 25
print(s[1]) #four
print(len(s)) #5
s[1] = 4 
del s[2]
print(s) #1,4, 16, 25
```

+ string <br> <br>
```
a = '1, four, 9, 16, 25'
print(a) #1, four, 9, 16, 25
print(a[1]) #,
print(len(a)) #18
a[1] = 4 #오류
del a[2] #오류
```

: _즉, list와 str 모두 sequence operation이지만, str은 텍스트이기 때문에 n번째 원소를 다른 값으로 바꾸거나 삭제 불가. <br>
    
## 3. 객체(Object)에 관하여 <br>
+ 객체의 3 특징 <br>
    1) value : 메모리에 저장된 값 <br>
    2) type	: int, str, dict 등등, 객체의 데이터 타입, 일종의 객체 생성자 <br>
              type() 로 확인 가능 <br>	
    3) identity: 각 객체가 가진 고유한 ID, 일종의 메모리 주소 <br>
              id() 로 확인 가능, a is b 로 일치불일치 여부 확인 가능 <br>

+ 가변객체(mutable) <br>
: 가변 객체로 생성 후에도 상태를 변경할 수 있다 <br>
: list, dict, set, 등등... <br>

+ 불변객체(immutable) <br>
: 객체 지향 프로그래밍에 있어서 불변객체는 생성 후 그 상태를 바꿀 수 없는 객체 <br>
: str, int, float, tuple, 등등... <br>
```
x = 'test1'
print(x) # test1

x += ' test2'
print(x) # test1 test2
```
: 'test1' value를 가진 x의 value를 'test1 test2'로 바꾼 결과 <br>
-> BUT 'test1'이 바뀐 것이 아니라! x에 새로운 value'test2'를 부여하면서 메모리 위치가 변경 된 것 <- (identity 변경) <br>
: 따라서 기존의 'test1'이 변경된 것이 아니라, **새로운 object를 생성한 것** <br>
: 아래를 통해서 검증 <br>
 ```
x = 'test1'
print(id(x)) #2728170311152

x += 'test2'
print(id(x)) #2728170310768
```
: id()는 해당 값이 저장되어 있는 일종의 메모리 위치를 나타냄. <- (identity) <br> 
: 만약 'test1'의 value가 변경된 것이라면, 메모리 위치는 동일해야 함. <br>
: int type의 연산결과도 마찬가지 <br>


## 4. dict_other container (Mapping Types) <br>
+ 값에 대한 이름을 문자로 부여하는 것.
+ 딕셔너리 타입은 immutable한 key(키)와 mutable한 value(값)으로 맵핑되어 있는 **순서가 없는 집합**. <br>
+ 기본 딕셔너리의 모습 <br>
```
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
#more details
{"a" : 1, "b":2}
{'a': 1, 'b': 2}
```
+ set 중괄호`{}`를 이용하지만 빈중괄호로 선언하면 type이 dict가 됨. <br>
+ dic의 큰 특징들 <br>
: 딕셔너리는 list나 tuple처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻음. <br>
: Key와 Value의 쌍 여러 개가 { }로 둘러싸여 있다. <br>
: 각각의 요소는 Key : Value 형태로 이루어져 있고 쉼표(,)로 구분되어 있다. <br>
: ※ Key에는 변하지 않는 값(immutable)을 사용하고, Value에는 변하는 값(mutable)과 변하지 않는 값(immutable) 모두 사용할 수 있다. <br>

```
person = {'name':'hyeonah', 'address':'seoul'}
person['name'] #hyeonah.
```




