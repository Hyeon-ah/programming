# 1 1 Regular Expressions
## Basic Text Processing
+ `[]`: square brackets
+ `<>`: angles
+ `()`: parentheses
+ `^`: Carat
### 1. What is Regular Expressions
- A formal language for specifying text strings
- Disjunctions (논리합: 수리 논리학에서 주어진 복수 명제에 적어도 1개 이상의 참이 있는지를 나타내는 논리 연산)
### 2. Kinds of Regular Expressions
#### 1) Letters inside square brackets `[]`: matches any digits <br>
#### 2) Ranges`[A-Z]` <br>
#### 3) Negations `[^Ss]`: we don't want the set of letters <br>
#### 4) pipe `|` = or <br>
	ex. a|b|c = [abc] <br>
#### 5) Other regular expressions: `?` `*` `+` `.` <br>
5-1) `?`: optional previous char(?앞의 char가 있어도 되고 없어도 되고) <br>
5-2) `*`: 0 or more of previous char(*앞의 문자/숫자가 0개 이상 있는지) <br>
5-3) `+`: 1 or more of previous char(+앞의 문자/숫자가 1개 이상 있는지) <br>
5-4) `.`: any digit is possible in the place of "." <br>
	ex. beg.n -> begin begun beg3n <br>
#### 6) Anchors `^` `$` -> Used **outside** of square brackets <br>
+ 2종 가설(기무가설을 거짓이지만, 기무가설 채택-> 살아야 하는게 죽는 경우?) 1종 가설(기무가설이 참이지만,
+ 기무가설 - 대립가설?
6-1) `^`: start with the specific char after ^  <br>
	ex. ^[A-Z]-> A부터 Z까지로 시작하는 것을 찾음 <br>
6-2) `$`: finish with the specific char before $  <br>
	ex. [A-Z]$ -> A부터 Z까지로 끝나는 것을 찾음 <br>

### 3. Practice_<the/The만 찾기>
	+ step 1: `[tT]he` -> the, The 모두 찾기
	+ step 2: `[tT]he[^A-Za-z]` -> the뒤에 아무것도 없게
	+ step 3: `[^A-Za-z][tT]he[^A-Za-z]` -> 앞에도 아무것도 없게.
