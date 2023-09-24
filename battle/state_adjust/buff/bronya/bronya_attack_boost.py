from battle.battle_event.event_core.event import EntityEvent
from battle.data_manager import DataManager
from battle.state_adjust.state_adjust import StateAdjust, STATES


class BronyaAttackBoost(StateAdjust):
    def __init__(self, sourceEntity, targetEntity):
        triggerList = [EntityEvent.CYCLE_END]
        super().__init__(STATES.notRemoveAble, STATES.buff, sourceEntity, targetEntity, triggerList)
        dm = DataManager()
        df = dm.skill_damage_mul
        # TODO 读取 布洛妮娅的行迹天赋等级
        trace_level = 10
        radio = df[(df['角色'] == '布洛妮娅') & (df['技能'] == '天赋') & (df['名称'] == '先人一步')][trace_level].iloc[
            0]

        # TODO 获取布洛妮娅天赋拉条数值
        self.boost = radio
    def on_trigger(self,**kwargs):
        self.sourceEntity.Timer.change_distance(self.boost)
        self.remove_self()
