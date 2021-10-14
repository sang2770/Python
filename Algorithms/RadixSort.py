def countingSort(array, place ):
    size=len(array);
    output=[0]*size;
    count=[0]*(10+1);
    for i in range(0, size):
        index=array[i]//place;
        count[index % 10]+=1;
    for i in range(1,10):
        count[i]+=count[i-1];
    i = size - 1;
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        array[i]=output[i];
def radixSort(array,maxElement):
    i=1;
    while(maxElement//i>0):
        countingSort(array,i);
        i*=10;
data=[1,4,2,5,6,10];
Max=max(data);
radixSort(data, Max);
print(data);
