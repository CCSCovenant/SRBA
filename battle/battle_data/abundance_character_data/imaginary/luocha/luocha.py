from battle.character import Character


class Luocha(Character):

    def __init__(self,level,trace_set,relics,light_cone):
        super().__init__("罗刹",level,trace_set,relics,light_cone)


    def normal_attack(self, target):
        """
        罗刹普通攻击
        :param target: combat_obj 对象
        """
        #罗刹普攻三段攻击 分裂比为 0.3，0.3，0.4 攻击力倍率


    def skill_attack(self,target):
        """
        罗刹战技
        :param target: combat_obj 对象
        """

        pass




