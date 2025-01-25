from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
        super().__init__()
    def move(self, dx, dy, dz):
        if  self._cords[2] + self.speed * dz < 0:
            print('It\'s too deep, I can\'t dive :(')
        else:
            d = [dx, dy, dz]
            for i in range(0, 3):
                self._cords[i] = self._cords[i] + self.speed * d[i]
    def get_cord(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}.')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Sorry, I\'m peaceful :(')
        else:
            print('Be careful, I\'m attacking you 0_0')
    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True
    def __init__(self, speed):
        super().__init__(speed)
    def lay_eggs(self):
        eggs_count = randint(1, 5)
        if eggs_count == 1:
            print(f'Here is {eggs_count} egg for you.')
        else:
            print(f'Here are {eggs_count} eggs for you.')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - int(self.speed / 2 * abs(dz))

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    
class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed):
        self.sound = 'Click-click-click'
        super().__init__(speed)

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cord()
db.dive_in(6)
db.get_cord()
db.lay_eggs()
