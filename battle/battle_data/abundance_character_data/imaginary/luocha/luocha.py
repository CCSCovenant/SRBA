from battle.character import Character
from battle.combatEntity import DamageType, InteractMethod, ToughnessReduce
from battle.damage_manager import attack, heal
from battle.state_adjust.buff.luocha.luocha_AutoSkil_CoolDown import LuochaAutoSkillCoolDown


class Luocha(Character):

    def __init__(self,level,trace_set,relics,light_cone):
        super().__init__("罗刹",level,trace_set,relics,light_cone)
        self.apply_auto_skill_listener()
        self.auto_skill_counter = LuochaAutoSkillCoolDown()



    def normal_attack(self, targetSet):
        """
        罗刹普通攻击
        :param target: combat_obj 对象
        """
        current_target = targetSet.target
        attack_value = self.Attack
        radio = 1
        #TODO 读取罗刹普攻倍率
        base_damage = attack_value*radio
        # 罗刹对目标造成三段比例为0.3 0.3 0.4 的虚数普通攻击伤害 造成30点削韧
        attack(base_damage, DamageType.IMAGINARY, InteractMethod.NormalAttack, self, current_target, ToughnessReduce.Normal, [0.3, 0.3, 0.4])

        #罗刹普攻三段攻击 分裂比为 0.3，0.3，0.4 攻击力倍率


    def skill_attack(self,targetSet):
        """
        罗刹战技
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

    def apply_auto_skill_listener(self):

        pass


    def get_auto_skill_counter(self):
        return self.auto_skill_counter











