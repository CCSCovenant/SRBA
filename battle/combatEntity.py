from enum import Enum

from battle.battle_event.event_core.event import EntityEvent, Event
from battle.timer import Timer


class CombatEntity:
    """
    CombatObj 用于储存角色和敌人的状态属性 包括各种基础数值和修正
    """
    def __init__(self,
                 Attack,
                 HP,
                 Defence,
                 Speed,
                 Hate,
                 StatusResistance,
                 TypeDamageRes,
                 CriticalChance,
                 CriticalDamage,
                 Level,
                 BreakDamage,
                 StatusProbability,
                 GameManager):
        """
        :param Attack: 攻击力 int
        :param HP: 生命值 int
        :param Defence: 防御力 int
        :param Speed: 速度 int
        :param Hate: 仇恨值
        :param StatusResistance: 效果抵抗 float 0-1
        :param TypeDamageRes: 属性抗性 float array 0-1
        :param CriticalChance: 暴击率 float e.g 5% = 5.0
        :param CriticalDamage: 暴击伤害 float e.g 50% = 50.0
        :param Level: 等级 int
        :param BreakDamage 击破特攻 double
        :param StatusProbability 效果命中 double
        :param GameManager 游戏管理器

        # 属性修正(加算)
        # AttackAddedRatio 攻击力比例修正
        # AttackDelta 攻击力修正
        # HPAddedRatio 生命值比例修正
        # HPDelta 生命值修正
        # DefenceAddedRatio 防御力比例修正
        # DefenceDelta 防御力修正
        # SpeedDelta 速度修正
        # DamageAddedRadio 伤害加成
        # TYPE_DMG_RES_ADJ
        # StatusResistanceBase 效果抵抗修正
        # CriticalChanceBase 暴击率修饰
        # CriticalDamageBase 暴击伤害修饰

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
        self.Attack = Attack
        self.maxHP = HP
        self.currentHP = HP
        self.Defence = Defence
        self.Speed = Speed
        self.HATE = Hate
        self.StatusResistance = StatusResistance
        self.TypeDamageRes = TypeDamageRes
        self.CriticalChance = CriticalChance
        self.CriticalDamage = CriticalDamage
        self.Level = Level
        self.BreakDamage = BreakDamage
        self.StatusProbability = StatusProbability
        self.HealAddedRadio = 0
        self.GameManager = GameManager

        # 基础数值
        self.BASE_Attack = Attack
        self.BASE_HP = HP
        self.BASE_Defence = Defence
        self.BASE_Speed = Speed
        self.BASE_StatusResistance = StatusResistance
        self.BASE_TypeDamageRes = TypeDamageRes
        self.BASE_CriticalChance = CriticalChance
        self.BASE_CriticalDamage = CriticalDamage
        self.BASE_Level = Level

        # 属性修正(比例加算)

        self.AttackAddedRatio = 0 #攻击力比例修正
        # HPAddedRatio 生命值比例修正
        # DefenceAddedRatio 防御力比例修正
        # DamageAddedRadio 伤害加成
        self.AttackDelta = 0 # 攻击力修正

        # HPDelta 生命值修正

        # DefenceDelta 防御力修正
        # SpeedDelta 速度修正

        # TYPE_DMG_RES_ADJ
        # StatusResistanceBase 效果抵抗修正
        # CriticalChanceBase 暴击率修饰
        # CriticalDamageBase 暴击伤害修饰
        self.ATK_ADJ = 0            # ATK_ADJ 攻击力修正
        self.HP_ADJ = 0             # HP_ADJ 生命值修正
        self.DEF_ADJ = 0            # DEF_ADJ 防御力修正
        self.SPEED_ADJ = 0          # SPEED_ADJ 速度修正
        self.TYPE_DMG_RES_ADJ = [0.0,0.0,0.0,0.0,0.0,0.0,0.0] # 抗性修正
        self.TYPE_DMG_PEN = [0.0,0.0,0.0,0.0,0.0,0.0,0.0] # 抗性穿透
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
        self.triggers = {}



    def add_adjust(self,state_adjust):
        self.state_adjust_list.append(state_adjust)
        state_adjust.on_add(self)

    def remove_adjust(self,state_adjust):
        state_adjust.on_remove()
        self.state_adjust_list.remove(state_adjust)

    def init_triggers(self):
        self.triggers.update(self.GameManager.triggers)

        EventList = [EntityEvent.NORMAL_ATTACK,EntityEvent.SKILL_ATTACK,EntityEvent.ULT_ATTACK,EntityEvent.DAMAGE,EntityEvent.FOLLOW_UP_ATTACK,EntityEvent.UNDER_ATTACK,EntityEvent.HP_CHANGE,EntityEvent.MP_CHANGE,EntityEvent.BUFF_CHANGE]

        for event in EventList:
            self.triggers[event] = Event()

    def heal(self,value):
        self.currentHP = max(self.currentHP+value,self.maxHP)
        self.triggers[EntityEvent.UNDER_HEAL].trigger(EntityEvent.UNDER_HEAL)


    def remove_current_debuff(self):
        # 移除当前的debuff
        pass

    def remove_current_buff(self):
        # 移除当前的buff
        pass

class DamageType(Enum):
    PHYSICAL = 0 # 物理属性伤害
    FIRE = 1 # 火属性伤害
    ICE = 2 # 冰属性伤害
    THUNDER = 3 # 雷属性伤害
    WIND = 4 # 风属性伤害
    QUANTUM = 5 # 量子属性伤害
    IMAGINARY = 6 # 虚数属性伤害

class InteractMethod(Enum):
    NormalAttack = 0
    SkillAttack = 1
    UltAttack = 2
    FollowUpAttack = 3

class ToughnessReduce(Enum):
    Normal = 30
    SKILL_SINGLE = 60
    SKILL_MULTI_MAIN = 60
    SKILL_MULTI_SUB = 30
    ULT_SINGLE = 90
    ULT_ALL = 60
    ULT_MULTI = 60







