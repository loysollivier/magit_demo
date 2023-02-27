#!/usr/bin/env python3
import random
import string

class Car:
    """ A class that represents a car"""

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        letters = ''.join(random.sample(string.ascii_uppercase,2))
        number = random.randint(0,999)
        self.vin = f"{letters}-{number:03}-{letters[::-1]}"
        self.price = price

    def __str__(self):
        return f"{self.brand:10} - {self.model:10} - {self.vin:10} - {self.price}"

car_list = [
    ["Peugeot", "2008", "20000"],
    ["Renault", "Megane", "30000"],
    ["Tesla", "Model 3", "40000"],
    ["Porsche", "Panamera", "100000"],
    ["Fiat", "Punto", "8000"],
]

car_instances = []
for (brand, model, price) in car_list:
    car_instances.append(Car(brand, model, price))
    print(f"Created car: {car_instances[-1]}")
