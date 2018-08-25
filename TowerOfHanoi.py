
#### Tower of hanoi #######

def towerOfHanoi(numberOfPlates, source_peg, destination_peg, auxilary_peg):
	if numberOfPlates == 1:
		print("Move disk 1 from Peg", source_peg, "to Peg", destination_peg);
		return;

	# Move numberOfPlates-1 peg from source to auxilary peg
	towerOfHanoi(numberOfPlates-1,source_peg,auxilary_peg, destination_peg);
	print ("Move disk",numberOfPlates,"from rod",source_peg,"to rod",destination_peg);
	towerOfHanoi(numberOfPlates-1, auxilary_peg, destination_peg, source_peg);

n = 4;
towerOfHanoi(3,'source_peg', 'destination_peg', 'auxilary_peg');


