# def ways(n):
#     A = 3**(n+6)
#     M = A**6 - A**5 - A**4 - A**3 - A**2 - A - 1
#     return pow(A, n+6, M) % A

# # for i in range(20):
# print ("610", '->', ways(610))




def  possibleWaysToReachAt(n):
	if n < 0:
		return 0;

	numberOfways = 0;
	first  = 0
	second = 0
	third  = 0
	fourth = 0
	fifth  = 0
	sixth  = 1

	for i in range(0,n+1):
		numberOfways = first + second + third + fourth + fifth + sixth
		if i > 0:
			first = second
			second = third
			third = fourth
			fourth = fifth
			fifth = sixth
			sixth = numberOfways
		print( i, "->", numberOfways)
	return numberOfways


possibleWaysToReachAt(610);
