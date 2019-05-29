
class Warrior(object):

    def __init__(self, attack=5):
        self.health = 50
        self.attack = attack
        self.is_alive = True

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        self.__is_alive = is_alive

    # from CheckIO solution
    # @property
    # def is_alive(self):
    #     return True if self.health > 0 else False

    def attackDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


def fight(unit_1, unit_2):
    counter = 1
    while True:
        if (counter % 2 == 0):
            unit_1.attackDamage(unit_2.attack)
            if not unit_1.is_alive:
                return False
        else:
            unit_2.attackDamage(unit_1.attack)
            if not unit_2.is_alive:
                return True
        counter += 1


me = Warrior()
bob = Knight()
fight(me, bob)
print(me.is_alive)
print(bob.is_alive)
