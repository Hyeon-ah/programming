# 2 1 Defining Minimum Edit Distance
## 1. Edit Distance is measuring gow similar two strings are based on the number of edits <br> (I for insertions, D for deletions, S for substitutions)
	- Costs = all operations cost 1, except S which costs 2 
## 2. Application
	- spelling correction, speech recognition, etc
## 3. How to find the Min Edit Distance?
	- Search for a path(sequence of edits) from the start string to the final string: 
		= Initial state: 바꾸고자하는 단어 
		= Operators: I, D, S 
		= Goal state: 얻고자하는 단어  
		= Path cost: edits 수(that we are eager to minimize) 
	- e.g.)  
		= Initial state: "intention" 
		= Operators: I("eintention"), D("ntention"),  <br>S("entention") 
		= Goal state: entiontion 
		= Path cost: 2 
## 4. Defining Min Edit Distance 
	- The edit distance between X[1..n] and Y[1..m] is D(n,m) 
	source string X, target string Y
	길이가 n인 X, 길이가 m인 Y

