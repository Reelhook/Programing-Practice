class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, manufacturer, year):
        """Intialize attributes to describe a car."""
        self.make = make
        self.manufacturer = manufacturer
        self.year = year

    def getdescriptionName(self):
        """Return a neatly formatted description name."""
        longName = f"{self.make} {self.manufacturer} {self.year}"
        return longName.title()


my_new_car = Car("jeep", "gladiator", 2021)
print(my_new_car.getdescriptionName())
