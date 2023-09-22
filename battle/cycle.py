from enum import Enum


class Cycle:
    def __init__(self,Entity,CycleType):
        self.Entity = Entity
        self.CycleType = CycleType
        self.Timer = Entity.Timer



    def decision_space(self):
        """

        :return:
        """
        pass


    def process(self,decision):


        #如果是插入回合
        if self.CycleType is CycleType.SPECIAL or CycleType.ULT:
            self.Entity.GameManager.remove_cycle(self)

    def __lt__(self, other):
        """重载小于运算符"""
        if self.CycleType is CycleType.SPECIAL or CycleType.ULT:
            return True
        return self.Timer.next_move_time < other.Timer.next_move_time

class CycleType(Enum):
    NORMAL = 0
    ULT = 1
    SPECIAL = 2