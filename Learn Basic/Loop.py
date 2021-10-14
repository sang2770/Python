##-- chỉ cung cấp for và while
listNumber=[1,2,4,5,5];
for number in listNumber:
    print(number);
name="Nguyen Van Sang"
for character in name:
    print(character, end="-");

##--for lồng
for number in range(0, 10):
    for numberChild in range(0,number):
        print(numberChild, end=" ");
    print("");

##--while
numberStart=1;
while(numberStart<=10):
    print(numberStart, end="-");
    if numberStart==9:
        break;
    numberStart+=1;
