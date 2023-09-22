from battle.battle_event.event_core.event import EntityEvent
from battle.state_adjust.state_adjust import StateAdjust, STATES


class BronyaAttackBoost(StateAdjust):
    def __init__(self, sourceEntity, targetEntity):
        triggerList = [EntityEvent.CYCLE_END]
        super().__init__(STATES.notRemoveAble, STATES.buff, sourceEntity, targetEntity, triggerList)
        # TODO 获取布洛妮娅天赋拉条数值
        self.boost = -10
    def on_trigger(self,**kwargs):
        self.sourceEntity.Timer.change_distance(self.boost)
        self.remove_self()
