class EntityProperty():
    """
    负责储存实体属性和对其进行操作
    一个对象包括如下属性
        基础:
        ————————
        生命值
        攻击力
        防御力
        速度

        进阶
        ————————
        暴击率
        暴击伤害
        击破特供
        治疗量加成
        能量上限
        能量恢复效率
        效果命中
        效果抵抗
        属性伤害*7
        属性抗性*7
        属性穿透*7
        减伤
        虚弱
        易伤
        增伤

        其中基础属性可以同时加算和乘算
        进阶属性只能加算
    """
    def __init__(self):
        self.base_property = {}
        self.current_property = {}
        self.property_add_radio = {}
        self.property_add_delta = {}

    def append_property(self,property_name,base_value):
        self.base_property[property_name] = base_value
        self.current_property[property_name] = base_value
        self.property_add_radio[property_name] = 0
        self.property_add_delta[property_name] = 0
    def get_property(self,property_name):
        return self.current_property[property_name]

    def add_property_delta(self,property_name,delta_value):
        self.property_add_delta[property_name] = self.property_add_delta[property_name] + delta_value
        self.current_property[property_name] = self.current_property[property_name] + delta_value

    def add_property_radio(self,property_name,delta_value):
        self.property_add_radio[property_name] = self.property_add_radio[property_name] + delta_value
        self.current_property[property_name] = self.base_property[property_name]+self.base_property[property_name]*self.property_add_radio[property_name] + self.property_add_delta[property_name]
