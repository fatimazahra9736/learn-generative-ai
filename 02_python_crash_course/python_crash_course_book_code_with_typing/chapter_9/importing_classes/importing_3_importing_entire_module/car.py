class Car:
    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptiv_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} on it")
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")    

    def incerement_odometer(self,miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self,battery_size = 40) -> None:
        self.battery_size = battery_size
    
    def describ_battery(self):
        print(f"this battery has a {self.battery_size}-KWH size")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225 
        print(f"this car can go about {range} miles on a full charge")

class Electriccar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery