##Create
mySet={1,2,3};
print(mySet);
mySet=set([4,2,2,3]);
print(mySet);

##add
mySet.add(5); ##One element
print(mySet);
mySet.update([1,7,8]);  ##many element
print(mySet);

##Delete
mySet.discard(8);
print(mySet);
##Show err if element no exits
##mySet.remove(10);
mySet.remove(1);
print(mySet);

##phép hợp
mySet1={3,5,6,1,2};
##print(mySet.union(mySet1));
print(mySet | mySet1);

##phép giao
##print(mySet.intersection(mySet1));
print(mySet & mySet1);

##calculator
##phép trừ
print(mySet - mySet1);
print(mySet);
print(mySet.difference(mySet1));
##loop
for item in mySet:
    print(item);

##practice
ListNumber=[1,2,4,6,4];
convertSet=set(ListNumber);
print("So phan tu khac nhau:",len(convertSet));
