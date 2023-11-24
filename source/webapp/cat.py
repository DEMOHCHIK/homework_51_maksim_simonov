import random


class Cat:
    def __init__(self):
        self.name = None
        self.age = 1
        self.happiness = 40
        self.satiety = 40
        self.sleeping = False

    def set_name(self, name):
        self.name = name

    def feed(self):
        if not self.sleeping:
            self.satiety += 15
            self.happiness += 5
            if self.satiety > 100:
                self.happiness -= 30

    def play(self):
        if not self.sleeping:
            self.happiness += 15
            self.satiety -= 10
            if random.randint(1, 3) == 1:
                self.happiness = 0
        else:
            self.sleeping = False
            self.happiness -= 5

    def sleep(self):
        self.sleeping = True
        self.happiness += 10

    def check_state(self):
        if self.satiety > 100:
            self.satiety = 100
            self.happiness -= 30
        elif self.satiety < 0:
            self.satiety = 0
        if self.happiness < 0:
            self.happiness = 0
        elif self.happiness > 100:
            self.happiness = 100