from battle.state_adjust.state_adjust import StateAdjust, STATES


class PermanentBuff(StateAdjust):
    def __init__(self, targetEntity):
        triggerList = []
        super().__init__(STATES.notRemoveAble, STATES.buff, None, targetEntity, triggerList)
        self.applyStatesBuff()

    def applyStatesBuff(self):

        pass
