class Parent2:
    def __init__(self, hair_colour, eye_colour, age):
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
        self.age = age


class Child2(Parent2):
    def __init__(self, name, hair_colour, eye_colour, age):
        super().__init__(hair_colour, eye_colour, age)
        self.name = name

    def describe(self):
        return (
            f"{self.name} has hair colour {self.hair_colour}, "
            f"eye colour {self.eye_colour}, and is {self.age} years old."
        )
