# -------------- Check if Array is sorted using recursion ---------------------

def isSorted(array, arrayLength):
	print("Call for array", array, "length", arrayLength);
	if arrayLength == 1:
		return True;
	return False if array[arrayLength-1] < array[arrayLength-2] else isSorted(array,arrayLength-1);


array = [1,3,2,7];

print(isSorted(array, len(array)));