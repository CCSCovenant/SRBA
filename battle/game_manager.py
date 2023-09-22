from battle.cycle import Cycle


class GameManager:

    def __init__(self, Character_List, Enemy_List, Spec_Event_List,decision_AI):
        self.Spec_Event_List = Spec_Event_List
        self.Character_List = Character_List
        self.Enemy_List = Enemy_List
        self.decision_AI = decision_AI

        self.GAME_END = False
        self.movement_list = []
        self.triggers = {}

        for character in self.Character_List:
            self.movement_list.append(Cycle(character))

        for enemy in self.Enemy_List:
            self.movement_list.append(Cycle(enemy))

        pass
    def main_loop(self):
        while(not self.GAME_END):
            cycle = min(self.movement_list)
            decision_space = cycle.decision_space()
            #Agent决策
            decision = 0
            ultCycle = cycle.process(decision)
            if ultCycle is not None:
                self.movement_list.append(ultCycle)
    def remove_cycle(self,cycle):
        self.movement_list.remove(cycle)
    def init_event(self):
        pass

    def summon_enemy(self):
        pass

    def remove_enemy(self):
        pass
