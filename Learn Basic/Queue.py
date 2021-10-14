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
myQueue=queue();
myQueue.push(1);
myQueue.push(2);
myQueue.push(3);
print(myQueue.front());
