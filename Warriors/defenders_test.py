import unittest

from defenders import Warrior, Knight, Army, Battle, Defender


class DefendersTesting(unittest.TestCase):

    def test_create_defender(self):
        result = Defender

        self.assertEqual(type(Defender()), result)

    def test_defender_health(self):
        result = 60

        d = Defender()
        self.assertEqual(d.health, result)

    def test_defender_vs_warrior(self):
        result = True

        b = Battle()
        a1 = Army()
        a1.addUnits(Defender, 1)
        a2 = Army()
        a2.addUnits(Warrior, 1)

        self.assertEqual(b.fight(a1, a2), result)

    def test_defender_vs_2_warrior(self):
        result = False

        b = Battle()
        a1 = Army()
        a1.addUnits(Defender, 1)

        a2 = Army()
        a2.addUnits(Warrior, 2)

        self.assertEqual(b.fight(a1, a2), result)

    def test_1_warrior_1_defender_vs_2_warrior(self):
        result = True

        b = Battle()
        a1 = Army()
        a1.addUnits(Warrior, 1)
        a1.addUnits(Defender, 1)

        a2 = Army()
        a2.addUnits(Warrior, 2)

        self.assertEqual(b.fight(a1, a2), result)

