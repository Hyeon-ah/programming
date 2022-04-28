# -*- coding: utf-8 -*-
"""practice_21-10-21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Fz30g-cGGPTy-NUyI8PxakbJfp1cam1
"""

# 피보나치 for문
def fib(n):
    list = []
    for i in range(0,n):
        if i <= 1:
            list.append(1)
        else:
            list.append(list[i-1] + list[i-2])
    return list[n-1]
 
fib(8) # 21

def fib(n):
  list = []
  for i in range(0,n):
    if i <= 1:
      list.append(1)
    else:
      list.append(list[i-1] + list[i-2])
  return list[n-1]

fib(8)

# 피보나치 재귀
def Fib(n):
  if n <= 1:
    return  n 
  else: 
    return Fib(n-1) + Fib(n-2)

Fib(8)

class C(object):
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)
    def getValue(self):
        return self.value
    def setValue(self, v):
        self.value = v



c1 = C(10)
print(c1.getValue()) #10
c1.setValue(20)
print(c1.getValue()) #20
'''
print(c1.show()) #20  #None
print(c1.__init__(30)) #None
'''

class D(object):
  def __init__(self,t):
    self.value = t
  def getValue(self):
    return self.value
  def setValue(self, t):
    self.value = t

d1 = D(20)
print(d1.getValue()) # 20
d1.setValue(30)
print(d1.getValue()) # 30

class F(object):
  def __init__(sunny, t):
    sunny.volume = t
  def getValue(sunny):
    return sunny.volume
  def setValue(sunny, t):
    sunny.volume = t

f1 = F(8)
print(f1.getValue()) # 8
f1.setValue(80)
print(f1.getValue()) # 80

class Cal(object): 
    # def __init__(self, v1, v2):
    #     self.v1 = v1
    #     self.v2 = v2
        
    def add(v1, v2):
        return v1 + v2
        
    def subtract(v1, v2):
        return v1 - v2

# c1 = Cal(10,10)
print(Cal.add(10,10))
print(Cal.subtract(10,10))

