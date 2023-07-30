from battle.timer import Timer


class CombatObj:
    """
    CombatObj 用于储存角色和敌人的状态属性 包括各种基础数值和修正
    """
    def __init__(self,
                 ATK,
                 HP,
                 DEF,
                 SPEED,
                 HATE,
                 DEBUFF_RES,
                 TYPE_DMG_RES,
                 CRIT_RATE,
                 CRIT_DMG,
                 LEVEL,
                 TOUGHNESS_ADJ,
                 EVENT_LIST):
        """
        :param ATK: 攻击力 int
        :param HP: 生命值 int
        :param DEF: 防御力 int
        :param SPEED: 速度 int
        :param HATE: 仇恨值
        :param DEBUFF_RES: 效果抵抗 float 0-1
        :param TYPE_DMG_RES: 属性抗性 float array 0-1
        :param CRIT_RATE: 暴击率 float e.g 5% = 5.0
        :param CRIT_DMG: 暴击伤害 float e.g 50% = 50.0
        :param LEVEL: 等级 int
        :param TOUGHNESS_ADJ 击破特攻 double
        :param EVENT_LIST 角色有的所有事件

        # 属性修正(加算)
        # ATK_ADJ 攻击力修正
        # HP_ADJ 生命值修正
        # DEF_ADJ 防御力修正
        # SPEED_ADJ 速度修正
        # TYPE_DMG_RES_ADJ
        # DEBUFF_RES_ADJ #效果抵抗修正
        # CRIT_RATE_ADJ 暴击率修饰
        # CRIT_DMG_ADJ 暴击伤害修饰

        # 伤害区修正(乘算)
        # DMG_INC_SELF 己方易伤系数
        # DMG_INC_OPPONENT 乙方增伤系数
        # DMG_REDUCE_SELF 己方虚弱系数系数
        # DMG_REDUCE_OPPONENT 己方减伤系数

        # DEF_PEN 防御穿透
        # DEF_REDUCE 防御降低

        # RES_PEN 抗性穿透

        # 特殊伤害乘区(暂不使用)
        # SPEC_DMG_INC_SELF
        # SPEC_DMG_INC_OPPONENT
        """
        #当前数值
        self.ATK = ATK
        self.HP = HP
        self.DEF = DEF
        self.SPEED = SPEED
        self.HATE = HATE
        self.DEBUFF_RES = DEBUFF_RES
        self.TYPE_DMG_RES = TYPE_DMG_RES
        self.CRIT_RATE = CRIT_RATE
        self.CRIT_DMG = CRIT_DMG
        self.LEVEL = LEVEL
        self.TOUGHNESS_ADJ = TOUGHNESS_ADJ

        # 基础数值
        self.BASE_ATK = ATK
        self.BASE_HP = HP
        self.BASE_DEF = DEF
        self.BASE_SPEED = SPEED
        self.BASE_DEBUFF_RES = DEBUFF_RES
        self.BASE_TYPE_DMG_RES = TYPE_DMG_RES
        self.BASE_CRIT_RATE = CRIT_RATE
        self.BASE_CRIT_DMG = CRIT_DMG
        self.BASE_LEVEL = LEVEL

        # 属性修正(加算)

        self.ATK_ADJ = 0            # ATK_ADJ 攻击力修正
        self.HP_ADJ = 0             # HP_ADJ 生命值修正
        self.DEF_ADJ = 0            # DEF_ADJ 防御力修正
        self.SPEED_ADJ = 0          # SPEED_ADJ 速度修正
        self.TYPE_DMG_RES_ADJ = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.TYPE_DMG_PEN = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.DEBUFF_RES_ADJ = 0     # DEBUFF_RES_ADJ 效果抵抗修正
        self.CRIT_RATE_ADJ = 0.0    # CRIT_RATE_ADJ 暴击率修饰
        self.CRIT_DMG_ADJ = 0.0     # CRIT_DMG_ADJ 暴击伤害修饰

        # 伤害区修正(乘算)

        self.DMG_INC_SELF = 0.0     # DMG_INC_SELF 己方易伤系数
        self.DMG_INC_OPPONENT = 0.0 # DMG_INC_OPPONENT 乙方增伤系数
        self.DMG_REDUCE_SELF = 0.0  # DMG_REDUCE_SELF 己方虚弱系数系数
        self.DMG_REDUCE_OPPONENT = 0.0 # DMG_REDUCE_OPPONENT 己方减伤系数

        self.DEF_PEN = 0.0          # DEF_PEN 防御穿透
        self.DEF_REDUCE = 0.0       # DEF_REDUCE 防御降低

        self.RES_PEN = 0.0          # RES_PEN 抗性穿透

        # 特殊伤害乘区(暂不使用)
        # SPEC_DMG_INC_SELF
        # SPEC_DMG_INC_OPPONENT
        self.Timer = Timer(self.SPEED,self)
        self.state_adjust_list = []
    def round_end_process(self):
        pass

    def add_adjust(self,state_adjust):
        self.state_adjust_list.append(state_adjust)
        state_adjust.on_add(self)

    def remove_adjust(self,state_adjust):
        state_adjust.on_remove()
        self.state_adjust_list.remove(state_adjust)