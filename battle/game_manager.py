class GameManager:

    def __init__(self, Character_List, Enemy_List, Spec_Event_List,decision_AI):
        self.Spec_Event_List = Spec_Event_List
        self.Character_List = Character_List
        self.Enemy_List = Enemy_List
        self.decision_AI = decision_AI

        self.GAME_END = False
        self.movement_list = []
        self.immediate_turn = []
        self.triggers = {}

        for character in self.Character_List:
            self.movement_list.append(character.Timer)

        for enemy in self.Enemy_List:
            self.movement_list.append(enemy.Timer)

        pass
    def main_loop(self):
        while(not self.GAME_END):
            '''
            角色行动() <-
            
            检查是否有插入回合
                执行插入回合
                           
            '''
            self.next_round()
            while len(self.immediate_turn > 0):
                self.process_immediate_turn(self.immediate_turn.pop())
            pass

    def process_immediate_turn(self):
        '''
        回合前事件检查
        (回合开始效果)
        '''
        pass
    def next_round(self):
        """

        :return:
        """

        '''
        回合前事件检查
        (持续伤害 回合开始效果)
        '''
        next_timer = min(self.movement_list)
        decisions = self.decision_AI.decide()
        self.apply_decision(decisions)

        '''
        回合后事件检查
        (结算buff/debuff)
        '''
        next_timer.move()



        pass

    def apply_decision(self,decisions):
        pass
    def init_event(self):
        pass

    def summon_enemy(self):
        pass

    def remove_enemy(self):
        pass
