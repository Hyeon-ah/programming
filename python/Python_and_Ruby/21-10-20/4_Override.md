## 1. Override
+ = 재정의
+ '올라타다'라는 뜻
+ 객체는 여러 기능을 하지고 있음. 각 기능은 method가 존재한다.(기능 = method) -> 객체지향
+ 새로운 객체 만드는데, 새로운 객체가 기존의 객체의 기능을 물려 받는다(상속)면 기존의 객체를 부모객체, 새로운 객체는 자식 객체라고 함.
+ 자식 객체는 부모 객체의 기능을 그대로 사용 = 상속의 핵심적 기능 
+ 만약 자식 객체능은 부모 객체의 기능을 변형 혹은 삭제해야 한다면? -> 동일한 이름의 method를 자식객체에 정의하면 부모객체의 특정한 기능을 "재정의" = Override

## 2.Override 형식
+ Override의 기본 형식 1
+ 부모 class의 method 재정의
```
class C1:
    def m(self):
        return 'parent'
         
# Override
class C2(C1):
    def m(self):
        return 'child'
    pass

o = C2()
print(o.m()) # child # o에 소속된 m 메서드 실햄. 
```
+ Override의 기본 형식 2
+ 부모 class의 method 호출 + 재정의
```
class C1:
    def m(self):
        return 'parent'
#Override의 기본 형식
class C2(C1):
    def m(self):

        return super().m() + ' child'
    pass
# super = method가 소속된 class의 부모 class 호출

o = C2()
print(o.m()) # parent child
```
## 3. Override 활용(4.py)
+ info라는 method를 
```
class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        result = self.v1+self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
        return result
    def subtract(self):
        result = self.v1-self.v2
        Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
        return result
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)
    def info(self):
        return "Cal => v1 : %d, v2 = %d" % (self.v1, self.v2)


class CalMultiply(Cal):
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result
    def info(self):
        return "CalMultiply => %s" % super().info()


class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1/self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result
    def info(self):
        return "CalDivide => %s" % super().info()

c0 = Cal(30, 60)
print(c0.info()) # Cal => v1 : 30, v2 = 60
c1 = CalMultiply(10,10)
print(c1.info()) # CalMultiply => Cal => v1 : 10, v2 = 10
c2 = CalDivide(20,10)
print(c2.info()) # CalDivide => CalMultiply => Cal => v1 : 20, v2 = 10
```
