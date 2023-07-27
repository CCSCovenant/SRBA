from battle.combat_obj import CombatObj
from battle.toughness import Toughness


class Enemy(CombatObj):

    def __int__(self,
                event_list,
                toughness_length):
        self.toughness = Toughness(toughness_length)
        pass