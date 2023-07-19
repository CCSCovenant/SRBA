def normal_damage(combat_obj_1, combat_obj_2):
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

    :param combat_obj_1: 战斗对象1
    :param combat_obj_2: 战斗对象2
    :return:
    """
    non_crit_damage = combat_obj_1.base_damage() * combat_obj_1.damage_mul_self() * combat_obj_2.damage_mul_opponent() * combat_obj_2.resistance_mul() * combat_obj_1.def_mul(
        combat_obj_2) * combat_obj_2.tenacity_mul() * combat_obj_1.sim_uni_mul(combat_obj_2)
    return non_crit_damage

    pass


