
class Timer:

    next_round_distance = 10000
    remain_distance = 10000
    next_move_time = 0
    def __int__(self,speed):
        pass

    '''
    获得下一个回合的时间戳 
    mei
    '''
    def get_next_round(self):

        return None

    '''
    获取行动值
    时间戳的数据比行动值多 此函数用于后期可视化用
    '''
    def get_WT(self):
        pass
    '''
    角色行动
    -当前路程归零
    
    '''
    def move(self):
        self.remain_distance = 0

    '''
    当任意事件执行完毕以后 更新剩余距离 用于计算推拉条
    time: 当前时间的时间戳
    '''
    def update_remain_distance(self,time):
        pass

    '''
    更新速度 
    new_speed: 新的速度
    time: 当前时间戳
    '''
    def change_speed(self,new_speed,time):

        self.update_remain_distance(time)
        pass
    '''
    推/拉条动作 提高剩余路程
    value: 推拉条比例. 是一个整数 推条为正 拉条为负. 
    e.g 推条16%：value = 16
    e.g 拉条25%：value = -25
    time: 当前时间戳
    '''
    def change_distance(self,value,time):

        self.update_remain_distance(time)

        pass





