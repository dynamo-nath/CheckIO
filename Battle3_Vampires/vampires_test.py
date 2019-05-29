import unittest

from vampires import Warrior, Knight, Army, Battle, Defender, Vampire


class VampiresTesting(unittest.TestCase):

    def test_create_vampire(self):
        result = Vampire

        self.assertEqual(type(Vampire()), result)

    def test_vampire_health(self):
        result = 40

        v = Vampire()
        self.assertEqual(v.health, result)

    def test_vampire_vs_defender(self):
        result = False

        b = Battle()
        a1 = Army()
        a1.addUnits(Vampire, 1)
        a2 = Army()
        a2.addUnits(Defender, 1)

        self.assertEqual(b.fight(a1, a2), result)

    def test_1war_4def_vs_3vamp_2war(self):
        result = True

        b = Battle()
        a1 = Army()
        a2 = Army()

        # a1.addUnits(Warrior, 1)
        # a2.addUnits(Vampire, 1)

        a1.addUnits(Warrior, 1)
        a1.addUnits(Defender, 4)

        a2.addUnits(Vampire, 3)
        a2.addUnits(Warrior, 2)

        self.assertEqual(b.fight(a1, a2), result)


b = Battle()
a1 = Army()
a2 = Army()

a1.addUnits(Warrior, 1)

a2.addUnits(Vampire, 1)

print(b.fight(a1, a2))
