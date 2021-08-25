#1. 문자열 표현
print('Hello world')
print("Hello world")
print("Hell'o' world")
print("Hell'o' world")

#escape \뒤에 있는 거 하나를 문자화 함.
print("Hell'o' \"w\"orld")

#newline
print('H')
print('e')
print('l')
print('l')
print('o')
print('H\ne\nl\nl\no')

#docsting
print('''
H
e
l
l
o
''')


#2. 문자열 처리
#변수=변할 수 있는 값
a = 'Hello Python'
print(a)

#python string length
print(len(a))

#string slice, 대괄호 안에 자릿수(index)를 준다.
#python은 카운팅을 0부터
print(a[0])
print(a[1])
print(a[2:5])

#repeat
print(a*2)
print((a+'\n')*2)


#3. 문자열 치환; 문자열과 변수
#editor이용_apple이릉을 각 이름에 맞게 수정
name = 'hyeonah' #name을 변수화
age = 12
print('to '+name+'. Lorem ipsum dolor sit amet, consectetur '+age+' adipisicing elit, sed do eiusmod apple tempor incididunt ut labore apple computeret dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '+name+' voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui '+name+' officia deserunt mollit anim id est laborum.')
#? 이름이 여러개이면 어떻게 하면 될까?

#formatting
#name은 문자만, age는 숫자만 넣도록 하도록


#순서대로 데이터 치환
#positional formatting
print('to {}. Lorem ipsum dolor sit amet, consectetur {} adipisicing elit, sed do eiusmod apple tempor incididunt ut labore apple computeret dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in {} voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui {} officia deserunt mollit anim id est laborum.' .format('hyeonah', 12, 'hyeonah', 'hyeonah'))

#4. formatting
#Named placeholder #중복이 사라지고, 데이터의 취지(가독성)높아짐.
print('to {name}. Lorem ipsum dolor sit amet, consectetur {age:d} adipisicing elit, sed do eiusmod apple tempor incididunt ut labore apple computeret dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in {name} voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui {name} officia deserunt mollit anim id est laborum.' .format(name='hyeonah', age =12))
#age:d(digit)를 하면 age에 문자가 오면 아래와 같은 오류나옴. = name은 문자만, age는 숫자만 넣도록 하도록.
#ValueError: Unknown format code 'd' for object of type 'str'
