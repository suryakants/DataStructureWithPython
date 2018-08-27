#--------Single Link List class --------------


class Node:
	# Default constructor
	def __init__(self, data):
		self.data = data;
		self.next = None; # make None as defalt value for next

	# Setter/getter - data value
	def setData(self,data):
		self.data = data;

	def getData(self):
		return self.data;

	# Setter/getter - next value
	def setNext(self,next):
		self.next = next;

	def getNext(self):
		return self.next;

	# return true if there is next node available to current node otherwise false.
	def hasNext(self):
		return self.next != None


def countNode(head):
	if head.next == None:
		return 1;
	count = 1;
	current = head;
	while current.next is not None:
		current = current.next;
		count += 1;

	return count;

# def insertNode(head, postion, data):
# 	current = head;
# 	newNode = Node(data);
# 	if postion is 1:
# 		newNode.next = current;
# 		head = newNode;
# 		return newNode;

# 	#while current.next:
# 		pass

def printLinkedList(head):
	currentNode = head
	print("LinkedList: ")
	while currentNode is not None:
		print(currentNode.data);
		currentNode = currentNode.next;

def reverseLinkedList(head):
	if head ==  None:
		return -1

	currentNode = head
	prevNode = None;
	nextNode = None;

	while currentNode != None:
		nextNode = currentNode.next;
		currentNode.next = prevNode;

		prevNode = currentNode;
		currentNode = nextNode;

	return prevNode;


def insertNode(position, data, head):
	newNode = Node(data);

	if newNode is None:
		return False;

	tempNode = head;

	#insert at 1st position
	if position == 1:
		newNode.next = tempNode;
		head = newNode;
		return True;

	#insert somewhere at middle;

	index = 1;
	while ((tempNode is not None) and (index < position)):
		index = index + 1;
		targetNode = tempNode;
		tempNode = tempNode.next;

	newNode.next = targetNode.next;
	targetNode.next = newNode;
	return True;


##### This function delete the given node from the linkedlist at given position
##### return the deleted node or None if the node isn't available

def deleteNode(head, postion):
	if head is None or postion is 0:
		print("No node to Delete or List is Empty");
		return head;
	currentNode = head;

	#Deleting node from first position
	if postion is 1:
		head = head.next;
		value = currentNode.data;
		currentNode = None;
		return head;

	prevNode = head;
	index = 1
	while index < postion and currentNode is not None:
		index =+ 1;
		prevNode = currentNode;
		currentNode = currentNode.next;

	if currentNode is None:
		print("Position Doesn't exist");
		return head;

	value = currentNode.data;
	prevNode.next = currentNode.next;
	currentNode = None;
	return head;


##### Delete the complete list

def deleteList(head):
	tempNode = head;
	auxilaryNode = head;

	while tempNode != None:
		auxilaryNode = tempNode.next
		tempNode = None;
		tempNode = auxilaryNode;

	del(head);


def findMidPointOFLL(head):
	if head == None:
		print("Linked List has not node");
		return -1;
	if head.next == None:
		return head;

	currentNode = head;
	tempNode = head;
	while currentNode != None and currentNode.next != None:
		print("Temp: ",tempNode.data, "current: ",currentNode.data);
		tempNode = tempNode.next;
		currentNode = currentNode.next.next;
	return tempNode;




#### Driver program

nodeA = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)
nodeE = Node(5)
nodeF = Node(6)
nodeG = Node(7)


nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
# print("Number of node in Single Link List", countNode(nodeA));
# printLinkedList(nodeA);
# nowNewHead = reverseLinkedList(nodeA);

# deleting a node
head = nodeA;
printLinkedList(head);
# head = print("DELETED NODE: ", deleteNode(head,1));
# printLinkedList(head);
print("------------------------")
midNode = findMidPointOFLL(head);
print(midNode.data);

#deleting the entire list
	# printLinkedList(head);
	# print("DELETED NODE: ", deleteList(head));
	# printLinkedList(nodeA);
