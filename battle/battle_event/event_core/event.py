from enum import Enum
from typing import List, Callable

class Event:
    def __int__(self):
        self._listeners: List[Callable] = []

    def add_listener(self, listener: Callable):
        self._listeners.append(listener)

    def remove_listener(self, listener: Callable):
        self._listeners.remove(listener)

    def trigger(self, *args, **kwargs):
        for listener in self._listeners:
            listener(*args, **kwargs)

class EntityEvent(Enum):
    NORMAL_ATTACK = 0
    SKILL_ATTACK = 1
    ULT_ATTACK = 2
    DAMAGE = 3
    FOLLOW_UP_ATTACK = 4
    UNDER_ATTACK = 5
    HP_CHANGE = 6
    MP_CHANGE = 7
    BUFF_CHANGE = 8
    SKILL_HEAL = 9
    UTL_HEAL = 10
    UNDER_HEAL = 11
    CYCLE_START = 12
    CYCLE_END = 13
class EnvEvent(Enum):
    GAME_START = 0
    ROUND_START = 1
    ROUND_END = 2
    GAME_END = 3
    SKILL_POINT_CHANGE = 4

