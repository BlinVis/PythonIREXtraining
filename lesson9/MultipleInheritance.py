

class Vertebrate:
    def __init__(self,backBone=True):
        self.has_backbone=backBone
    def vertebrate_info(self):
        print(f'Vertebrates have a backbone')

class Aquatic:
    def __init__(self,habitat='Water'):
        self.habitat=habitat
    def aquatic_info(self):
        print(f'Aquatics live in water')

class Fish(Vertebrate,Aquatic):
    def __init__(self,species,backbone=True,habitat='Water'):
        super().__init__(backBone=backbone)
        self.habitat=habitat
        self.species=species
    def swim(self):
        print(f'this fish is swimming')

goldfish=Fish('golden fish')
goldfish.swim()
print(goldfish.has_backbone)
