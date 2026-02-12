


class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def introduce(self):
        print(f"привет! меня зовут {self.name}. мне {self.age}"
              f"моя профессия - {self.profession}")

class Classmate(Person):
    def __init__(self, name, age, profession, class_group, person):
        super().__init__( name, age, profession )
        self.class_group = class_group
        self.person = person
    def introduce(self):
        print(f"привет! Я {self.name}, мне {self.age} лет. "
        f"учусь в группе {self.class_group} с {self.person.name}. будущая профессия — {self.profession}.")

class Friend(Person):
    def __init__(self, name, age, profession, hobby, person):
        super().__init__( name, age, profession)
        self.hobby = hobby
        self.person = person
    def introduce(self):
        print(f"привеь! я {self.name},я друг {self.person.name} мне {self.age} лет. моя профессия - {self.profession}"
              f"в свободнее время занимаюсь {self.hobby}")

person1 = Person ("Айдар", 19, "программист")
friend1 = Friend ("Бека", 20, "экономист", "скачки", person1)
people = [person1, friend1]
friend1.introduce()
for i in people:
    i.introduce()