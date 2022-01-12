# 2 3 Backtrace for Computing Alignments
	##  1. Computing alignments
		- Align each character of the two strings to each other by "backtrace"
		- Every time we enter a cell, remember where we came from
		- When we reach the end,
		Trace back the path from the upper right corner to read off the alignment 

	## 2. Edit Distance

	## 3. MinEdit with Backtrace

	## 3. Adding Backtrace to Min Edit Distance
		- Base conditions
		- Recurrence Relation
		- Termination

	## 4. The Distance Matrix
		- Every non-decreasing path
		- from (0,0) to (M,N)
		- corresponds to an alignment of the 2 sequences

	## 5. Result of Backtrace
		- e.g.
			= I N T E * N T I O N
			= * E X E C U T I O N
			
	## 6. Performance of algorithm
		- Time : O(nm) _ order
		- Space : O(nm) 
		- Backtrace : O(n+m) 
