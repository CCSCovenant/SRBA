'''
事件轴由一系列事件构成事件轴构成
每个事件结束后 game_manager 会通过
遍历检查事件组中每个事件的 is_event_active 检查事件是否激活

如果事件激活 执行 event_end_check()
如果事件未激活 执行event_start_check()


如果事件从未激活转移到激活 执行 on_event_start 函数
如果事件从激活转移到未激活 执行 on_event_end 函数
如果事件保持激活 执行 on_event_run 函数
如果事件保持未激活 不执行任何操作
'''
class Event:
    def __int__(self):
        pass


    def is_event_active(self,GameManager):

        pass

    def event_start_check(self,GameManager):

        pass

    def event_end_check(self,GameManager):
        pass
    def on_event_start(self,GameManager):
        pass

    def on_event_end(self,GameManager):
        pass

    def on_event_run(self,GameManager):
        pass
