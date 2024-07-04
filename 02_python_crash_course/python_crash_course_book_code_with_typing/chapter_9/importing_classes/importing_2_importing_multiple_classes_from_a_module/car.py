"""A set of classes used to represent gas and electric cars"""

class Car:
    """Asimple attampts to represent a car"""
    def __init__(self,make,model,year) -> None:
        """initialize attributes to represent a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def  read_odometer(self):
        """print a statment showing the car's mileage"""
        print(f"this car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        """
        set the odometer read the given value.
        reject the change if it attampts to roll the odometer.
        """    
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")    

    def increment_odometer(self,miles):
        """add the given amount to the odometer reading"""
        self.odometer_reading += miles

class Battery:
    """A simple attampt to modle a battery for an electric car"""
    def __init__(self,battery_size=40) -> None:
        """initialize t battry's attributs"""
        self.battry_size = battery_size

    def describe_battery(self):
        """print a statment describing battery size"""
        print(f"this car has a {self.battry_size}-kwH size")

    def get_range(self):
        """print a statment about the range this battery provides"""    
        if self.battry_size == 40:
            range = 150
        elif self.battry_size == 65:
            range = 225   
        print(f"this car can go about {range} mils on a full charge")     

class Electriccar(Car):
    """model aspects of a car,specific toelectric vehicles"""
    def __init__(self, make, model, year) -> None:
        """
        initialize attributes to a parent class.
        initialize attributs specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery
