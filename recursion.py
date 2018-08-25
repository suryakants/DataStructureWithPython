# Calculating factorial of positive integer

import time


# def calculateFactorail(n):
# 	if n == 0:
# 		return 1;
# 	elif n == 1:
# 		return 1;
# 	else:
# 		return n * calculateFactorail(n-1);

# print(calculateFactorail(24));


def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)

start_time = time.time()
print(treefactorial(100));
print ("My program took", time.time() - start_time, "to run")

