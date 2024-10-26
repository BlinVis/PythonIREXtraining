class Vehicles:
    def __init__(self,maker,model ,year):
        self.maker=maker
        self.model=model
        self.year=year
    def display_info(self):
        print(f'maker:{self.maker}, model:{self.model}, year:{self.year}')

class Car(Vehicles):
    def __init__(self,maker,model,year,body_style):
        super().__init__(maker,model,year)
        self.body_style=body_style

class ElectricCar(Car):
    def __init__(self,maker,model,year,body_style,battery_capacity):
       super().__init__(maker,model,year,body_style)
       self.battery_capacity=battery_capacity
    def charge(self):
        print(f'Charging the electric car')

tesla=ElectricCar('tesla','Cybertruck',2017,'Triangular',112.2)
print(tesla.charge())

