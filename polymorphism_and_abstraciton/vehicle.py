from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self, drive):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        required_fuel = (self.fuel_consumption + 0.9) * distance
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        required_fuel = (self.fuel_consumption + 1.6) * distance
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)
