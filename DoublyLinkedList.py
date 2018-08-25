### Doubly Lisk list


class Node:
	def  __init__(self,data = None, next = None, prev = None):
		self.data = data;
		self.next = next;
		self.prev = prev;


def insertNodeAtBeginning(head, data):
	newNode = Node(data);

	if head == None:
		head = newNode;
	else:
		newNode.next = head
		head.prev = newNode;
		head = newNode

	# printDLL(head);
	return head;

def printDLL(head):
	currentNode = head
	print("Doubly Link List:")
	while currentNode != None:
		print(currentNode.data);
		currentNode = currentNode.next;

def deleteNodeFromDLL(head, position):
	if position == 0 or head == None:
		print("Empty List");
		return None;
	tempNode = head;
	if position == 1:
		head = head.next;
		if head != None:
			head.prev = None;
        tempNode = None;
        return head;
    counter = 1;
    while k < position and tempNode != None:
    	tempNode = tempNode.next;
    	counter += 1;

    if k != position-1:
    	print("position doesn't exist");
    	return head;

    prevNode = tempNode.prev;
    prevNode.next = tempNode.next
    if tempNode.next:
    	tempNode.next.prev = prevNode;
    	tempNode = None
    return head;


# Deiver code
nodeFive   = Node(5)
nodeFour   = Node(4)
nodeThree = Node(3)
nodeTwo   = Node(2)
nodeOne   = Node(1)

nodeOne.prev = None;
nodeOne.next = nodeTwo;
nodeTwo.prev = nodeOne;

nodeTwo.next = nodeThree;
nodeThree.prev = nodeTwo;
nodeThree.next = nodeFour;

nodeFour.prev = nodeThree;
nodeFour.next = nodeFive;

nodeFive.prev = nodeFour;
nodeFive.next = None;

printDLL(nodeOne);
# nodeOne = insertNodeAtBeginning(nodeOne, 0);
nodeOne = deleteNodeFromDLL(nodeOne, 0);
printDLL(nodeOne);



