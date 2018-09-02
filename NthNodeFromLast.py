class Node:
	# Default constructor
	def __init__(self, data):
		self.data = data;
		self.next = None; # make None as defalt value for next




def printLinkedList(head):
	currentNode = head
	print("LinkedList: ")
	while currentNode is not None:
		print(currentNode.data);
		currentNode = currentNode.next;

def findNthNodeFromEnd(head, position):
    if head == None:
        print("Empty List");
        return;
    tempNode = head;
    pTempNode = head;
    count = 0;
    while tempNode != None:
        count += 1;
        if position - count == 0:
            pTempNode = head;
        elif position - count > 0:
            pTempNode = pTempNode.next;
        tempNode = tempNode.next;
    if pTempNode != None:
        print("nth node from End: ", pTempNode.next);
    print("No node found");





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


head = nodeA;
printLinkedList(head);
findNthNodeFromEnd(head, 3);
