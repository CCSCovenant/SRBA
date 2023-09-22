from battle.battle_event.event_core.event import EntityEvent
from battle.state_adjust.buff.absBuff.TimeRestrictStatesBuff import TimeRestrictStatesBuff
from battle.state_adjust.state_adjust import StateAdjust, STATES


class BronyaUltBuff(TimeRestrictStatesBuff):
    def __init__(self, sourceEntity, targetEntity):
        super().__init__(sourceEntity, targetEntity, 2)

    def applyStatesBuff(self):
        # TODO 读取布洛妮娅终结技倍率 （攻击力提高, 暴伤基础 爆伤额外）
        # TODO 读取布洛妮娅暴击倍率
        self.attack_boost_radio = 0.46
        critical_damage_increase_delta = 0.145
        critical_damage_increase_radio = 0.17
        self.critical_damage_increase = critical_damage_increase_delta + critical_damage_increase_radio * self.CriticalDamage
        # TODO 对目标实体施加buff
        pass
