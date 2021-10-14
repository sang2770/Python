##Stack
class Stack:
    def __init__(self):
        self.stack=[];
    def push(self, item):
        self.stack.append(item);
    def pop(self):
        if len(self.stack)<1:
            return ;
        return self.stack.pop();
    def size(self):
        return len(self.stack);
    def isEmpty(self):
        if len(self)==0:
            return true;
        return false;
    def get(self):
        return self.stack;
stack=Stack();
stack.push(1);

for item in stack.get():
    print(item);
