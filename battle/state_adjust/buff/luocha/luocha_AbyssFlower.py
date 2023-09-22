from battle.battle_event.event_core.event import EntityEvent
from battle.state_adjust.state_adjust import StateAdjust, STATES


class LuochaAbyssFlower(StateAdjust):
    CYCLE_TIME = 2
    def __init__(self,sourceEntity,targetEntity):
        triggerList = [EntityEvent.SKILL_ATTACK,EntityEvent.ULT_ATTACK,EntityEvent.CYCLE_END]
        super().__init__(STATES.notRemoveAble,STATES.buff,sourceEntity,targetEntity,triggerList)
        self.counter = 0
        self.time_remain = 0
        self.active = False

    def on_trigger(self,**kwargs):
        if "EventType" not in kwargs:
            raise ValueError("on_trigger requires 'EventType' arguments.")
        EventType = kwargs["EventType"]

        if EventType == EntityEvent.SKILL_ATTACK or EntityEvent.ULT_ATTACK:
            if self.active:
                pass
            else:
                self.counter = self.counter + 1
                if self.counter == 2:
                    self.active = True
                    self.time_remain =LuochaAbyssFlower.CYCLE_TIME
                    self.deploy_cycle_of_life()
        else:
            if self.active:
                self.time_remain = self.time_remain - 1
                if self.time_remain == 0:
                    self.active = False
                    self.counter = 0
            else:
                pass

    def deploy_cycle_of_life(self):
        GameManager = self.sourceEntity.GameManager
        #TODO 为全体施加结界效果

    def remove_cycle_of_life(self):
        GameManager = self.sourceEntity.GameManager
        #TODO 移除所有结界效果


