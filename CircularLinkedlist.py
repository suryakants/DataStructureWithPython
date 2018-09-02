# Circular Linkedlist


class Node:
	# Default constructor
	def __init__(self, data):
		self.data = data;
		self.next = None; # make None as defalt value for next



def traverseCircularLinkedList(head):
	if head == None:
		return 0;
	count = 1;
	currentNode = head;

	while currentNode.next != head:
		count += 1;
		currentNode = currentNode.next;

	return count;

def printLinkedList(head):
	currentNode = head
	print("LinkedList: ")
	print(currentNode.data);
	currentNode = currentNode.next

	if currentNode == head:
		return;

	while currentNode != head:
		print(currentNode.data);
		currentNode = currentNode.next;


def printCLL(head):
	temp = head;
	if head is not None:
		while True:
			print(temp.data);
			temp = temp.next;
			if temp == head:
				break;

def deleteNode(head, position):
	print("will be implemented soon");

def insertNodeAtTheEndOfCLL(head,data):
	currentNode = head;
	if head == None:
		return;
	newNode = Node(data);
	if newNode == None:
		print("Memory error");
		return;
	newNode.next = None;

	while currentNode.next != head:
		currentNode = currentNode.next;

	newNode.next = head;
	currentNode.next = newNode;
	return head;

def insertNodeAtTheBegining(head, data):
	if head == None:
		return;
	currentNode = head;
	newNode = Node(data);
	if newNode == None:
		print("Memory error");
		return;
	newNode.next = head;

	while currentNode.next != head:
		currentNode =  currentNode.next;

	currentNode.next = newNode;
	head = newNode;
	printLinkedList(head);

def deleteLastNodeFromCLL(head):
	if head == None:
		return;
	currentNode = head;
	prevNode = head;

	while currentNode.next != head:
		prevNode = currentNode
		currentNode = currentNode.next

	prevNode.next = head;
	del(currentNode);
	# return head;

def deleteFirstNodeFromCLL(head):
	if head == None:
		return;
	temp = head;
	currentNode = head;
	while currentNode.next != head:
		currentNode = currentNode.next;

	currentNode.next = head.next;
	head = head.next;
	del temp;
	printLinkedList(head);

def findNthNodeFromEnd(head, position):
	if head == None:
		return;
	tempOne = head;
	tempTwo = head;
	count = 1;
	while tempOne.next != None:
		tempOne = tempOne.next;
		if count >= position:
			tempTwo = tempTwo.next;
		count += 1;

	return tempTwo;

#### Driver program

nodeA = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)
nodeE = Node(5)
nodeF = Node(6)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = None;
# nodeF.next = nodeA

# print("Number of node in Single Link List", countNode(nodeA));
# printLinkedList(nodeA);
# nowNewHead = reverseLinkedList(nodeA);

# deleting a node
head = nodeA;
# printCLL(head);
# print("----------------")
# print(traverseCircularLinkedList(head));
# head = print("DELETED NODE: ", deleteNode(head,1));
# insertNodeAtTheEndOfCLL(head, 7);
# insertNodeAtTheBegining(head, 0);
print("----------------")
# deleteLastNodeFromCLL(head)
# deleteFirstNodeFromCLL(head);
# printLinkedList(head);
print(findNthNodeFromEnd(head,6).data)
# print("Data :", searchNode.data);

# printLinkedList(head);
