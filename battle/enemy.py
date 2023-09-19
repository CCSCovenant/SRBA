from battle.combatEntity import CombatEntity
from battle.toughness import Toughness


class Enemy(CombatEntity):

    def __init__(self,
                event_list,
                toughness_length):
        self.toughness = Toughness(toughness_length)
        pass