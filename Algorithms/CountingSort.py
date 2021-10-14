def countingSort(array, maxSize ):
    size=len(array);
    output=[0]*size;
    count=[0]*maxSize;
    for i in range(0, size):
        count[array[i]]+=1;
    for i in range(1,maxSize):
        count[i]+=count[i-1];
    for i in range(0, size):
        output[count[array[i]]-1]=array[i];
        count[array[i]]-=1;
    for i in range(0, size):
        array[i]=output[i];
        
data=[1,4,2,5,6,10];
Max=max(data);
countingSort(data, Max+1);
print(data);
    
    
