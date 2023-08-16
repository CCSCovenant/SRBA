import os.path
from battle.data_parser import parse_general_data,parse_relic_main_data,parse_relic_sub_data
def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

@singleton
class DataManager(object):
    def __init__(self):
        general_data_path = './battle_data/general_data/general_data_by_666bj_2.xlsx'
        current_dir = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_dir)
        data_path = os.path.join(current_dir,general_data_path)
        data_path = os.path.normpath(data_path)
        self.character_data, self.light_cone_data, self.level_up_data, self.skill_stance_and_energy_recover, self.skill_damage_distributed, self.skill_damage_mul, self.character_path, = parse_general_data(data_path)
        relic_main_data_path = './battle_data/relics/RelicMainAffixConfig.json'
        data_path = os.path.join(current_dir, relic_main_data_path)
        data_path = os.path.normpath(data_path)
        self.relic_main_data = parse_relic_main_data(data_path)
        relic_sub_data_path = './battle_data/relics/RelicSubAffixConfig.json'
        data_path = os.path.join(current_dir, relic_sub_data_path)
        data_path = os.path.normpath(data_path)
        self.relic_sub_data = parse_relic_sub_data(data_path)
        pass