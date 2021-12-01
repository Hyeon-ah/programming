# 1 1 Regular Expressions
## Basic Text Processing
+ `[]`: square brackets
+ `<>`: angles
+ `()`: parentheses
### 1. What is Regular Expressions
- A formal language for specifying text strings
- Disjunctions (논리합: 수리 논리학에서 주어진 복수 명제에 적어도 1개 이상의 참이 있는지를 나타내는 논리 연산)
### 2. Kinds of Regular Expressions
(1) Letters inside square brackets `[]`: matches any digits <br>
(2) Ranges`[A-Z]` <br>
(3) Negations `[^Ss]`: we don't want the set of letters <br>
`^`을 Carat 이라고 함. <br>
(4) pipe `|` = or <br>
	+ ex. a|b|c = [abc] <br>
(5) Other regular expressions: ? `*` `+` `.` <br>
	+ `?`: optional previous char(?앞의 char가 있어도 되고 없어도 되고) <br>
	+ `*`: 0 or more of previous char(*앞의 문자/숫자가 0개 이상 있는지) <br>
	+ `+`: 1 or more of previous char(+앞의 문자/숫자가 1개 이상 있는지) <br>
	+ `.`: any digit is possible in the place of "." <br>
	ex. beg.n -> begin begun beg3n <br>
(6) Other regular expressions: Anchors ^ $ -> Used **outside** of square brackets <br>
	+ `^`: start with the specific char after ^  <br>
	ex. ^[A-Z]-> A부터 Z까지로 시작하는 것을 찾음 <br>
	+ `$`: finish with the specific char before $  <br>
	ex. [A-Z]$ -> A부터 Z까지로 끝나는 것을 찾음 <br>

### 3. Practice_<the/The만 찾기>
	+ step 1: [tT]he -> the, The 모두 찾기
	+ step 2: [tT]he[^A-Za-z] -> the뒤에 아무것도 없게
	+ step 3: [^A-Za-z][tT]he[^A-Za-z] -> 앞에도 아무것도 없게.
