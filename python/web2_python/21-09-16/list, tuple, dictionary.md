## list, tuple, dictionary 차이점 <br>
### 1. list  <br>
[]
indexing, sliding, 수정, del함수, append(), sort(), reverse, etc <br>
### 2. tuple <br>
() <br>
생성, 삭제, 불가 <br>
tuple안에 tuple 가능. <br>
indexing, sliding, 더하기, 곱하기, 길이 가능 <br>
for문에서 enumerate()하면 tuple 형태로 반환 <br>
```
t = [1,5,7,33,39,52]
for p in enumerate(t):
  print(p)
```
```
반환 값 : <br>
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)
```
### 3. dicionary
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
Key와 Vlaue의 쌍 여러 개가 {}을 둘러싸임. 
