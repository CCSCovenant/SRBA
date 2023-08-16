from battle.combat_obj import CombatObj
from battle.data_manager import DataManager


class Character(CombatObj):

    def __init__(self, character_name, level, trace_set, relics, light_cone):
        dm = DataManager()
        character_data = dm.character_data
        level_up_data = dm.level_up_data
        if character_name not in character_data:
            raise RuntimeError('此角色不存在 character does not existed')

        BASE_ATK = character_data[character_name]['基础攻击力'] * level_up_data[level]['角色系数']
        BASE_HP = character_data[character_name]['基础生命值'] * level_up_data[level]['角色系数']
        BASE_DEF = character_data[character_name]['基础防御力'] * level_up_data[level]['角色系数']
        BASE_SPEED = character_data[character_name]['基础速度']
        BASE_HATE =  character_data[character_name]['基础仇恨']

        BASE_ATK = BASE_ATK + light_cone.ATK
        BASE_HP = BASE_HP + light_cone.HP
        BASE_DEF = BASE_DEF + light_cone.DEF

        BASE_CRIT_RATE = 5.0
        BASE_CRIT_DMG = 50.0
        super().__init__(ATK=BASE_ATK,
                         HP=BASE_HP,
                         DEF=BASE_DEF,
                         SPEED=BASE_SPEED,
                         HATE=BASE_HATE,
                         DEBUFF_RES=0,
                         TYPE_DMG_RES=[0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                         CRIT_RATE=BASE_CRIT_RATE,
                         CRIT_DMG=BASE_CRIT_DMG,
                         LEVEL=level)

        self.ENERGY_LIMIT = character_data[character_name]['能量上限']
        pass

    def apply_trace(self,trace_set):
        pass

    def apply_relic(self,relics):
        for relic in relics:
            pass
        pass


