+ https://docs.python.org/3/에서 문서 참고가능.<br>

## 1. LIST_new data type(목록) <br>
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

+ string <br>
```
a = '1, four, 9, 16, 25'
print(a) #1, four, 9, 16, 25
print(a[1]) #,
print(len(a)) #18
a[1] = 4 #오류
del a[2] #오류
```

: _즉, list와 str 모두 sequence operation이지만, str은 텍스트이기 때문에 n번째 원소를 다른 값으로 바꾸거나 삭제 불가. <br>
    
## 3. dict_other container (Mapping Types) <br>
+ 딕셔너리 타입은 immutable(객체 지향 프로그래밍에 있어서 불변객체는 생성 후 그 상태를 바꿀 수 없는 객체를 말한다.)한 키(key)와 mutable(가변 객체로 생성 후에도 상태를 변경할 수 있다)한 값(value)으로 맵핑되어 있는 순서가 없는 집합입니다.

REPL에서 확인합니다.

일반적인 딕셔너리 타입의 모습입니다. 중괄호로 되어 있고 키와 값이 있습니다.

>>> {"a" : 1, "b":2}
{'a': 1, 'b': 2}
```
person = {'name':'hyeonah', 'address':'seoul'}
person['name'] #hyeonah.
```




<list>
list((4, 5, 5)) #[4, 5, 5]
