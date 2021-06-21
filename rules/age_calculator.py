class AgeCalculator:
    age: int

    def __init__(self, age):
        self.age = age

    def calculator(self):
        if self.age < 18:
            return 'Your age is under 18.'
