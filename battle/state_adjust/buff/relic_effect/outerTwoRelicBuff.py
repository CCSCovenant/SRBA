from battle.state_adjust.buff.absBuff.PermanentBuff import PermanentBuff


class outerTwoRelicBuff(PermanentBuff):

    def __init__(self,targetEnttiy):
        super.__init__(targetEnttiy)

    def applyStatesBuff(self):
        #TODO 根据遗器RID从JSON解析需要提升的属性和对应数值
        pass

