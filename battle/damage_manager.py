import random
from enum import Enum


def attack(base_damage, damage_type, InteractMethod, combatEntity_1, combatEntity_2, toughness_reduce, damage_dist):
    for radio in damage_dist:
        damage(base_damage * radio, damage_type, combatEntity_1, combatEntity_2, InteractMethod)
    combatEntity_2.on_attack()

def heal(base_heal,InteractMethod,combatEntity_1,combatEntity_2):
    #TODO combatEntity_1治疗combatEntity_2
    pass


def damage(base_damage, damage_type, combatEntity_1, combatEntity_2, InteractMethod):
    """
    伤害 =
    基础伤害区*
    增伤系数*
    易伤系数*
    减伤系数*
    虚弱系数*
    暴击系数*
    防御系数*
    抗性系数*
    特殊增伤系数*
    特殊易伤系数
    :param base_damage: 基础伤害 int
    :param damage_type: 伤害属性 int 0-7
    :param combatEntity_1: 攻击对象
    :param combatEntity_2: 受击对象
    :param damage_method: 伤害类型 int 0-2: 0:常规伤害 1:击破伤害 2:普通持续伤害
    :return: FINAL_DAMAGE: 最后伤害
    :return: is_CRIT: 是否暴击
    """

    #增伤系数
    DMG_INC_OPPONENT = 1 + combatEntity_1.DMG_INC_OPPONENT
    #易伤系数
    DMG_INC_SELF = 1 + combatEntity_2.DMG_INC_SELF
    #减伤系数
    DMG_DEC = 1 + combatEntity_2.DMG_REDUCE_OPPONENT
    #虚弱系数
    DMG_REDUCE = combatEntity_1.DMG_REDUCE_SELF
    #暴击系数
    CRIT = 1
    is_CRIT = False
    if random.random() >= combatEntity_1.CRIT_RATE:
        CRIT += combatEntity_1.CRIT_DMG
        is_CRIT = True
    #防御系数
    DEF_ADJ = combatEntity_2.DEF * (1 - combatEntity_2.DEF_REDUCE - combatEntity_1.DEF_PEN)
    DEF_REDUCE = (200 + combatEntity_1.LEVEL * 10) / (DEF_ADJ + 200 + 10 * combatEntity_1.LEVEL)
    #抗性系数
    RES_REDUCE = 1 - combatEntity_2.TYPE_DMG_RES[damage_type] + combatEntity_1.TYPE_DMG_PEN[damage_type]
    RES_REDUCE = max(min(RES_REDUCE, 2.0), 0.1) # 抗性系数被限制在10%-200%之内

    FINAL_DAMAGE = base_damage*DMG_INC_OPPONENT*DMG_INC_SELF*DMG_DEC*DEF_REDUCE*CRIT*DEF_REDUCE*RES_REDUCE
    return FINAL_DAMAGE,is_CRIT




