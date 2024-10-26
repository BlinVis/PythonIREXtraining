class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
    def getage(self):
        return self.__age
    def setage(self,age):
        self.__age=age
donjeta=Student('Donjeta',17)
print(donjeta.__age)


