from battle.battle_event.event_core.event import EntityEvent
from battle.state_adjust.state_adjust import StateAdjust


class LuochaPerimeter(StateAdjust):

    def __init__(self,sourceEntity,targetEntity):
        targetedList = [EntityEvent.FOLLOW_UP_ATTACK,EntityEvent.NORMAL_ATTACK,EntityEvent.SKILL_ATTACK,EntityEvent.ULT_ATTACK]
        super().__init__(1,0,sourceEntity,targetEntity,targetedList)
        #TODO 检查罗刹的天赋
        self.heal_all = True
        self.heal_all_radio = 0.07
        self.heal_all_add = 93
        #TODO 检查罗刹天赋倍率
        self.heal_single_radio = 0
        self.heal_single_add = 0

    def on_trigger(self,EventType):
        baseValue = self.sourceEntity.Attack
        self.targetEntity.heal(baseValue*self.heal_single_radio+self.heal_single_add)
        #TODO 基于罗刹(sourceEntity)的攻击力 从GameManger获得所有除targetEntity以外的角色并治疗


        pass


