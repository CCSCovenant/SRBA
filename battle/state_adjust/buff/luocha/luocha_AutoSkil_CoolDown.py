from battle.battle_event.event_core.event import EntityEvent
from battle.state_adjust.state_adjust import StateAdjust, STATES
class LuochaAutoSkillCoolDown(StateAdjust):

    CoolDown = 2
    def __init__(self, sourceEntity, targetEntity):
        triggerList = [EntityEvent.CYCLE_END]
        super().__init__(STATES.notRemoveAble, STATES.buff, sourceEntity, targetEntity, triggerList)
        self.CD = 0
    def on_trigger(self,**kwargs):
        self.CD = self.CD - 1

    def should_active(self):
        return self.CD <= 0

    def active(self):
        self.CD = LuochaAutoSkillCoolDown.CoolDown