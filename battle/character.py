from battle.combatEntity import CombatEntity
from battle.data_manager import DataManager


class Character(CombatEntity):

    def __init__(self, character_name, level, trace_set, relics, light_cone):
        """

        :param character_name:
        :param level:
        :param trace_set: 一个int数组 trace_set[0-3] 代表普攻 战技 终结技 天赋等级 取值范围为1-15。 trace_set[4-6]为天赋状态 取值为0-1 1代表激活该天赋
        traceset[7-16]代表额外行迹 取值同样为0-1.
        :param relics:
        :param light_cone:
        """
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
        super().__init__(Attack=BASE_ATK,
                         HP=BASE_HP,
                         Defence=BASE_DEF,
                         Speed=BASE_SPEED,
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
            for att,value in relic.radioMod:
                self.mod_property_radio(att,value)
            for att,value in relic.deltaMod:
                self.mod_property_delta(att,value)
        

    def normal_attack(self, target):
        """
        :param target: combat_obj对象
        """
        pass
    def skill_attack(self,target):
        """
        :param target: combat_obj对象
        """
        pass

    def ult_attack(self, target):
        """
        :param target: combat_obj对象
        """
        pass


    def follow_up_attack(self, target):
        """
        :param target: combat_obj对象
        """
        pass

    def on_game_start(self):
        pass

    def on_round_start(self):
        pass

    def on_round_end(self):
        pass

    def on_cycle_start(self):
        pass

    def on_cycle_end(self):
        pass

    def on_hp_change(self,source):
        pass

    def on_mp_change(self,source):
        pass

    def on_buff_change(self,source):
        pass

    def on_skill_point_change(self,source):
        pass

    def under_attack(self,source):
        pass



