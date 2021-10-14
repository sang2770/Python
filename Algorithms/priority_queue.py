class Priority_queue():
##  Hàm tạo
    def __init__(self, increase=True):
        self.array=[];
        self.size=0;
        self.increase=increase;
##  Trả về kích thước 
    def size(self):
        return self.size;
##  Kiểm tra trống
    def empty(self):
        if(self.size==0):
            return True;
        else:
            return False;
##  Trả về phần tử đầu tiên
    def top(self):
        return self.array[0];
##  Vun đống sắp xếp
    def heapify(self,i):
        largest = i;
        l = 2 * i + 1;
        r = 2 * i + 2;
        n=self.size;
        if(self.increase==True):
            if l < n and self.array[i] < self.array[l]:
                largest = l;
            if r < n and self.array[largest] < self.array[r]:
                largest = r;
        else:
            if l < n and self.array[i] > self.array[l]:
                largest = l;
            if r < n and self.array[largest] > self.array[r]:
                largest = r;
        # Swap 
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest],self.array[i];
            self.heapify(largest);
##  Thêm
    def add(self,newElement):
        if(self.size==0):
            self.array.append(newElement);
        else:
            self.array.append(newElement);
            for i in range((self.size//2)-1, -1, -1):
                self.heapify(i);
        self.size+=1;
## Xóa
    def delete(self,num):
        i=0;
        for i in range(0, self.size):
            if(num==self.array[i]):
                break;
        self.array[i], self.array[self.size-1]=self.array[self.size-1], self.array[i];
        self.array.remove(self.array[self.size-1]);
        self.size-=1;
        for j in range((self.size//2) - 1, -1, -1):
            self.heapify(j);
## Xóa đầu
    def pop(self):
        top=self.array[0]
        self.delete(top);
    
Myqueue= Priority_queue();
Myqueue.add(2);
Myqueue.add(9);
Myqueue.add(1);
Myqueue.add(5);
while(Myqueue.empty()==False):
    print(Myqueue.top(), end=' ');
    Myqueue.pop();

    
        
