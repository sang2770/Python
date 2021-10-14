##x=input("Nhap x")
##print(x)
##y=input("gia tri cua y:")
##print(y)
##print(int(x)+int(y))
##x=int(x)
##y=int(y)
##if x%2 ==0:
##    print(str(x) +"La so chan:")
##else:
##    print(str(x) +" La So le !")
##
##for letter in 'Python':
##    print("current letter:", letter);
##fruits=['banana', 'apple'];
##for i in fruits:
##    print("current index:", i);
##
def sum(a, b=10):
    print(str(a), str(b));
    return a+b;
print(sum(1,2));
print(sum(1));

print(sum(b=1, a=2));
##chuoi
str1="""Nguyen Van Sang
        Xuan
        Pham"""
print(str1[0:4]);
print(str1[7:-2]);
count=len(str1);
print(count);
str2=str1.replace("Van", "Xuan")

print(str2);
##find in string
print(str1.find("Sang"));
print(str1.split(' '));
print(str1.splitlines());
##Chuoi tho;
path="C:\nowWhere";
path1=r"C:\nowWhere";
print(path);
print(path1);

