
class Node(object):
    """docstring for Node for linked List"""
    def __init__(self, value):
        super(Node, self).__init__()
        self.value = value;
        self.next = None;


class Stack(object):
    """docstring forStack."""
    self.top = None;

    def __init__(self):
        super(Stack, self).__init__()

    def push(self, value):
        tempNode = self.top;
        top = Node(value);
        top.next = tempNode;

    def pop(self):
        tempNode = self.top;
        top = top.next;
        return tempNode.value;

    def peek(self):
        return self.top.value

    def printStackData(self):
        currentNode = self.top;
        while currentNode.next != None:
            print(current.value);
            current = current.next;


stack = Stack();
stack.push("1")
stack.push("21")
stack.push("14")
stack.push("11")
stack.push("31")
print(stack.peek());
print(stack.pop());
# stack.printStackData();
