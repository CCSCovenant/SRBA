import json
from enum import Enum

from battle.battle_event.event_core.event import EntityEvent, Event
from battle.timer import Timer


class CombatEntity:
    """
    CombatObj 用于储存角色和敌人的状态属性 包括各种基础数值和修正
    """

    def __init__(self, GameManager, **kwargs):
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
        """
        with open("./battle_data/property.json",'r') as property_file:
            defaultProperty = json.load(property_file)
        for attribute in defaultProperty:
            base_property = defaultProperty[attribute]
            if attribute in kwargs:
                base_property = kwargs[attribute]
            setattr(self, "Base_" + attribute, base_property)
            setattr(self, "Current_" + attribute, base_property)
            setattr(self, "DeltaAdd_" + attribute, 0)
            setattr(self, "RadioAdd_" + attribute, 0)

        self.MAX_HP = self.Current_HP
        self.Timer = Timer(self.Current_Speed, self)
        self.state_adjust_list = []
        self.triggers = {}

    def mod_property_delta(self, property_name, delta_value):
        # 更新数值增加
        # 获取当前增加的数值
        current_delta_value = getattr(self, "DeltaAdd_" + property_name)
        # 进行修正
        setattr(self, "DeltaAdd_" + property_name, current_delta_value + delta_value)
        # 更新现在的数值, 当前数值加上修正值
        current_value = getattr(self, "Current_" + property_name)
        setattr(self, "Current_" + property_name, current_value + delta_value)

    def mod_property_radio(self, property_name, delta_value):
        # 更新当前百分比增加的数值
        # 获取当前的百分比增幅
        if property_name is "DmgReduction":
            # 伤害减少是唯一乘算乘区 特例
            current_value = getattr(self, "RadioAdd_" + property_name)
            # 正值代表应用伤害 降低 负值代表降低伤害降低
            if delta_value > 0:
                setattr(self, "Current_" + property_name, current_value * (1 - delta_value))
            else:
                setattr(self, "Current_" + property_name, current_value * 1 / (1 + delta_value))

        else:
            current_radio_value = getattr(self, "RadioAdd_" + property_name)
            # 修正当前的百分比增幅
            setattr(self, "RadioAdd_" + property_name, current_radio_value + delta_value)
            # 获取基础值, 更新之后的百分比增幅 和 当前的数值增幅
            base_value = getattr(self, "Base_" + property_name)
            updated_radio = getattr(self, "RadioAdd_" + property_name)
            current_delta_value = getattr(self, "DeltaAdd_" + property_name)
            # 更新后的值
            current_value = base_value + updated_radio * base_value + current_delta_value
            # 更新目前的值
            setattr(self, "Current_" + property_name, current_value)

    def add_adjust(self, state_adjust):
        self.state_adjust_list.append(state_adjust)
        state_adjust.on_add(self)

    def remove_adjust(self, state_adjust):
        state_adjust.on_remove()
        self.state_adjust_list.remove(state_adjust)

    def init_triggers(self):
        self.triggers.update(self.GameManager.triggers)

        EventList = [EntityEvent.NORMAL_ATTACK, EntityEvent.SKILL_ATTACK, EntityEvent.ULT_ATTACK, EntityEvent.DAMAGE,
                     EntityEvent.FOLLOW_UP_ATTACK, EntityEvent.UNDER_ATTACK, EntityEvent.HP_CHANGE,
                     EntityEvent.MP_CHANGE, EntityEvent.BUFF_CHANGE]

        for event in EventList:
            self.triggers[event] = Event()

    def heal(self, value):
        self.currentHP = max(self.currentHP + value, self.maxHP)
        self.triggers[EntityEvent.UNDER_HEAL].trigger(EntityEvent.UNDER_HEAL)

    def remove_current_debuff(self):
        # 移除当前的debuff
        pass

    def remove_current_buff(self):
        # 移除当前的buff
        pass

    def apply_change(self):
        pass


class DamageType(Enum):
    PHYSICAL = 0  # 物理属性伤害
    FIRE = 1  # 火属性伤害
    ICE = 2  # 冰属性伤害
    THUNDER = 3  # 雷属性伤害
    WIND = 4  # 风属性伤害
    QUANTUM = 5  # 量子属性伤害
    IMAGINARY = 6  # 虚数属性伤害


class InteractMethod(Enum):
    NormalAttack = 0
    SkillAttack = 1
    UltAttack = 2
    FollowUpAttack = 3


class ToughnessReduce(Enum):
    NORMAL = 30
    SKILL_SINGLE = 60
    SKILL_MULTI_MAIN = 60
    SKILL_MULTI_SUB = 30
    ULT_SINGLE = 90
    ULT_ALL = 60
    ULT_MULTI = 60
