from army import Army, Knight, Warrior, Battle

warriors = Army()
warriors.addUnits(Warrior, 3)

knights = Army()
knights.addUnits(Knight, 3)

army_3 = Army()
army_3.addUnits(Warrior, 20)
army_3.addUnits(Knight, 5)

army_4 = Army()
army_4.addUnits(Warrior, 30)

army_5 = Army()
army_5.addUnits(Warrior, 20)

army_6 = Army()
army_6.addUnits(Warrior, 21)

battle = Battle()
print(battle.fight(knights, warriors))
print(battle.fight(army_3, army_4))
print(battle.fight(army_5, army_6))
