class Parent:
    def __init__(self, hair_colour, eye_colour, age):
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
        self.age = age

    def describe(self):
        return f"Hair colour: {self.hair_colour}, Eye colour: {self.eye_colour}, and Age: {self.age}"
