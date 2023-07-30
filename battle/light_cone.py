from battle.data_manager import DataManager


class LightCone:
    def __init__(self, light_cone_name, level):
        dm = DataManager()
        light_cone_data = dm.light_cone_data
        level_up_data = dm.level_up_data
        if light_cone_name not in light_cone_data:
            raise RuntimeError('此光锥不存在 light cone does not existed')
        self.HP = light_cone_data[light_cone_name]['基础生命值'] * level_up_data[level]
        self.ATK = light_cone_data[light_cone_name]['基础攻击力'] * level_up_data[level]
        self.DEF = light_cone_data[light_cone_name]['基础防御力'] * level_up_data[level]
