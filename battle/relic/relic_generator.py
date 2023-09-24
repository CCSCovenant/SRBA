import random

from battle.data_manager import DataManager
from battle.relic.relic import Relic


def gen_relic(PART, ID,STAR=5,LEVEL=15, **kwargs):
    PART_MAPPING = {
        '1': ['HPDelta'],
        '2': ['AttackDelta'],
        '3': ['HPAddedRatio', 'AttackAddedRatio', 'DefenceAddedRatio', 'CriticalChanceBase', 'CriticalDamageBase',
               'HealRatioBase', 'StatusProbabilityBase'],
        '4': ['HPAddedRatio', 'AttackAddedRatio', 'DefenceAddedRatio', 'SpeedDelta'],
        '5': ['HPAddedRatio', 'AttackAddedRatio', 'DefenceAddedRatio', 'PhysicalAddedRatio', 'FireAddedRatio',
               'IceAddedRatio', 'ThunderAddedRatio', 'WindAddedRatio', 'QuantumAddedRatio', 'ImaginaryAddedRatio'],
        '6': ['BreakDamageAddedRatioBase', 'SPRatioBase', 'HPAddedRatio', 'AttackAddedRatio', 'DefenceAddedRatio']
    }

    CURRENT_MAPPING = PART_MAPPING[ID]
    #随机主属性
    if "MAIN_ATT" not in kwargs:
        MAIN_ATT = random.sample(CURRENT_MAPPING,1)
    else:
        MAIN_ATT = kwargs["MAIN_ATT"]

    SUB_ATT = {}
    SUB_ATT_STEP = {}
    #随机副属性
    if "SUB_ATT" not in kwargs:
        boost_time = LEVEL//3 + random.randint(0,1)
        #TODO 随机生成副词条
        pass
    else:
        pass



    relic = Relic(PART,STAR,LEVEL,MAIN_ATT,SUB_ATT,SUB_ATT_STEP,ID)
    return relic


def gen_relics(outer_ID, inner_ID, **kwargs):
    pass

