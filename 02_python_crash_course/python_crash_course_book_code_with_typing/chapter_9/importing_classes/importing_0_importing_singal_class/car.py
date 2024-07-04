"""A class that can be used to represent a car"""

class Car:
    """A simple attampt to represent a car"""

    def __init__(self,make,modle,year) -> None:
        """Initialize attributes to describe a car"""
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name:str = f"{self.make} {self.modle} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statment showing the cars mileage""" 
        print(f"this car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        """
        set the odometer reading to the given value.
        reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer") 

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading+= miles          
