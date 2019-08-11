class Car:
    """ Objectice is to create a Car class which contains the owner's name, miles to drive and fuel required for driving.
    Initally, the car has no fuel therefore it needs to be refilled.
    Once refilled, the car can drive upto the required miles.
    In case, there is not enough fuel to complete the miles, an indication will appear saying how much more is needed to be refilled.

    The car can also refill from another car in case of an emergency if there is no petrol pump.
    """
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.miles = 0
        self.fuel = 0
    
    def drive(self, miles):
        fuel_req = miles * 3

        if self.fuel == 0:
            print(self.owner_name, "your fuel is", self.fuel, "Please refill.")
        elif self.fuel < fuel_req:
            print(self.owner_name, "you do not have enough fuel, you require", (fuel_req - self.fuel), "more for driving.")
        else:
            self.miles += miles
            self.fuel -= fuel_req
            print(self.owner_name, "you have driven", self.miles, "miles. The fuel is now", self.fuel)
        
    def refill(self, fuel):
        self.fuel += fuel
        print(self.owner_name, "you have refilled", fuel, "and your current fuel is", self.fuel)

    def transfer_from(self, another_car, fuel):
        self.fuel += fuel
        print(self.owner_name, "you have refilled", fuel, "and your current fuel is", self.fuel)
        another_car.transfer_to(fuel)

    def transfer_to(self, fuel):
        self.fuel -= fuel
        print(self.owner_name, "your fuel is now", self.fuel)


car_1 = Car('Stephen')
car_1.drive(10) # Stephen your fuel is 0 Please refill.
car_1.refill(20) # Stephen you have refilled 20 and your current fuel is 20
car_1.drive(10) # Stephen you do not have enough fuel, you require 10 more for driving.
car_1.refill(10) # Stephen you have refilled 10 and your current fuel is 30
car_1.drive(10) # You have driven 10 miles. The fuel is now 0

car_2 = Car('Jude')
car_2.refill(50) # Jude you have refilled 50 and your current fuel is 50

car_1.transfer_from(car_2, 10)
# Stephen you have refilled 10 and your current fuel is 10
# Jude your fuel is now 40