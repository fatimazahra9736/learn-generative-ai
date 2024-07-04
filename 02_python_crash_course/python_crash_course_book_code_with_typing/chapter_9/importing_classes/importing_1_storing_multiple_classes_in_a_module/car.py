"""A set of classes used to represent gas and electric cars"""
class Car:
    """A simple attampt to represent a car"""

    def __init__(self,make,model,year):
        """initialize attrebutes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a formatted descriptive name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """print a statment showing the cars mileage"""
        print(f"this car has {self.odometer_reading} on it")

    def update_odometer(self,mileage):
        """
        set the odometer reading to the given value.
        reject the chane if it attamps to roll the odometer back.
        """
        if mileage>= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("you can't roll back an odometer")
    
    def increament_odometer(self,miles):
        self.odometer_reading += miles

class Battery:
    """A simple attamp to modle a battery for an electric car"""

    def __init__(self,battery_size = 40) -> None:
        """initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statment describing battery size"""
        print(f"this car has a{self.battery_size}-KWH battery")

    def get_range(self):
        """print a statment about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"this car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """modles aspects of a car,specific to electric vehicles"""
    def __init__(self,make,model,year) -> None:
        """
        initialize attributes of a parent class.
        initialize attributes specific to an electric car.
        """
        super().__init__(make,model,year)
        self.battery = Battery()
