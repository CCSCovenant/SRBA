
class Character:
    #ATK 攻击力
    #DEF 防御力
    #SPEED 速度

    def __int__(self,rule_list):
        pass

    def on_event(self):
        pass

    def damage(self,enemy):

        non_crit_damage = self.base_damage()*self.damage_mul_self()*enemy.damage_mul_opponent()*enemy.resistance_mul()*self.def_mul(enemy)*enemy.tenacity_mul()*self.sim_uni_mul(enemy)
        return non_crit_damage

        pass

    def base_damage(self):
        #TODO
        pass
    def damage_mul_self(self):
        # TODO
        pass
    def damage_mul_opponent(self):
        # TODO
        pass

    def crit_mul(self,enemy):
        # TODO
        pass
    def resistance_mul(self,enemy):
        # TODO
        pass
    def def_mul(self,enemy):
        # TODO
        pass
    def tenacity_mul(self,enemy):
        # TODO
        pass
    def sim_uni_mul(self,enemy):
        # will not use it for now
        return 1