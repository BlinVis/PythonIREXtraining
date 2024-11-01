from symtable import Class


class HumanBMI:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height

    def calculate_bmi(self):
        return (self.weight / (self.height**2))

    def get_bmi_category(self):
        bmi=self.weight/ (self.height**2)
        if bmi<18.5:
            return ('Underweight')
        elif 18.5<=bmi<24.9:
            return ('Normal weight')
        elif 24.9<=bmi<29.9:
            return ('Overweight')
        elif bmi>29.9:
            return ('Obese')

    def get_info(self):
        print(self.name,self.age,self.height,self.weight,self.calculate_bmi(),self.get_bmi_category())

class Adult(HumanBMI):
    def __init__(self,name,age,weight,height):
        super().__init__(name,age,weight,height)

class Child(HumanBMI):
    def __init__(self,name,age,weight,height):
        super().__init__(name,age,weight,height)
    def get_bmi_category(self):
        bmi = self.weight / (self.height ** 2)
        if bmi < 14:
            return ('Underweight')
        elif 14 <= bmi < 18:
            return ('Normal weight')
        elif 18 <= bmi < 24:
            return ('Overweight')
        elif bmi > 24:

            return ('Obese')

class BmiApp:










blini=Child('Blin',17,70,1.75)

blini.get_info()
