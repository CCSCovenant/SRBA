class Timer:
    """
    每个在场对象都有一个内置timer. 在每次事件以后通过更新timer来决定下一个行动对象
    时间戳最小的对象开始行动 并将当前时间戳更新为此时间戳
    """
    next_round_distance = 10000
    next_move_time = 0
    speed = 0

    def __int__(self, speed,combatObj):
        """
          初始化第一次入场的速度.
          入场加减速/推拉条由rules负责
          行动值 = 剩余路程/速度
          例如 125速对象下次行动时间为10000/125 = 80
        """
        self.combatObj = combatObj
        self.next_round_distance = 10000
        self.speed = speed
        self.next_move_time = self.next_round_distance / self.speed
        pass

    def get_next_round(self):
        """
        获得下一个回合的时间戳
        """
        return self.next_move_time

    def get_move_time(self):
        """
        获取行动值
        """
        return self.next_move_time

    def move(self):
        """
        角色行动
        -当前路程重置
        -计算下次移动时间戳
        """
        self.next_move_time = self.next_round_distance / self.speed
        self.combatObj.round_end_process()

    def change_speed(self, new_speed):
        """
        更新速度
        new_speed: 新的速度
        """
        self.next_move_time = self.next_move_time*(self.speed/new_speed) # 更新下次行动时间
        self.speed = new_speed # 更新速度
        pass



    def change_distance(self, value):
        """
        推/拉条动作 提高剩余路程
        value: 推拉条比例. 是一个整数 推条为正 拉条为负.
        e.g 推条16%：value = 16
        e.g 拉条25%：value = -25
        """
        total_move_time = self.next_round_distance/self.speed #计算行动条总长
        next_move_adj = (total_move_time * value) / 100 # 计算行动值变化
        self.next_move_time  = self.next_move_time + next_move_adj # 更新下次行动时间
        self.next_move_time  = min(0,self.next_move_time ) # 拉条以后剩余行动值必须大于等于0

    def __lt__(self, other):
        """重载小于运算符"""
        return self.next_move_time < other.next_move_time



