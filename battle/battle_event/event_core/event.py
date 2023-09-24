from enum import Enum, auto
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
    NORMAL_ATTACK = auto
    SKILL_ATTACK = auto
    ULT_ATTACK = auto
    DAMAGE = auto
    FOLLOW_UP_ATTACK = auto
    UNDER_ATTACK = auto
    HP_CHANGE = auto
    MP_CHANGE = auto
    SPEED_CHANGE = auto
    STATUS_PROBABILITY_CHANGE = auto
    CRITICAL_RATE_CHANGE = auto
    CRITICAL_DAMAGE_CHANGE = auto
    STATUS_RESISTANCE_CHANGE = auto
    BUFF_CHANGE = auto
    SKILL_HEAL = auto
    UTL_HEAL = auto
    UNDER_HEAL = auto
    CYCLE_START = auto
    CYCLE_END = auto
class EnvEvent(Enum):
    GAME_START = 0
    ROUND_START = 1
    ROUND_END = 2
    GAME_END = 3
    SKILL_POINT_CHANGE = 4

