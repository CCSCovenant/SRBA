import re
from enum import Enum, auto

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
    __TypeMapping__ = {"Fire":0,"Ice":1,"Thunder":3,"Physical":0,"Wind":4,"Quantum":5,"Imaginary":6}

    def __init__(self,PART,STAR,LEVEL,MAIN_ATT,SUB_ATT,SUB_ATT_STEP,ID):
        #TODO 完成遗器修正值的填写TAT

        self.radioMod = {}
        self.deltaMod = {}

        dm = DataManager()
        relic_main_att = dm.relic_main_data
        main_relic_id = PART+STAR
        relic_main = relic_main_att[main_relic_id]
        BaseValue,LevelAdd = self.get_values_from_property(relic_main,MAIN_ATT)


        Att_Name,isDelta = self.process_string(MAIN_ATT)

        if isDelta:
            self.deltaMod[Att_Name] = BaseValue+LevelAdd*(LEVEL-1)
        else:
            self.radioMod[Att_Name] = BaseValue+LevelAdd*(LEVEL-1)

        relic_sub_att = dm.relic_sub_data
        relic_sub = relic_sub_att[STAR]
        for key in SUB_ATT:
            BaseValue, StepValue = self.get_values_from_sub_property(relic_sub, key)
            Bases = SUB_ATT[key]
            Steps = SUB_ATT_STEP[key]
            Att_Name, isDelta = self.process_string(key)
            if isDelta:
                current = self.deltaMod[Att_Name]
                self.deltaMod[Att_Name] = current + Bases*BaseValue + StepValue*Steps
            else:
                current = self.radioMod[Att_Name]
                self.radioMod[Att_Name] = current + Bases*BaseValue + StepValue*Steps
        self.ID = ID

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

    def process_string(s: str) -> (str, bool):
        # 检测字符串是否以'delta'结尾
        if s.endswith('Delta'):
            # 移除'delta'并返回
            return s[:-5], False
        else:
            # 移除所有'AddedRatio'和'Base'实例
            s = s.replace('AddedRatio', '').replace('Base', '')
            return s, False

class Parts(Enum):
    HEAD = "1"
    HANDS = "2"
    BODY = "3"
    FEET = "4"
    SPHERE = "5"
    ROPE = "6"

class RID(Enum):
    云无留迹的过客 = auto
    野穗相伴的快枪手 = auto
    净庭教宗的圣骑士 = auto
    密林卧雪的猎人 = auto
    街头出身的拳王 = auto
    戍卫风雪的铁卫 = auto
    宝命长存的莳者 = auto
    晨昏交界的翔鹰 = auto
    流星追迹的怪盗 = auto
    激奏雷电的乐队 = auto
    熔岩锻铸的火匠 = auto
    盗匪荒漠的废土客 = auto
    繁星璀璨的天才 = auto
    折断的龙骨 = auto
    繁星竞技场 = auto
    不老者的仙舟 = auto
    停转的萨尔索图 = auto
    太空封印站 = auto
    星体差分机 = auto
    泛银河商业公司 = auto
    生命的翁瓦克 = auto
    盗贼公国塔利亚 = auto
    筑城者的贝洛伯格 = auto
