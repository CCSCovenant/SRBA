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

