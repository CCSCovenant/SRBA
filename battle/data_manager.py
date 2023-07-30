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
        path = '/battle_data/general_data/general_data_by_666bj_2.xlsx'
        self.character_data, self.light_cone_data, self.level_up_data, self.skill_stance_and_energy_recover, self.skill_damage_distributed, self.skill_damage_mul, self.character_path, = parser_general_data(path)



        pass