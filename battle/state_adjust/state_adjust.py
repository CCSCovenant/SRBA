
class StateAdjust:
    def __init__(self,type,is_removeable,counter,CombatObj):
        self.type = type
        self.is_removeable = is_removeable
        self.counter = counter
        self.CombatObj = CombatObj


    def on_add(self):
        pass

    def on_remove(self):
        pass

    def on_round_end(self):
        if self.counter == 0:
            self.CombatObj.remove_adjust(self)
        else:
            self.counter = self.counter - 1

