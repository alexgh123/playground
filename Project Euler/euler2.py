"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

# Will try solving this one without counting every third term or temp variable
def fibadder(max):
	sum = 0
	first = 1
	second = 2

	while first < max:
		if(first % 2 == 0):
			sum += first
		second = first + second
		first = second - first

	return sum

print(fibadder(4000000))
