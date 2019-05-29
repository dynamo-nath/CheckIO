
class Warrior(object):

    def __init__(self, attack=5, health=50, defense=0):
        self.attack = attack
        self.health = health
        self.defense = defense
        self.is_alive = True

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        self.__is_alive = is_alive

    def takeDamage(self, damage):
        self.health -= (damage - self.defense)
        if self.health <= 0:
            self.is_alive = False


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(attack=3, health=60, defense=2)


class Vampire(Warrior):
    def __init__(self):
        self.max_health = 40
        self.vampirism = 2
        super().__init__(attack=4, health=40, defense=0)

    def vampirism_boost(self, opp_defense):
        new_health = (self.health +
                      int((self.attack - opp_defense) / self.vampirism))
        if new_health > self.max_health:
            self.health = self.max_health
        else:
            self.health = new_health


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

            s1 = army1.soldiers[army1Dead]
            s2 = army2.soldiers[army2Dead]
            print(s1.health)
            print(s2.health)
            # army 1 attacks
            if counter % 2 != 0 and army1Dead < len(army1.soldiers):
                (s2.takeDamage(s1.attack))
                if type(s1) == Vampire and s1.health != 0:
                    s1.vampirism_boost(s2.defense)
                if not s2.is_alive:
                    army2Dead += 1
                    counter = 0
                if army2.soldiers[len(army2.soldiers)-1].health <= 0:
                    return True
                
            # army2 attacks
            elif counter % 2 == 0 and army2Dead < len(army2.soldiers):
                (s1.takeDamage(s2.attack))
                if type(s2) == Vampire and s2.health != 0:
                    s2.vampirism_boost(s1.defense)
                if not s1.is_alive:
                    army1Dead += 1
                    counter = 0
                if army1.soldiers[len(army1.soldiers)-1].health <= 0:
                    return False
                
            counter += 1

