# -*- coding: utf-8 -*-
"""WEEK IV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KocgZGeITO3hrhZLr9J36V-1lI_isJWn
"""

#1
class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
        
car = vehicle(120,20 )
print(car.max_speed, car.mileage)

#2
class vehicle:
    pass

#3

class vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(vehicle):
    pass

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def bus_seating_capacity(self, capacity):
        return capacity

class Bus(Vehicle):
    
    def seating_capacity(self, capacity=50):
        return super().bus_seating_capacity(capacity=50)
bus = Bus("Tesla", 180, 20)
print(bus.seating_capacity())

class vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def busfare(self):
        return self.capacity * 100

class Bus(vehicle):
    def busfare(self):
        amount = super().busfare()
        amount += amount * 10 / 100
        return amount

bus = Bus("Tesla", 10, 40)
print("Total Bus fare is:", bus.busfare())