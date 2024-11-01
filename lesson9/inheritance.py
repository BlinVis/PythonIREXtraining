class Animal:

    def __init__(self,name):
        self.name=name
    def sound(self):

        print('some generic animal sound')

    def description1(self):
        print(f'The animal name is {self.name}')


class Dog(Animal):
    def sound(self):
        print('Woof')
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def description2(self):
        super().description1()
        print(f'this is the breed {self.breed}')



#class Cat(Animal):
   # def sound(self):
       # print('Meow')
    #super().__init__(name)


kafsha=Animal('animal name')
kafsha.sound()

qeni=Dog('bis','golden retriever')

qeni.sound()
qeni.description2()




