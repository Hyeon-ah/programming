# 1 2 Regular Expression Substitutions
## Basic Text Processing_ More regular Expressions: Substitutions(치환) and ELIZA
+ ^ 또는 문자를 메타문자가 아닌 문자 그 자체로 매치하고 싶은 경우에는 \^ 로 사용하면 된다.

### 1. Capture Groups(그루핑)
+ Say we want to put angles around all numbers: the 35 boxes -> the <35> boxes
+ Use parens () to "capture" a pattern into a numbered register(1,2,3 ...)
+ Use `\1` to refer to the contents of the register <br>
(재참조)`\1`은 정규식의 그룹 중 첫 번째 그룹을 가리킴. 두 번째 그룹을 참조하려면 `\2`를 사용.

### 2. Capture Groups: Multiple Registers
+ ex. <br>
```
/the (.*)er they (.*), the \1er we \2/ 
	Matches: 
		the faster they ran, the faster we ran 
	But not: 
		the faster they ran, the faster we ate 
```
+ But suppose we don't want to capture?
+ Parentheses' 2 functions: 
	1) Grouping terms _정규식의 여러 문자를 그룹으로 묶어주는 것_
	2) Capturing _정규식의 일부분에 해당하는 문자열에만 관심이 있을 때 그 부분을 따로 빼서 캡처하는 기능_

+ Non-capture groups: add a `?:` after paren
+ To sum up, 
```
`?:` -> consider this parens just for grouping not for capturing.
```
ex.
```
/(?:some|a few) (people|cats) like some \1/ <br>
	Matches: <br>
		some cats like some cats <br>
	But not: <br>
		some cats like some some <br>
```

#### ()의 그루핑, 캡쳐 기능 관련하여
+ Example of Grouping 
```
'12 1212 1222'에서 ‘12’ 혹은 ‘1222’가 아닌 ‘1212’와 같은 문자열을 찾기 
-> 소괄호 ( )로 그룹화

print(re.match('(12)+', '1212'))
print(re.search('(12)+', '1212'))
print(re.findall('(12)+', '1212'))
print(re.fullmatch('(12)+', '1212'))
```
+ Example of Capturing
```
‘yyyy-mm-dd’와 같이 날짜를 나타내는 문자열 중 월, 일을 각각 따로 빼서 쓰기
-> 따로 빼고 싶은 부분인 ‘mm’과 ‘dd’ 부분에만 소괄호의 캡처 기능을 사용

print(re.findall('\d{4}-(\d\d)-(\d\d)', '2028-07-28'))
print(re.findall('\d{4}-(\d\d)-(\d\d)', '1999/05/21 2018-07-28 2018-06-31 2019.01.01'))
```
결과
```
[('07', '28')]
[('07', '28'), ('06', '31')] # 형식에 맞지 않는 01.01은 나오지 않음.
```
### 3. Lookahead Assertions
+ Make use of the paren question mark syntax for non-capture.
+ `(?= pattern)` -> is true if pattern matches, but is **ZERO-WIDTH(문자열 소비하지 않음)**; doesn't advance character pointer
+ `(?! pattern)` -> true if a pattern does not match <br>
This used more when parsing complex patterns.
+ `/^(?!Volcano)[A-Za-z]+/` <br>
-> matches the beginning of a line matches any single word that doesn't start with "Volcano"

### 4. Kinds of Zero-width Assertion
https://wansook0316.github.io/dv/concept/2020/10/08/regex-07-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%A9%94%ED%83%80%EB%AC%B8%EC%9E%90.html
+ ^	->문자열의 맨 처음과 일치하는가?(괄호 밖에 사용시.)	 
```
>>> print(re.search('^Life', 'Life is too short'))
<re.Match object; span=(0, 4), match='Life'>
>>> print(re.search('^Life', 'My Life'))
None
```
+ $	->문자열의 맨 끝과 일치하는가?	 
+ \A ->문자열의 맨 처음과 일치하는가?	 
+ \Z ->문자열의 맨 끝과 일치하는가?	 
+ \b ->단어 구분자(보통 whitespace_공백으로 구분됨.)
```	
>>> p = re.compile(r'\bclass\b')
>>> print(p.search('no class at all'))
<re.Match object; span=(3, 8), match='class'> 
+ \B ->whitespace가 양쪽에 없는(사실 단어라고 볼수는 없음) 경우에 해당 문자가 있는 경우 매치
```
```
>>> p = re.compile(r'\Bclass\B')
>>> print(p.search('no class at all'))
None
>>> print(p.search('the declassified algorithm'))
<re.Match object; span=(6, 11), match='class'>
>>> print(p.search('one subclass is'))
None
```


### 5. Simple Application: ELIZA
+ Early NLP system that imitated a Rogerian psychotherapist_Joseph Weizenbaum, 1966.
+ Uses pattern matching to match("I need X") and translates them into...("What would it mean to you if you got X?")
