class queue():
    def __init__(self):
        self.queue=[];
    def push(self, item):
        self.queue.append(item);
    def front(self):
        return self.queue[0];
    def pop(self):
        self.queue.remove(0);
    def isEmpty(self):
        if len(self.queue)>0:
            return false;
        return true;
class stack():
    def __init__(self):
        self.stack=[];
    def push(self, item):
        self.stack.insert(0,item);
    def front(self):
        return self.stack[0];
    def pop(self):
        self.stack.remove(0);
    def isEmpty(self):
        if len(self.stack)>0:
            return false;
        return true;
##myStack=stack();
##myStack.push(2);
##myStack.push(3);
##print(myStack.front());
