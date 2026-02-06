class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            edu = "у меня есть высшее образование"
        else:
            edu = "у меня нет высшего образования"

        print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии я {self.occupation}, {edu}.")


person1 = Person("Ади", "12.05.2005", "программист", True)
person2 = Person("Айбек", "03.11.2000", "дизайнер", False)
person3 = Person("Мира", "25.08.1998", "врач", True)

print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

print()

person1.introduce()
person2.introduce()
person3.introduce()