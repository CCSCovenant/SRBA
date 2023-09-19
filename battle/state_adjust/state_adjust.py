
class StateAdjust:
    def __init__(self,is_removeable,type,sourceEntity,targetEntity,triggerList):
        """
        :param is_removeable: 是否可以被解除 0代表不可移除，1代表可以移除
        :param type: 正面/负面效果 0代表正面 1 代表负面
        :param sourceEntity: 施加对象
        :param targetEntity: 生效的对象
        :param triggerList: 需要注册的触发器类型
        """
        self.is_removeable = is_removeable
        self.type = type
        self.sourceEntity = sourceEntity
        self.targetEntity = targetEntity
        self.triggerList = triggerList


    def trigger_list(self):
        """
        :return:返回需要注册的事件类型
        """
        return self.triggerList

    def on_add(self):
        pass

    def on_remove(self):
        pass

    def on_trigger(self,EventType):

        pass

