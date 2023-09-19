import os

from battle.data_parser import parse_general_data

general_data_path = '../battle/battle_data/general_data/general_data_by_666bj_2.xlsx'
current_dir = os.path.abspath(__file__)
current_dir = os.path.dirname(current_dir)
data_path = os.path.join(current_dir,general_data_path)
data_path = os.path.normpath(data_path)
parse_general_data(data_path)