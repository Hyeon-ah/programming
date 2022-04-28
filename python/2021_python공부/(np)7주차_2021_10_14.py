# -*- coding: utf-8 -*-
"""(np)7주차_2021-10-14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C0MLau6OR1CrZWPxd1ZwplPPDH2lhwO8

## Numpy
"""

import numpy as np
# b = np.array(['jeong','hyeon','ah'])

a = np.array([1,2,3])
a # 백터로서 리스트가 작용함

import numpy as np
np.array([[3,4],[5,6]])

a.shape

a.ndim #차원

a.dtype

a.itemsize #size of memeory

a.size #각 객체의 크기

b = np.array([[1,2,3],[4,5,6]])
b

b.ndim

b.dtype

b.size

b.shape

a.max()

b.max()

a.var()

b.flatten()

np.append(a,b)

np.append([a],b,axis=0) #b를 a에 append하되 행을 기준으로

np.append(b,a)

"""## Numpy 사칙연산"""

c = np.array([[1,2],[3,4]])
d = np.array([[10,20],[30,40]])

c+d

c*d # element by element 곱

np.matmul(c,d) # 행렬 곱

c@d

f = list(range(0,10))
 f

np.arange (0,10)

e = list(range(0,10,2))
e

np.arange (0,10,2)

np.array(e)

np.arange(0,10).reshape(5,2)

# 3차원
t = np.arange(0, 36).reshape(3,6,2)
t

print(t[1,5,1])

# 2차원 배열의 슬라이싱
g = np.arange(0,9).reshape(3,3)
g

print(a[0])

