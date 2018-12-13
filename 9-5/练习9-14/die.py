from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides = sides
        self.one = 1
    def roll_die(self):
        x = randint(self.one,self.sides)
        print(x)
    def read_die(self,sides2):
        self.sides = sides2
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(
            str(self.sides) +
            "面骰子投掷10次:"
        )
        for self.number in self.numbers:
            self.roll_die()