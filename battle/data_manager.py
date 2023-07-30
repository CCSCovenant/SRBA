import os.path
from battle.data_parser import parser_general_data
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
        path = './battle_data/general_data/general_data_by_666bj_2.xlsx'
        current_dir = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_dir)
        data_path = os.path.join(current_dir,path)
        data_path = os.path.normpath(data_path)
        self.character_data, self.light_cone_data, self.level_up_data, self.skill_stance_and_energy_recover, self.skill_damage_distributed, self.skill_damage_mul, self.character_path, = parser_general_data(data_path)



        pass