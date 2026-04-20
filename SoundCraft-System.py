from abc import ABC, abstractmethod
from os import name
class Instrument(ABC):
    num_of_instruments = 0
    instrument = []
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
        Instrument.num_of_instruments += 1

    @abstractmethod
    def play(self):
        pass
    def display_info(self):
        print(f"Name: {self.name}, Brand: {self.brand}, Price: ${self.price}")    

    @abstractmethod
    def get_material(self):
        pass

    @abstractmethod
    def repair(self):
        pass

    @abstractmethod
    def clean(self):
        pass

class Guitar(Instrument):
    def __init__(self,name,price,brand,num_of_strings):
        super().__init__(name,brand,price)
        self.num_of_strings = num_of_strings

    def get_material(self):
        return "Wood"
    
    def repair(self):
        print(f"Repairing the {self.name}.")

    def clean(self):
        print(f"Cleaning the {self.name}.")    
    
    def play(self):
        print(f"Playing the {self.name} with {self.num_of_strings} strings.")

class Piano(Instrument):
    def __init__(self,name,price,brand,num_of_keys):
        super().__init__(name,brand,price)
        self.num_of_keys = num_of_keys

    def get_material(self):
        return "Wood and Metal"
    
    def repair(self):
        print(f"Repairing the {self.name}.")

    def clean(self):
        print(f"Cleaning the {self.name}.")    
    
    def play(self):
        print(f"Playing the {self.name} with {self.num_of_keys} keys.")

class Drums(Instrument):
    def __init__(self,name,price,brand,num_of_drums):
        super().__init__(name,brand,price)
        self.num_of_drums = num_of_drums

    def get_material(self):
        return "Wood and Plastic"
    
    def repair(self):
        print(f"Repairing the {self.name}.")

    def clean(self):
        print(f"Cleaning the {self.name}.")    
    
    def play(self):
        print(f"Playing the {self.name} with {self.num_of_drums} drums.")

class Violin(Instrument):
    def __init__(self,name,price,brand,num_of_strings):
        super().__init__(name,brand,price)
        self.num_of_strings = num_of_strings

    def get_material(self):
        return "Wood"
    
    def repair(self):
        print(f"Repairing the {self.name}.")

    def clean(self):
        print(f"Cleaning the {self.name}.")    
    
    def play(self):
        print(f"Playing the {self.name} with {self.num_of_strings} strings.")

class Flute(Instrument):
    def __init__(self,name,price,brand,length):
        super().__init__(name,brand,price)
        self.length = length

    def get_material(self):
        return "Metal"
    
    def repair(self):
        print(f"Repairing the {self.name}.")

    def clean(self):
        print(f"Cleaning the {self.name}.")    

    def play(self):
        print(f"Playing the {self.name} with length {self.length} cm.")


    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: ${self.price}")

class add_instrument():
    def add_instrument(self,instrument):
        Instrument.instrument.append(instrument)
        print(f"{instrument.name} added to the system.")

class show_all():
    def show_all(self):
        if not Instrument.instrument:
            print("No instruments in the system.")
            return
        print("All Instruments in the System:")
        for instrument in Instrument.instrument:
            instrument.display_info()

# Example usage
g1 = Guitar("Guitar", 1000, "Yamaha", 6)
p1 = Piano("Piano", 5000, "Casio", 88)
d1 = Drums("Drums", 2000, "Pearl", 5)
v1 = Violin("Violin", 1500, "Stradivarius", 4)
f1 = Flute("Flute", 800, "Yamaha", 30)

print("== adding instruments to the system ==")
print()
manager = add_instrument()

manager.add_instrument(g1)
manager.add_instrument(p1)
manager.add_instrument(d1)
manager.add_instrument(v1)
manager.add_instrument(f1)
print()

print("== showing all instruments in the system ==")
print()
viewer = show_all()
viewer.show_all()

print("== playing all instruments ==")
print()
for inst in Instrument.instrument:
    inst.play()

print("== repairing and cleaning all instruments ==")
print()
for inst in Instrument.instrument:
    inst.repair()
    inst.clean()

print("== total number of instruments in the system ==")
print("Total instruments:", Instrument.num_of_instruments)

print("== displaying information of all instruments ==")
print()

for inst in Instrument.instrument:
    inst.display_info()

print("== displaying material of all instruments ==")
print()
for inst in Instrument.instrument:
    print(f"{inst.name} is made of {inst.get_material()}.")
