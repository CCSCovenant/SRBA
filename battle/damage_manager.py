import random

def damage(base_damage,combat_obj_1, combat_obj_2):
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
    :param base_damage: 基础伤害
    :param combat_obj_1: 攻击对象
    :param combat_obj_2: 受击对象
    :return:
    """

    #增伤系数
    DMG_INC_OPPONENT = 1+combat_obj_1.DMG_INC_OPPONENT
    #易伤系数
    DMG_INC_SELF = 1+combat_obj_2.DMG_INC_SELF
    #减伤系数
    DMG_DEC = 1+combat_obj_2.DMG_REDUCE_OPPONENT
    #虚弱系数
    DMG_REDUCE = combat_obj_1.DMG_REDUCE_SELF
    #暴击系数
    CRIT = 1
    if random.random() >= combat_obj_1.CRIT_RATE:
        CRIT += combat_obj_1.CRIT_DMG
    
    return

    pass


