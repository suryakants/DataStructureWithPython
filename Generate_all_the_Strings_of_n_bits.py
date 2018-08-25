####------generate all the Strings of n bits ------######

array = [1,2];
def binary(n):
	if n < 1:
		print(array);
	else:
		array[n-1] = 0;
		binary(n-1);
		array[n-1] = 1;
		binary(n-1);

binary(len(array));
