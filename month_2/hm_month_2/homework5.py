class Distance:
    conversation_to_metrs = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
    }

    def __init__(self, value, unit):
        if unit not in self.conversation_to_metrs:
            raise ValueError(f"Unknown unit")
        self.unit = unit
        self.value = value

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self.conversation_to_metrs[self.unit]

    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError(f"не верные значения")

        total_meters = self.to_meters() + other.to_meters()
        return Distance(total_meters, "m")

d = Distance(10, "km")
d2 = Distance(500, "m")
result = d + d2

print(d)
print(d2)
print(result)