from battle.character import Character
from battle.combatEntity import ToughnessReduce, InteractMethod, DamageType
from battle.damage_manager import attack


class Bronya(Character):

    def __init__(self,level,trace_set,relics,light_cone):
        super().__init__("布洛妮娅",level,trace_set,relics,light_cone)


    def normal_attack(self, targetSet):
        """
        布洛妮娅普通攻击
        :param target: combat_obj 对象
        """
        current_target = targetSet.target
        attack_value = self.Attack
        radio = 1
        #TODO  读取布洛妮娅普攻倍率
        base_damage = attack_value*radio
        #TODO 检查布洛妮娅行迹1
        hasTrace = True
        #普攻必定暴击
        if hasTrace:
            self.CriticalChance = self.CriticalChance + 1.0
        attack(base_damage, DamageType.WIND, InteractMethod.NormalAttack, self, current_target, ToughnessReduce.Normal, [1])
        if hasTrace:
            self.CriticalChance = self.CriticalChance - 1.0
        #TODO 先人一步实现

    def skill_attack(self,targetSet):
        """
        布洛妮娅战技
        :param target: combat_obj 对象
        """
        current_target = targetSet.target
        attack_value = self.Attack
        radio = 1
        # TODO 读取罗刹战技治疗倍率
        base_heal = attack_value * radio
        heal(base_heal,InteractMethod.SkillAttack,self,current_target)

        # TODO 判断trace_set是否点了行迹2（战技解控）
        current_target.remove_current_debuff()

    def ult_attack(self,targetSet):
        targets = targetSet.targets

        attack_value = self.Attack
        radio = 1
        # TODO 读取罗刹终结技倍率
        base_damage = attack_value * radio
        for target in targets:
            attack(base_damage, DamageType.IMAGINARY, InteractMethod.NormalAttack, self, target, ToughnessReduce.ULT_ALL ,1)
            target.remove_current_buff()