#!/usr/bin/env python3

class Car:
    """ A class that represents a car"""

    def __init__(self, brand, model, vin, price):
        self.brand = brand
        self.model = model
        self.vin = vin
        self.price = price

    def __str__(self):
        return f"{self.brand:10} - {self.model:10} - {self.vin:10} - {self.price}"

car_list = [
    ["Peugeot", "2008", "AB-123-BA", "20000"],
    ["Renault", "Megane", "ZZ-222-ZZ", "30000"],
    ["Tesla", "Model 3", "DF-365-FD", "40000"],
    ["Porsche", "Panamera", "FG-345-FD", "100000"],
]

car_instances = []
for (brand, model, vin, price) in car_list:
    car_instances.append(Car(brand, model, vin, price))
    print(f"Created car: {car_instances[-1]}")
