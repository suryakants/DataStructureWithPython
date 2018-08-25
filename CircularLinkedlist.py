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
nodeF.next = nodeA

# print("Number of node in Single Link List", countNode(nodeA));
# printLinkedList(nodeA);
# nowNewHead = reverseLinkedList(nodeA);

# deleting a node
head = nodeA;
printCLL(head);
print("----------------")
# print(traverseCircularLinkedList(head));
# head = print("DELETED NODE: ", deleteNode(head,1));
insertNodeAtTheEndOfCLL(head, 7);
printLinkedList(head);

