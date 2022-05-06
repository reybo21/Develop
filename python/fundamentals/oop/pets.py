

class Pet:

    def __init__(self, name, type, tricks = []):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0

    def sleep(self):
        print ("I'm a basic pet...I don't sleep")
        self.energy += 25

    def eat(self):
        print ("I'm a basic pet...I just eat air.")
        self.energy += 5
        self.health += 10

    def play(self):
        print ("I'm a basic pet...I just play with myself.")
        self.health += 5

    def noise(self):
        print ("I'm a basic pet...I make no noise.")


class Dog(Pet):

    def __init__(self, name, type, tricks):
        Pet.__init__(self,name, type, tricks)

    def sleep(self):
        print ("When I sleep, I sleep with my legs up in the air")
        self.energy += 500

    def eat(self):
        print ("When I eat, I nom nom my food all over the place")
        self.energy += 50
        self.health += 75

    def play(self):
        print ("BALL BALL BALL BALL BALL!!!")
        self.energy -= 10

    def noise(self):
        print ("Woof Woof Woof")


class Cat(Pet):

    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)

    def sleep(self):
        print ("When I sleep, I sleep with my legs up in the air")
        self.energy += 500
