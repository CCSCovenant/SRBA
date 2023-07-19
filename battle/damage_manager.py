import random

def damage(base_damage,damage_type,combat_obj_1, combat_obj_2):
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
    :param damage_type: 伤害类型 int 0-7
    :param combat_obj_1: 攻击对象
    :param combat_obj_2: 受击对象
    :return: FINAL_DAMAGE: 最后伤害
    :return: is_CRIT: 是否暴击
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
    is_CRIT = False
    if random.random() >= combat_obj_1.CRIT_RATE:
        CRIT += combat_obj_1.CRIT_DMG
        is_CRIT = True
    #防御系数
    DEF_ADJ = combat_obj_2.DEF * (1-combat_obj_2.DEF_REDUCE - combat_obj_1.DEF_PEN)
    DEF_REDUCE = (200 + combat_obj_1.LEVEL * 10) / ( DEF_ADJ + 200 + 10 * combat_obj_1.LEVEL )
    #抗性系数
    RES_REDUCE = 1 - combat_obj_2.TYPE_DMG_RES[damage_type] + combat_obj_1.TYPE_DMG_PEN[damage_type]
    RES_REDUCE = max(min(RES_REDUCE, 2.0), 0.1) # 抗性系数被限制在10%-200%之内

    FINAL_DAMAGE = base_damage*DMG_INC_OPPONENT*DMG_INC_SELF*DMG_DEC*DEF_REDUCE*CRIT*DEF_REDUCE*RES_REDUCE
    return FINAL_DAMAGE,is_CRIT



