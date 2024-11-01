from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age,weight,height): #konstruktori

        self.name=name
        self.age=age
        self._weight=weight
        self._height=height

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self,value):
        if value<0:
            raise ValueError('weight cannot be negative')
        self._weight=value



    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError('height cannot be negative')
        self._height=value

    @abstractmethod
    def calculate_bmi(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass
    def print_info(self):
        print(f'{self.name}, Age:{self.age},weight:{self.weight}, height:{self.height}')
        print(f'BMI:{self.calculate_bmi():.2f}, Category: {self.get_bmi_category()}')

class Adult(Person):
    def calculate_bmi(self):
        return self.weight/(self.height**2)
    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return ('Underweight')
        elif 18.5 <= bmi < 24.9:
            return ('Normal weight')
        elif 24.9 <= bmi < 29.9:
            return ('Overweight')
        elif bmi > 29.9:
            return ('Obese')

class Child(Adult):
    def get_bmi_category(self):
        bmi = self.calculate_bmi()*1.3
        if bmi < 14:
            return ('Underweight')
        elif 14 <= bmi < 18:
            return ('Normal weight')
        elif 18 <= bmi < 24:
            return ('Overweight')
        elif bmi > 24:
            return ('Obese')
class BMIApp:
    def __int__(self):
       self.people=[]

    def add_person(self,person):
        self.people.append(person)

    def collect_user_data(self):
        name=input('enter name')
        age=int(input('enter age'))
        weight=float(input('enter wieght in kg'))
        height=float(input('enter height in meters'))
        if age>=18:
            person=Adult(name,age,weight,height)
        else:
            person=Child(name,age,weight,height)
        self.add_person(person)
    def print_result(self):
        for person in self.people:
            person.print_info()

    def run(self):
        while True:
            self.collect_user_data()
            dont=input('Do you want to add a person').strip().lower()
            if dont!='y':

                break
        self.print_result()
app=BMIApp()
app.run()











