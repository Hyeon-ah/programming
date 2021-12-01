# 1 1 Regular Expressions
## Basic Text Processing
+ []: square brackets
+ <>: angles
+ (): parentheses
1. What is Regular Expressions
- A formal language for specifying text strings
- Disjunctions (논리합: 수리 논리학에서 주어진 복수 명제에 적어도 1개 이상의 참이 있는지를 나타내는 논리 연산)
2. Kinds of Regular Expressions
(1) Letters inside square brackets []: matches any digits
(2) Ranges[A-Z]
(3) Negations [^Ss]: we don't want the set of letters
	+ ^을 Carat 이라고 함.
(4) pipe | = or
	+ ex. a|b|c = [abc]
(5) Other regular expressions: ? * + .
	+ ?: optional previous char(?앞의 char가 있어도 되고 없어도 되고)
	+ *: 0 or more of previous char(*앞의 문자/숫자가 0개 이상 있는지)
	+ +: 1 or more of previous char(+앞의 문자/숫자가 1개 이상 있는지)
	+ .: any digit is possible in the place of "."
	ex. beg.n -> begin begun beg3n
(6) Other regular expressions: Anchors ^ $ -> Used **outside** of square brackets
	+ ^: start with the specific char after ^ 
	ex. ^[A-Z]-> A부터 Z까지로 시작하는 것을 찾음
	+ $: finish with the specific char before $ 
	ex. [A-Z]$ -> A부터 Z까지로 끝나는 것을 찾음

3. Practice_<the/The만 찾기>
	+ step 1: [tT]he -> the, The 모두 찾기
	+ step 2: [tT]he[^A-Za-z] -> the뒤에 아무것도 없게
	+ step 3: [^A-Za-z][tT]he[^A-Za-z] -> 앞에도 아무것도 없게.