class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f'hello my name is {self.name}, and i am {self.age} years old')

person1=Person('Blin',17)
person1.greet()

class Student:
    def __init__(self,emri,age,kursi,Nota):
        self.emri=emri
        self.kursi=kursi
        self.age=age
        self._nota=nota #kjo o variabel private

    def _funksion(self):#ky o funksion privat

        print('this is a protected method ')



    def greet(self):
        print(f'My name is {self.emri},i am {self.age} years old, and i learn {self.kursi}')
Blini=Student('Blin',17,'python')
Blini.greet()


