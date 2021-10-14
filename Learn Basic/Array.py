##Khong phan biet kieu gia tri
ListName=["Sang", "Xuan","Mai"];
print(ListName[2]);
print(ListName[-1]);
#lấy từ đoạn
ListName_Child=ListName[0:2]
print(ListName_Child);
#update
ListName[2]="Trung"
print(ListName);
#delete
del ListName[2];
print(ListName);
#gộp array

Date=[1993, 1223];
Name=["NguyenSang", "PhamXuan"];
Full=[Date, Name];
print(Full);

ListNumber=[1,2,3,4,5,6,7];
print(ListNumber[0:6:2])

#xoa phan tu cuoi 

Last=ListNumber.pop();
print(Last);
ListNumber.pop()
print(ListNumber)

##tim gia tri cos thi tra ve vij trij 
print(ListNumber.index(2));
##dao nguoc
ListNumber.reverse();
print(ListNumber);
##Sap xep
ListNumber.sort(); ##Tang dan
print(ListNumber)
ListNumber.sort(reverse=True); ##giam dan
print(ListNumber)

##Gán thì nó là tham chiếu
##=> Giải pháp là copy
ListCopy=ListNumber.copy();
print(ListCopy);
ListCopy[1]=11;
print(ListCopy);
print(ListNumber);
