class Stack(object):
    def __init__(self, limit=10):
        self.stackArr = [];
        self.limit = limit;

    def isEmpty(self):
        return len(self.stackArr) <= 0

    def push(self,item):
        if len(self.stackArr) >= self.limit:
            print("StackOverFlow");
        else:
            self.stackArr.append(item);
            print("Stack after push:", self.stackArr);

    def pop(self):
        if len(self.stackArr) <= 0:
            print("Stack Underflow");
            return 0;
        else:
            return self.stackArr.pop();

    def top(self):
        if len(self.stackArr) <= 0:
            print("StackOverFlow");
            return 0;
        else:
            self.stackArr[-1]

    def size(self):
        return len(self.stackArr);



# Driver Code

our_stack = Stack(5)
our_stack.push("1")
our_stack.push("21")
our_stack.push("14")
our_stack.push("11")
our_stack.push("31")

our_stack.push("14")
our_stack.push("15")
our_stack.push("19")
our_stack.push("3")
our_stack.push("99")
our_stack.push("9")
print (our_stack.top())
print (our_stack.pop())
print (our_stack.top())
print (our_stack.pop())
