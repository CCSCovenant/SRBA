import pandas as pd

def paser_enemy_data():
    path = 'battle_data/enemy_data/enemy_base_data_by_666bj_2.xlsx'
    xls = pd.ExcelFile(path)
    sheet_names = xls.sheet_names
    print(sheet_names)
    for sheet_name in sheet_names:
        # 读取工作表内容
        df = pd.read_excel(xls, sheet_name)
        print(df)

    pass

def parser_general_data(path):

    xls = pd.ExcelFile(path)

    # 角色基础属性
    df = pd.read_excel(xls,'角色基础属性')
    character_data = {}
    for index, row in df.iterrows():
        character_data[row[0]] = row

    # 光锥基础属性
    df = pd.read_excel(xls, '光锥基础属性')
    light_cone_data = {}
    for index, row in df.iterrows():
        light_cone_data[row[0]] = row

    # 升级系数

    df = pd.read_excel(xls, '基础属性系数')
    level_up_data = {}
    for index, row in df.iterrows():
        level_up_data[row[0]] = row

    # 角色破韧和回能
    df = pd.read_excel(xls, '角色技能破韧和回能')
    skill_stance_and_energy_recover = {}
    for index, row in df.iterrows():
        skill_stance_and_energy_recover[row[0]] = row

    # 角色技能分裂百分比

    df = pd.read_excel(xls, '角色技能分裂比')
    skill_damage_distributed = {}
    for index, row in df.iterrows():
        skill_damage_distributed[row[0]] = row

    # 技能倍率表

    df = pd.read_excel(xls, '角色技能倍率表')
    skill_damage_mul = {}
    for index, row in df.iterrows():
        skill_damage_mul[row[0]] = row

    # 角色行迹

    df = pd.read_excel(xls, '角色行迹')
    character_path = {}
    for index, row in df.iterrows():
        character_path[row[0]] = row

    return character_data,light_cone_data,level_up_data,skill_stance_and_energy_recover,skill_damage_distributed,skill_damage_mul,character_path


