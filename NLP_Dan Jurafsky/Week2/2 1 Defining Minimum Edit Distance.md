# 2 1 Defining Minimum Edit Distance
## Edit Distance is measuring gow similar two strings are based on the number of edits <br> (I for insertions, D for deletions, S for substitutions)<br>
	- Costs = all operations cost 1, except S which costs 2 <br> 
## Application
	- spelling correction, speech recognition, etc
## How to find the Min Edit Distance?
	- Search for a path(sequence of edits) from the start string to the final string: <br>
		= Initial state: 바꾸고자하는 단어 <br> 
		= Operators: I, D, S <br>
		= Goal state: 얻고자하는 단어  <br>
		= Path cost: edits 수(that we are eager to minimize) <br>
	- e.g.)  <br>
		= Initial state: "intention" <br>
		= Operators: I("eintention"), D("ntention"),  <br>S("entention") <br>
		= Goal state: entiontion <br>
		= Path cost: 2 <br>
## Defining Min Edit Distance 
	- The edit distance between X[1..n] and Y[1..m] is D(n,m) <br>
	길이가 n인 X, 길이가 m인 Y

