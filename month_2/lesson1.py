

class CAR:
    def __init__(self, color, model):
        self.color = color
        self.model = model


car_camry = CAR ("black", "camry")
print(car_camry.model, car_camry.color)

class diesel (CAR):
    def __init__(self):
        self.color = "green"
        self.bio = "bio"



