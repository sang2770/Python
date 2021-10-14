class Dictionary():
    def __init__(self):
        self.hashSize=10;
        self.hashTable=[];
        
    def hashfunc(self,s):
        Total=0;
        for x in s:
            Total+=ord(x);
        return Total% self.hashSize;
    
    def ChangeSize(self, index):
        self.hashSize=index+10;
        temp=[];
        for i in range(self.hashSize):
            temp.append(("", ""));
        i=0;
        for i in range(len(self.hashTable)):
            temp[i]=self.hashTable[i];
        self.hashTable=temp;
        
    def insert(self, s1, s2):
        index=self.hashfunc(s1);
##        self.ChangeSize(index);
        if(index>self.hashSize):
            self.ChangeSize(index);
        while(self.hashTable[index][0] !=""):
            index=(index+1)%self.hashSize;
        self.hashTable[index]=(s1, s2);
        
    def search(self, s):
        index =self.hashfunc(s);
        while(self.hashTable[index][0] !=s and self.hashTable[index] !=""):
            index=(index+1)%self.hashSize;
        if(self.hashTable[index][0]==s):
            return self.hashTable[index][1];
        return "Not Found";
            

dic=Dictionary();
dic.insert("Hello", "Xin Chao");
dic.insert("Cat", "Con meo");
dic.insert("Dog", "Con cho");
##
print(dic.search("Hello"));
print(dic.search("Cat"));
print(dic.search("Dog"));


