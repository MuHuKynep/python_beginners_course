my_string ="Hello, world!"
print(type(my_string))
print(type(str))

class MyClass:
    pass
print(type(MyClass))

my_class = MyClass()
print(type(my_class))


class Ork:
    def __init__(self, level:int) ->None:
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 100 * level

    def attack(self):
        print(f'Ork attaks with {self.attack_power} power')

ork = Ork(level=2)
print(ork.attack_power)

ork.attack()
