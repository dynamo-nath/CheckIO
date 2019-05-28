
class Warrior(object):

    def __init__(self, attack=5, health=50):
        self.attack = attack
        self.health = health
        self.is_alive = True

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        self.__is_alive = is_alive

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        self.defense = 2
        super().__init__(attack=3, health=60)

    def takeDamage(self, damage):
        if damage > self.defense:
            self.health -= (damage - self.defense)
        if self.health <= 0:
            self.is_alive = False


class Army(object):

    def __init__(self):
        self.soldiers = []

    def addUnits(self, soldier, qty):
        for x in range(0, qty):
            self.soldiers.append(soldier())
        return self.soldiers


class Battle(object):

    def fight(self, army1, army2):
        counter = 1
        army1Dead = 0
        army2Dead = 0
        while True:

            # army 1 attacks
            if counter % 2 != 0 and army1Dead < len(army1.soldiers):
                (army2.soldiers[army2Dead]
                    .takeDamage(army1.soldiers[army1Dead].attack))
                a2health = army2.soldiers[army2Dead].health
                if not army2.soldiers[army2Dead].is_alive:
                    army2Dead += 1
                    counter = 0
                if army2.soldiers[len(army2.soldiers)-1].health <= 0:
                    return True
                
            # army2 attacks
            elif counter % 2 == 0 and army2Dead < len(army2.soldiers):
                (army1.soldiers[army1Dead]
                    .takeDamage(army2.soldiers[army2Dead].attack))
                a1health = army1.soldiers[army1Dead].health
                if not army1.soldiers[army1Dead].is_alive:
                    army1Dead += 1
                    counter = 0
                if army1.soldiers[len(army1.soldiers)-1].health <= 0:
                    return False
                
            counter += 1

