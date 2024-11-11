import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, x, y, z, speed):
        self._cords = [x, y, z]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed

        if new_z < 0:
            print("It's too deep, I can't dive :(")
            return

    def get_cords(self):
        print(f'X: {self.x}, Y: {self.y}, Z: {self.z}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = abs(dz) * self.speed / 2
        return


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self):
        self.speak = 'Click-click-click'



db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

# True
# True
# Click-click-click
# Be careful, i'm attacking you 0_0
# X: 10 Y: 20 Z: 30
# X: 10 Y: 20 Z: 0
# Here are(is) 3 eggs for you