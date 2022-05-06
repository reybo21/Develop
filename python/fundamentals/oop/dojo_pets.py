import pets


class Ninja:

    def __init__(self, first_name, last_name,treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()


spicy = pets.Cat('spicy', 'golden lab', ['beg','dance','sit','lay'])
phil = Ninja('phil', 'collins', 5, 10, spicy)

print(spicy.health)
print(spicy.energy)

spicy.sleep()
phil.feed()
phil.walk()
phil.bathe()

print(spicy.health)
print(spicy.energy)
