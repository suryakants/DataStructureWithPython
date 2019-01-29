def findFn(n):
	if n == 1:
		return 1
	fn = 0
	f0 = 0
	f1 = 1

	for i in range(0,n):
		fn = f0 + f1;
		if i > 0:
			f0 = f1
			f1 = fn;
	return fn;



# for i in range(1,10):
print(findFn(8181));
