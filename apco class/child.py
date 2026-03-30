from parent import Parent


class Child(Parent):
    def __init__(self, name, hair_colour, eye_colour, age):
        super().__init__(hair_colour, eye_colour, age)
        self.name = name

    def describe(self):
        base_description = super().describe()
        return f"{self.name} -> {base_description}"

    def get_parent_description(self):
        return super().describe()


class A:
    def __init__(self):
        self.calls = ["A"]


class B(A):
    def __init__(self):
        A.__init__(self)
        self.calls.append("B")


class C(A):
    def __init__(self):
        A.__init__(self)
        self.calls.append("C")


class DProblem(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        self.calls.append("DProblem")


class BetterA:
    def __init__(self):
        self.calls = ["A"]


class BetterB(BetterA):
    def __init__(self):
        super().__init__()
        self.calls.append("B")


class BetterC(BetterA):
    def __init__(self):
        super().__init__()
        self.calls.append("C")


class DFixed(BetterB, BetterC):
    def __init__(self):
        super().__init__()
        self.calls.append("DFixed")


if __name__ == "__main__":
    child = Child("Avery", "brown", "green", 12)
    print("Child class test:")
    print(child.describe())
    print("Parent function called from child:")
    print(child.get_parent_description())
    print()

    print("Diamond issue example (direct parent calls):")
    problem = DProblem()
    print(problem.calls)
    print("Notice B is lost because A is initialized twice and resets shared state.")
    print()

    print("Diamond fixed example (using super and MRO):")
    fixed = DFixed()
    print(fixed.calls)
    print("A appears once because MRO handles shared ancestors correctly.")
