##Mặc định các method là public
class Animal():
    def __init__(self, name, age):
        self.name=name;
        self.age=age;
    def showName(seft):
        print(seft.name);

dog=Animal("dog", 11);
dog.showName();

##Kế thừa
class Cat(Animal):
    def showName(self):
        print(self.name+" inhederit");
##    private
    def __Private():
        print("Private");
cat=Cat("Cat", 11);
cat.showName();
##cat.__Private();
