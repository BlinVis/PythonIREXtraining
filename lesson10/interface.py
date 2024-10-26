from abc import ABC, abstractmethod
class Printable():
    @abstractmethod
    def print_info(self):
        pass

class Books(Printable):
    def __init__(self,name,author):
        self.name=name
        self.author=author
    def print_info(self):
        print(f'{self.name} was written by {self.author}')
        