#Program to show Inheritance in python: calculating bus fare with the amount
# returned by Vehicle (parent) class

class Vehicle:
    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity*100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount*10 /100
        return amount

name = input("Enter the name of the bus: ")
mileage = float(input("Enter mileage of the bus: "))
capacity = float(input("Enter capacity of the bus: "))

bus_A =Bus(name,mileage,capacity)
print(f'''Total Bus fare of the bus: {name},
with mileage {mileage} L/Km,
and capacity of {capacity} Litres = Rs.''',
bus_A.fare())
