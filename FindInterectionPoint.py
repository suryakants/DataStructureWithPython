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


def findIntersactionPoint(head1, head2):
    l1 = 0; l2 = 0; diff = 0;
    list1 = head1;
    list2 = head2

    while list1 != None:
        l1 += 1;
        list1 = list1.next;

    while list2 != None:
        l2 += 1;
        list2 = list2.next;

    diff = l1-l2;
    list1 = head1;
    list2 = head2;

    if(l1 < l2):
        list1 = head2;
        list2 = head1;
        diff = l2-l1;

    for i in range(diff):
        list1 = list1.next;

    while list1 != None and list2 != None:
        if list1 == list2:
            return list1.data;
        list1 = list1.next;
        list2 = list2.next;
    return -1;





#### Driver program

nodeA = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)
nodeE = Node(5)
nodeF = Node(6)
nodeG = Node(7)

nodeX = Node(100);
nodeY = Node(200);
nodeZ = Node(300);

nodeX.next = nodeY
nodeY.next = nodeG;
nodeZ.next = nodeG;


nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = None


head = nodeA;
printLinkedList(head);
print("----------")
printLinkedList(nodeX);
print("Interection Point: ", findIntersactionPoint(nodeX, head));

# isLinkedListCircular(head);
# findNthNodeFromEnd(head, 3);
