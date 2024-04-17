from typing import TypeVar, Callable

T = TypeVar('T')

class Container():
    instances = {}
    @staticmethod
    def make(className: T)-> T:
        classStr = className.__module__
        if classStr not in Container.instances:
            obj = className()
            Container.instances[classStr] = obj
            return obj
        else:
            return Container.instances[classStr]

