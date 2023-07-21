import openpyxl

def paser_enemy_data():
    path = 'battle_event/enemy/enemy_base_data_by_666bj.xlsx'
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    print(type(sheet_obj))

    pass


paser_enemy_data()