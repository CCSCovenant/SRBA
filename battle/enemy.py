from battle.combatEntity import CombatEntity
from battle.toughness import Toughness


class Enemy(CombatEntity):

    def __init__(self,
                event_list,
                toughness_length):
        self.toughness_length = toughness_length
        self.current_toughness_length = toughness_length
        pass


    def on_attack(self):
        pass


    def toughness_recover(self):
        self.current_toughness_length = self.toughness_length
        pass

