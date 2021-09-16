## list, tuple, dictionary 차이점 <br>
### 1. list  <br>
+ 표현방법: [] <br>
+ 다양한 자료형 모두 사용 가능, empty_list(e.x.list())도 가능. <br>
+ indexing, sliding, 수정, del함수, append(), sort(), reverse, etc <br>
+ indexing
```
h = [1, 2, 3]
h #[1, 2, 3]
h[0] #1
```
+ sliding
```
h = [1, 2, 3]
h[0:2] ##[1, 2, 3]
```
+ del()
```
h = [1, 2, 3]
del h[1]
h #[1, 3]
```
+ append()
```
h = [1, 2, 3]
h.append('a')
h #[1, 2, 3, 'a']
```
### 2. tuple <br>
+ 표현방법: () <br>
+ list처럼 순서 있으나, element 값 변경 불가.
+ 생성, 삭제, 불가 <br>
+ tuple안에 tuple 가능. <br>
```
h = (1, 'b', ('gee', 'hi'))
h #(1, 'b', ('gee', 'hi')
```
+ indexing, sliding, 더하기, 곱하기, 길이 가능 <br>
+ for문에서 enumerate()하면 tuple 형태로 반환 <br>
```
t = [1,5,7,33,39,52]
for p in enumerate(t):
  print(p)
```
```
#결과 값
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)
```
### 3. dicionary
+ 표현방식: {Key1:Value1, Key2:Value2, Key3:Value3, ...}
+ Key와 Vlaue의 쌍 여러 개가 {}을 둘러싸임.
+ Key에 리스트는 사용불가, but 튜플은 Key로 사용가능.
+ Key는 변하지 않는 값이 와야 함. (딕셔너리의 Key로 쓸 수 있느냐 없느냐는 Key가 변하는 값인지 변하지 않는 값인지에 달려 있음.)
