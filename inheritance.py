class Person:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("Hello my name is {}.".format(self.name))

class Superhero(Person):
    def __init__(self, name, superpower):
        super().__init__(name)
        self.superpower = superpower
    def reveal(self):
        print("Yes, I am {} and do have the power of {}".format(self.name, self.superpower))
