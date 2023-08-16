import re

from battle.data_manager import DataManager


class Relic:
    """
    PART: 遗器的位置 1:头 2:手 3:躯干 4：脚部 5:球 6:绳 string
    STAR: 遗器的星级 2,3,4,5 string
    LEVEL: 遗器的等级
    MAIN_ATT: 遗器的主属性
    SUB_ATT: 遗器的副属性 是一个dict. key是副属性的id
    SUB_ATT[dict] 储存对应的强化次数
    SUB_ATT_STEP: 遗器的副属性 是一个dict. key是副属性的id
    SUB_ATT_STEP[dict]: 储存对应的‘偏移量’ e.g 强化档次之和

    ID: 遗器的套装ID. 用于判断遗器套装效果

    """
    __TypeMapping__ = {"Physical":0,"Fire":1,"Ice":2,"Thunder":3,"Wind":4,"Quantum":5,"Imaginary":6}
    def __init__(self,PART,STAR,LEVEL,MAIN_ATT,SUB_ATT,SUB_ATT_STEP,ID):
        self.AttackAddedRatio = 0  #  攻击力比例修正
        self.AttackDelta = 0 # 攻击力加算
        self.HPAddedRatio = 0  # 生命值比例修正
        self.HPDelta = 0  # 生命值加算
        self.DefenceAddedRatio = 0  # 防御力比例修正
        self.DefenceDelta = 0  # 防御力加算
        self.SpeedDelta = 0  #速度加算
        self.BreakDamageAddedRatioBase = 0 #击破特攻
        self.SPRatioBase = 0 # 充能效率
        self.TypeDamageAddedRadio = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # 属性伤害比例修正
        self.StatusResistanceBase = 0  # 效果抵抗修正
        self.CriticalChanceBase = 0.0  # 暴击率修正
        self.CriticalDamageBase = 0.0  # 暴击伤害修正
        self.HealRatioBase = 0.0 # 治疗提升
        self.StatusProbabilityBase = 0.0 # 效果命中
        self.ID = ID

        dm = DataManager()
        relic_main_att = dm.relic_main_data
        main_relic_id = PART+STAR
        relic_main = relic_main_att[main_relic_id]
        BaseValue,LevelAdd = self.get_values_from_property(relic_main,MAIN_ATT)
        bool,value = self.check_att(MAIN_ATT)
        if bool:
            self.TypeDamageAddedRadio[self.__TypeMapping__[value]] = BaseValue+LevelAdd*LEVEL
        else:
            current_value = getattr(self, MAIN_ATT)
            setattr(self, MAIN_ATT, current_value + BaseValue + LevelAdd * LEVEL)

        relic_sub_att = dm.relic_sub_data
        relic_sub = relic_sub_att[STAR]
        for key in SUB_ATT:
            BaseValue, StepValue = self.get_values_from_sub_property(relic_sub, key)
            Bases = SUB_ATT[key]
            Steps = SUB_ATT_STEP[key]
            current_value = getattr(self, key)
            setattr(self, key, current_value + Bases * BaseValue + Steps * StepValue)

    def get_values_from_property(self,data, target_property):
        # 遍历 JSON 数据
        for group_id, group_data in data.items():
            for affix_id, affix_data in group_data.items():
                if affix_data['Property'] == target_property:
                    base_value = affix_data['BaseValue']['Value']
                    level_add = affix_data['LevelAdd']['Value']
                    return base_value, level_add
        # 如果没有找到对应的 Property，返回 None
        raise RuntimeError('No such att for target relic: 对应的遗器没有指定的属性')
    def get_values_from_sub_property(self,data, target_property):
        # 遍历 JSON 数据
        for group_id, group_data in data.items():
            for affix_id, affix_data in group_data.items():
                if affix_data['Property'] == target_property:
                    base_value = affix_data['BaseValue']['Value']
                    level_add = affix_data['StepValue']['Value']
                    return base_value, level_add
        # 如果没有找到对应的 Property，返回 None
        raise RuntimeError('No such att for target relic: 对应的遗器没有指定的属性')

    def check_att(self,att):
        pattern = r'^(Physical|Fire|Ice|Thunder|Wind|Quantum|Imaginary)AddedRadio$'
        match = re.match(pattern, att)

        if match:
            return True, match.group(1)

        return False, None