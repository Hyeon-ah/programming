## 1. 피보나치 재귀
+ => 결국 피보나치가 0과 1로 이루어져 있다!!!!!!!
```
def fibonacci_of(n):
    if n <=1:  # Base case
        return n 
    else:
        return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
   
print(fibonacci_of(8)) # 21
```

## 2. for문
```
def fib(n):
    list = []
    for i in range(0,n):
        if i <= 1:
            list.append(1)
        else:
            list.append(list[i-1] + list[i-2])
    return list[n-1]
 
fib(8) # 21
```
## 3. Python program to generate Fibonacci series until 'n' value (1)
```
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b
```
+ 결과 값
```
Enter the value of 'n': 8
Fibonacci Series:  0 1 1 2 3 5 8 13 
```
## 4. Python program to generate Fibonacci series until 'n' value (2)_ while 문
```
def fib(number_of_terms):
   counter = 0

   first = 0
   second = 1
   temp = 0
 
   while counter <= number_of_terms:
      print(first)
      temp = first + second
      first = second
      second = temp
      counter = counter + 1
    
fib(8)
```
+ 결과 값
```
0
1
1
2
3
5
8
13
21
```
