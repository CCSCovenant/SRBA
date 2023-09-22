from battle.battle_event.event_core.event import EntityEvent
from battle.state_adjust.state_adjust import StateAdjust, STATES


class LuochaAutoSkill(StateAdjust):

    def __init__(self,sourceEntity,targetEntity):
        triggerList = [EntityEvent.HP_CHANGE]
        super().__init__(STATES.notRemoveAble,STATES.buff,sourceEntity,targetEntity,triggerList)


    def on_trigger(self,**kwargs):
        counter = self.sourceEntity.get_auto_skill_counter
        if counter.should_active():
            self.sourceEntity.skill_attack(self.targetEntity)
            counter.active()



