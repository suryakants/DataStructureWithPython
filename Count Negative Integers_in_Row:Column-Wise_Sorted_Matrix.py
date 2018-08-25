
#  ----- Count Negative Integers in Row/Column-Wise Sorted Matrix -------
#       Example matrix M = [[-3,-2,-1,1], [-2,2,3,4], [4,5,7,8]];
#		wrong matrix(not sorted column wise) M = [[-3,-2,-1,1], [-3,-2,-1,-1], [4,5,7,8]];


def findNegativeNumberCount(M, n, m):
	count = 0;
	i = 0;
	j = m - 1;

	while i < n and j >= 0:
		if M[i][j] < 0:
			count += (j+1);
			i += 1;
		else:
			j -= 1;

	return count;



#function call

M = [[-3,-2,-1,1], [-2,2,3,4], [4,5,7,8]];
print(findNegativeNumberCount(M,3,4))


