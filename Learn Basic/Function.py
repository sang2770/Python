##-- dùng từ khóa def
def sum(number1, number2=10):
##    global addNumber
    number1+=addNumber;return number1+number2;
##--biến global
addNumber=3;
print(sum(1,2));
print(sum(1));


##-- chuyền nhiều tham số

def Res(*param):
    result=0;
    for item in param:
        result+=item;
    return result;
print(Res(1,2,3,4));
