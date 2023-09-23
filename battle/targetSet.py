from enum import Enum


class TargetSet:
    """
    TargetSet用于为角色的普攻/战技/终结技提供目标

    """
    def __init__(self, type, **kwargs):
        self.type = type

        if self.type == TargetType.SINGLE:
            if "target" not in kwargs:
                raise ValueError("TargetType.SINGLE requires 'target' argument.")
            self.target = kwargs["target"]

        elif self.type == TargetType.MAIN_AND_SUB:
            if "main_target" not in kwargs or "sub_targets" not in kwargs:
                raise ValueError("TargetType.MAIN_AND_SUB requires 'main_target' and 'sub_targets' arguments.")
            self.main_target = kwargs["main_target"]
            self.sub_targets = kwargs["sub_targets"]

        elif self.type == TargetType.MULTIPLE:
            if "targets" not in kwargs:
                raise ValueError("TargetType.MULTIPLE requires 'targets' argument.")
            self.targets = kwargs["targets"]

        else:
            raise ValueError("Invalid type!")


class TargetType(Enum):
    SINGLE = 0 # 单攻
    MULTI = 1 # 扩散
    ALL = 2 # 群攻

