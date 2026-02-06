class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def introduce(self):
        print(f"привет! меня зовут {self.name}. мне {self.age}"
              f"моя профессия - {self.profession}")

class Classmate(Person):
    def __init__(self, name, age, profession, class_group):
        super().__init__(self, name, age, profession )
        self.class_group = class_group
    def introduce(self):
        f"привет! Я {self.name}, мне {self.age} лет. "
        f"учусь в группе {self.class_group}. будущая профессия — {self.profession}."

