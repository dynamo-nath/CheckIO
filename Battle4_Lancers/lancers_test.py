import unittest

from lancers import Warrior, Knight, Army, Battle, Defender, Vampire, Lancer


class LancersTesting(unittest.TestCase):

    def test_create_lancer(self):
        result = Lancer

        self.assertEqual(type(Lancer()), result)

    def test_lancer_health(self):
        result = 50

        l = Lancer()
        self.assertEqual(l.health, result)

    def test_lancer_vs_warrior_and_knight(self):
        pass
        

    # def test_1war_4def_vs_3vamp_2war(self):
    #     result = True

    #     b = Battle()
    #     a1 = Army()
    #     a2 = Army()

    #     # a1.addUnits(Warrior, 1)
    #     # a2.addUnits(Vampire, 1)

    #     a1.addUnits(Warrior, 1)
    #     a1.addUnits(Defender, 4)

    #     a2.addUnits(Vampire, 3)
    #     a2.addUnits(Warrior, 2)

    #     self.assertEqual(b.fight(a1, a2), result)