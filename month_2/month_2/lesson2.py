class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print(f"car {self.model} is driving to {destination}" )

class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

    def drive_to(self, destination):
        print(f"bus {self.model} is driving to {destination}")

class Truck(Car):
    pass

car_subaru = Car ("silver", "forester")
print(car_subaru.model)
car_subaru.drive_to("bishkek")
bus_42 = Bus ("green", "MAN", 42)
print(bus_42.model)
print(bus_42.drive_to)
