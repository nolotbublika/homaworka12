class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_power(self):

        return 'hp1'


class Nissan(Vehicle, Car):

    price = 1500000
    vehicle_type = 'sport'

    def horse_power(self):

        return 'hp2'


juke = Nissan()
print(juke. vehicle_type,juke.price)
