class Cleaner:
    def clean(self):
        print("Cleaning...")

class Pooper:
    def poop(self):
        print("Pooping...")

class Eater:
    def eat(self):
        print("Eating...")

class Housemate:
    def __init__(self, name, eater=None, pooper=None, cleaner=None):
        self.name = name
        self.eater = eater
        self.pooper = pooper
        self.cleaner = cleaner
