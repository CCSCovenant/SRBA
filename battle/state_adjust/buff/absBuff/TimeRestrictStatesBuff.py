"""
抽象类
这类buff 是持续 N个回合的数值加成类buff.
"""
from battle.battle_event.event_core.event import EntityEvent
from battle.state_adjust.state_adjust import StateAdjust, STATES


class TimeRestrictStatesBuff(StateAdjust):

    def __init__(self, sourceEntity, targetEntity,TIME):
        triggerList = [EntityEvent.CYCLE_END]
        super().__init__(STATES.RemoveAble, STATES.buff, sourceEntity, targetEntity, triggerList)
        self.applyStatesBuff()
        self.TIME = TIME

    def applyStatesBuff(self):
        pass

    def on_trigger(self,**kwargs):
        self.TIME = self.TIME - 1
        if self.TIME <= 0:
            self.remove_self()